import subprocess, sys, json, importlib, os
ENV = dict(os.environ, PGHOST="localhost", PGPORT="54329", PGUSER="lab", PGDATABASE="labdb")

def psql(script):
    p = subprocess.run(["psql", "-At", "-v", "ON_ERROR_STOP=1", "-q", "-X"], input=script, capture_output=True, text=True, env=ENV)
    return p.returncode, p.stdout, p.stderr

def run(e):
    probe = e.get("probe", e["key"]).rstrip().rstrip(";")
    fn = "chk_o" if e["ordered"] else "chk"
    setup = e.get("setup", "")
    stmts = e.get("stmts", "")
    show_order = "" if e["ordered"] else " ORDER BY t::text"
    script = f"""BEGIN;
SET LOCAL search_path = public;
{setup}
{stmts}
CREATE TEMP TABLE _p AS {probe};
SELECT 'G|' || lab.{fn}('SELECT * FROM _p');
SELECT 'R|' || t::text FROM _p t{show_order} LIMIT 16;
ROLLBACK;
"""
    rc, out, err = psql(script)
    if rc != 0:
        return None, [], err.strip()
    g = None; rows = []
    for line in out.splitlines():
        if line.startswith("G|"): g = line[2:]
        elif line.startswith("R|"): rows.append(line[2:])
    return g, rows, ""

if __name__ == "__main__":
    mods = sys.argv[1].split(",")
    only = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else None
    res = {}
    for m in mods:
        mod = importlib.import_module(m)
        for e in mod.EX:
            if only and e["id"] not in only: continue
            g, rows, err = run(e)
            res[e["id"]] = {"golden": g, "rows": rows, "err": err}
            print(e["id"], g, ("ERR: " + err[:300]) if err else "")
    json.dump(res, open("goldens_" + "_".join(mods) + ".json", "w"), indent=1)
