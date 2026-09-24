#!/usr/bin/env python3
"""C-50 / C-56 / C-NEW-02: extract the SQL lab kit printed in the SQL companion's §3.8 and re-run every exercise key
against a throwaway local PostgreSQL cluster, then compare each fingerprint with the golden the course prints.

Usage:  kit_verify.py ROOT [--pgbin DIR] [--out REPORT.md] [--keep]

Nothing is downloaded. The cluster lives in a temporary directory, listens only on a Unix socket plus 127.0.0.1:54329,
runs with timezone UTC and C collation (the kit's pins), and is removed afterwards unless --keep. The goldens in the
course are never edited (invariant 6): a mismatch is reported, not "fixed".
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SQLF = "sql-databases-companion.md"
RUNNERS = ["ex_l1_4", "ex_l5_8", "ex_l9_13", "ex_l14"]


def extract(root, dest):
    L = open(os.path.join(root, "work", SQLF), encoding="utf-8").read().split("\n")
    s = next(i for i, l in enumerate(L) if l.startswith("### 3.8 "))
    e = next(i for i in range(s + 1, len(L)) if L[i].startswith("## ") or L[i].startswith("### 3.9"))
    names, cur, buf, inside = [], None, [], False
    for l in L[s:e]:
        m = re.match(r"^#### `([\w.]+)`$", l)
        if m and not inside:
            cur = m.group(1)
            continue
        if l.startswith("```"):
            if inside:
                open(os.path.join(dest, cur), "w", encoding="utf-8").write("\n".join(buf) + "\n")
                names.append(cur)
                buf, inside = [], False
            elif cur:
                inside = True
            continue
        if inside:
            buf.append(l)
    return names


def sh(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = os.path.abspath(args[0] if args else ".")
    pgbin = sys.argv[sys.argv.index("--pgbin") + 1] if "--pgbin" in sys.argv else "/usr/lib/postgresql/16/bin"
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else os.path.join(root, "kit-verification.md")
    tmp = tempfile.mkdtemp(prefix="sqlkit-")
    kit, data = os.path.join(tmp, "kit"), os.path.join(tmp, "pgdata")
    os.makedirs(kit)
    names = extract(root, kit)
    user = []
    if os.geteuid() == 0:                        # initdb refuses to run as root
        shutil.chown(tmp, "postgres")
        user = ["runuser", "-u", "postgres", "--"]
        os.chmod(tmp, 0o755)
    r = sh(user + [f"{pgbin}/initdb", "-D", data, "-U", "lab", "--locale=C", "--encoding=UTF8", "-A", "trust"])
    if r.returncode:
        raise SystemExit("initdb failed: " + r.stderr[-400:])
    conf = os.path.join(data, "postgresql.conf")
    with open(conf, "a") as fh:
        fh.write(f"\nport = 54329\nlisten_addresses = '127.0.0.1'\nunix_socket_directories = '{tmp}'\n"
                 "timezone = 'UTC'\nfsync = off\n")
    r = sh(user + [f"{pgbin}/pg_ctl", "-D", data, "-l", os.path.join(tmp, "pg.log"), "-w", "start"])
    if r.returncode:
        raise SystemExit("pg_ctl start failed: " + r.stderr[-400:])
    env = dict(os.environ, PGHOST="localhost", PGPORT="54329", PGUSER="lab", PGDATABASE="labdb")
    rows, report = [], {}
    try:
        sh([f"{pgbin}/createdb", "-h", "localhost", "-p", "54329", "-U", "lab", "labdb"], env=env)
        ver = sh(["psql", "-At", "-X", "-c", "SHOW server_version"], env=env).stdout.strip()
        r = sh(["psql", "-X", "-q", "-v", "ON_ERROR_STOP=1", "-f", "lab_schema.sql", "-f", "lab_seed.sql"],
               env=env, cwd=kit)
        if r.returncode:
            raise SystemExit("schema/seed load failed: " + r.stderr[-600:])
        for mod in RUNNERS:
            want = json.load(open(os.path.join(kit, f"goldens_{mod}.json"), encoding="utf-8"))
            os.rename(os.path.join(kit, f"goldens_{mod}.json"), os.path.join(kit, f"printed_{mod}.json"))
            r = sh([sys.executable, "run_ex.py", mod], env=dict(env, LAB_ALLOW_PG_MAJOR=ver.split(".")[0]), cwd=kit)
            if r.returncode:
                raise SystemExit(f"run_ex.py {mod} failed: " + (r.stderr or r.stdout)[-600:])
            got = json.load(open(os.path.join(kit, f"goldens_{mod}.json"), encoding="utf-8"))
            for k in want:
                g0, g1 = want[k].get("golden"), got.get(k, {}).get("golden")
                rows.append((mod, k, g0, g1, "match" if g0 == g1 else "golden-unreproduced"))
        # the trap fingerprints: each canonical wrong query through lab.chk, against goldens_wrong.json
        sys.path.insert(0, kit)
        import wrongs   # noqa: E402  (the kit's own file, extracted above)
        want = json.load(open(os.path.join(kit, "goldens_wrong.json"), encoding="utf-8"))
        for k, (why, q) in wrongs.WRONG.items():
            q = q.replace("'", "''")
            g1 = sh(["psql", "-At", "-X", "-c", f"SELECT lab.chk('{q}')"], env=env).stdout.strip() or None
            g0 = want.get(k, {}).get("golden")
            rows.append(("wrongs", k, g0, g1, "match" if g0 == g1 else "golden-unreproduced"))
        report["version"] = ver
    finally:
        sh(user + [f"{pgbin}/pg_ctl", "-D", data, "-m", "fast", "stop"])
        if "--keep" not in sys.argv:
            shutil.rmtree(tmp, ignore_errors=True)
    ok = sum(1 for r in rows if r[4] == "match")
    md = ["# SQL lab kit verification (C-50, C-56, C-NEW-02)", "",
          "Generated by `refactor-tools/kit_verify.py` (re-run: `python3 refactor-tools/kit_verify.py .`). The kit is "
          "extracted from the SQL companion's §3.8 (the course text, not the learner's machine copy), loaded into a "
          "throwaway local cluster with timezone UTC and C collation, and every exercise key is run by the kit's own "
          "`run_ex.py`. The printed goldens are compared, never edited (invariant 6).", "",
          f"- Files extracted from §3.8: {len(names)} ({', '.join(names)})",
          f"- Server: PostgreSQL {report.get('version', '?')} (the kit pins 15.x; run under `LAB_ALLOW_PG_MAJOR`, "
          "so the deviation is recorded here)",
          f"- Keys run: {len(rows)} · match: {ok} · golden-unreproduced: {len(rows) - ok}", "",
          "| Runner | Key | Printed golden | Re-run | Status |", "|---|---|---|---|---|"]
    md += [f"| {a} | {b} | `{c}` | `{d}` | {e} |" for a, b, c, d, e in rows]
    open(out, "w", encoding="utf-8").write("\n".join(md) + "\n")
    print(f"kit_verify: PostgreSQL {report.get('version')}; {len(rows)} keys; {ok} match; {len(rows) - ok} differ")
    sys.exit(0 if ok == len(rows) else 1)


if __name__ == "__main__":
    main()
