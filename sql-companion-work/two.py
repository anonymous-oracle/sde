import subprocess, os, select, time, sys
ENV = dict(os.environ, PGHOST="localhost", PGPORT="54329", PGUSER="lab", PGDATABASE="labdb")
class S:
    def __init__(self, name):
        self.name=name
        self.p=subprocess.Popen(["psql","-X","-At","-q"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=ENV,text=True,bufsize=0)
        self.buf=""
    def run(self, sql, wait=1.0):
        tok=f"__END{time.time_ns()}__"
        self.p.stdin.write(sql.strip()+"\n\\echo "+tok+"\n"); self.p.stdin.flush()
        out=""; t0=time.time()
        while time.time()-t0<wait:
            r,_,_=select.select([self.p.stdout],[],[],0.1)
            if r:
                ch=self.p.stdout.readline()
                if not ch: break
                if tok in ch:
                    return out.strip(), False
                out+=ch
        return out.strip(), True   # True => still blocked
    def drain(self, wait=1.0):
        out=""; t0=time.time()
        while time.time()-t0<wait:
            r,_,_=select.select([self.p.stdout],[],[],0.1)
            if r:
                ch=self.p.stdout.readline()
                if not ch: break
                out+=ch
        return out.strip()
    def close(self):
        try: self.p.stdin.write("\\q\n"); self.p.stdin.flush()
        except Exception: pass
        self.p.wait(timeout=5)
def step(s, sql, wait=1.0):
    out, blocked = s.run(sql, wait)
    print(f"[{s.name}] {sql.strip().splitlines()[0][:90]}" + ("  ... " if len(sql.strip().splitlines())>1 else ""))
    print(f"      -> {'(BLOCKED)' if blocked else out or 'ok'}" if blocked or out else "      -> ok")
    return out, blocked
