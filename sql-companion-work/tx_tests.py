from two import *
import subprocess
def sql(x):
    return subprocess.run(["psql","-X","-At","-q","-c",x],capture_output=True,text=True,env=ENV).stdout.strip()
sql("DROP SCHEMA IF EXISTS tx CASCADE; CREATE SCHEMA tx;")
def fresh(ddl):
    sql("DROP SCHEMA IF EXISTS tx CASCADE; CREATE SCHEMA tx;"); 
    for d in ddl.split(";;"): 
        if d.strip(): sql(d)

def scenario(title): print("\n=== "+title)

scenario("T1 lost update READ COMMITTED (app-side read-modify-write)")
fresh("CREATE TABLE tx.acct(id int primary key, bal int); ;; INSERT INTO tx.acct VALUES (1,100)")
a,b=S("S1"),S("S2")
step(a,"BEGIN; SELECT bal FROM tx.acct WHERE id=1;")
step(b,"BEGIN; SELECT bal FROM tx.acct WHERE id=1;")
step(a,"UPDATE tx.acct SET bal=130 WHERE id=1; COMMIT;")
step(b,"UPDATE tx.acct SET bal=80 WHERE id=1; COMMIT;")
print("final:",sql("SELECT bal FROM tx.acct WHERE id=1")); a.close(); b.close()

scenario("T1b atomic UPDATE fixes it")
fresh("CREATE TABLE tx.acct(id int primary key, bal int); ;; INSERT INTO tx.acct VALUES (1,100)")
a,b=S("S1"),S("S2")
step(a,"BEGIN; UPDATE tx.acct SET bal=bal+30 WHERE id=1;")
step(b,"BEGIN; UPDATE tx.acct SET bal=bal-20 WHERE id=1;")   # blocks
step(a,"COMMIT;")
print("S2 after S1 commit:",b.drain())
step(b,"COMMIT;")
print("final:",sql("SELECT bal FROM tx.acct WHERE id=1")); a.close(); b.close()

scenario("T1c REPEATABLE READ: second writer aborts")
fresh("CREATE TABLE tx.acct(id int primary key, bal int); ;; INSERT INTO tx.acct VALUES (1,100)")
a,b=S("S1"),S("S2")
step(a,"BEGIN ISOLATION LEVEL REPEATABLE READ; SELECT bal FROM tx.acct WHERE id=1;")
step(b,"BEGIN ISOLATION LEVEL REPEATABLE READ; SELECT bal FROM tx.acct WHERE id=1;")
step(a,"UPDATE tx.acct SET bal=130 WHERE id=1; COMMIT;")
step(b,"UPDATE tx.acct SET bal=80 WHERE id=1;")
step(b,"ROLLBACK;")
print("final:",sql("SELECT bal FROM tx.acct WHERE id=1")); a.close(); b.close()

scenario("T2 non-repeatable read: RC vs RR")
for lvl in ["READ COMMITTED","REPEATABLE READ"]:
    fresh("CREATE TABLE tx.acct(id int primary key, bal int); ;; INSERT INTO tx.acct VALUES (1,100)")
    a,b=S("S1"),S("S2"); print("--",lvl)
    step(a,f"BEGIN ISOLATION LEVEL {lvl}; SELECT bal FROM tx.acct WHERE id=1;")
    step(b,"UPDATE tx.acct SET bal=999 WHERE id=1;")
    step(a,"SELECT bal FROM tx.acct WHERE id=1; COMMIT;")
    a.close(); b.close()

scenario("T3 write skew (on-call): RR vs SERIALIZABLE")
for lvl in ["REPEATABLE READ","SERIALIZABLE"]:
    fresh("CREATE TABLE tx.oncall(doc int primary key, on_call boolean not null); ;; INSERT INTO tx.oncall VALUES (1,true),(2,true)")
    a,b=S("S1"),S("S2"); print("--",lvl)
    step(a,f"BEGIN ISOLATION LEVEL {lvl}; SELECT count(*) FROM tx.oncall WHERE on_call;")
    step(b,f"BEGIN ISOLATION LEVEL {lvl}; SELECT count(*) FROM tx.oncall WHERE on_call;")
    step(a,"UPDATE tx.oncall SET on_call=false WHERE doc=1;")
    step(b,"UPDATE tx.oncall SET on_call=false WHERE doc=2;")
    step(a,"COMMIT;")
    step(b,"COMMIT;")
    print("on call now:",sql("SELECT count(*) FROM tx.oncall WHERE on_call")); a.close(); b.close()

scenario("T3b phantom: RC vs RR (insert visible?)")
for lvl in ["READ COMMITTED","REPEATABLE READ"]:
    fresh("CREATE TABLE tx.t(id int primary key); ;; INSERT INTO tx.t VALUES (1),(2)")
    a,b=S("S1"),S("S2"); print("--",lvl)
    step(a,f"BEGIN ISOLATION LEVEL {lvl}; SELECT count(*) FROM tx.t;")
    step(b,"INSERT INTO tx.t VALUES (3);")
    step(a,"SELECT count(*) FROM tx.t; COMMIT;")
    a.close(); b.close()

scenario("T4 deadlock")
fresh("CREATE TABLE tx.acct(id int primary key, bal int); ;; INSERT INTO tx.acct VALUES (1,100),(2,100)")
a,b=S("S1"),S("S2")
step(a,"BEGIN; UPDATE tx.acct SET bal=bal-10 WHERE id=1;")
step(b,"BEGIN; UPDATE tx.acct SET bal=bal-10 WHERE id=2;")
step(a,"UPDATE tx.acct SET bal=bal+10 WHERE id=2;", wait=0.5)
step(b,"UPDATE tx.acct SET bal=bal+10 WHERE id=1;", wait=2.5)
print("S1 says:",a.drain(2.0))
a.run("ROLLBACK;",0.5); b.run("ROLLBACK;",0.5); a.close(); b.close()

scenario("T5 SKIP LOCKED queue")
fresh("CREATE TABLE tx.job(id int primary key, state text not null default 'new'); ;; INSERT INTO tx.job SELECT g FROM generate_series(1,6) g")
a,b=S("W1"),S("W2")
step(a,"BEGIN; SELECT id FROM tx.job WHERE state='new' ORDER BY id LIMIT 2 FOR UPDATE SKIP LOCKED;")
step(b,"BEGIN; SELECT id FROM tx.job WHERE state='new' ORDER BY id LIMIT 2 FOR UPDATE SKIP LOCKED;")
step(b,"BEGIN; SELECT id FROM tx.job WHERE state='new' ORDER BY id LIMIT 2 FOR UPDATE;",wait=1)
a.run("ROLLBACK;",0.5); b.run("ROLLBACK;",0.5); a.close(); b.close()

scenario("T6 SELECT FOR UPDATE fixes lost update")
fresh("CREATE TABLE tx.acct(id int primary key, bal int); ;; INSERT INTO tx.acct VALUES (1,100)")
a,b=S("S1"),S("S2")
step(a,"BEGIN; SELECT bal FROM tx.acct WHERE id=1 FOR UPDATE;")
step(b,"BEGIN; SELECT bal FROM tx.acct WHERE id=1 FOR UPDATE;")
step(a,"UPDATE tx.acct SET bal=130 WHERE id=1; COMMIT;")
print("S2 unblocked:",b.drain(1.0))
step(b,"UPDATE tx.acct SET bal=110-20 WHERE id=1; COMMIT;")
print("final:",sql("SELECT bal FROM tx.acct WHERE id=1")); a.close(); b.close()
sql("DROP SCHEMA IF EXISTS tx CASCADE")
