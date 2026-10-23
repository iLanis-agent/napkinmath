import json, random
def dec(n, p=2):
    b = 10**p
    w, f = divmod(n, b)
    fs = str(f).zfill(p).rstrip("0")
    return str(w) + "." + fs if fs else str(w)
def m(n): return f"{n//100}.{str(n%100).zfill(2)}"
def pl(n, one, many): return f"{n}" + (one if n == 1 else many)
def v(n, one, many): return one if n == 1 else many
def packs(n, b):
    k = -(-n//b)
    return f"The {pl(n,' napkin',' napkins')} at {pl(b,' napkin',' napkins')} a pack {v(n,'takes','take')} {pl(k,' pack',' packs')}, the last pack holding {pl(n-(k-1)*b,' napkin',' napkins')}."
def weeks(n, w):
    k = n//w
    return f"The {pl(n,' napkin',' napkins')} at {pl(w,' napkin',' napkins')} a week {v(n,'lasts','last')} {pl(k,' full week',' full weeks')} with {pl(n-k*w,' napkin',' napkins')} left for the next week."
def cost(b, pc, n):
    cc = b*pc
    pb = (2*cc + n)//(2*n)
    return f"The {pl(b,' pack',' packs')} at ${m(pc)} a pack {v(b,'comes','come')} to ${m(cc)}, ${m(pb)} a napkin."
def time_(n, pm):
    t = -(-n//pm); h, r = t//60, t%60
    return f"The {pl(n,' napkin',' napkins')} at {pl(pm,' napkin',' napkins')} a minute {v(n,'takes','take')} {pl(t,' minute',' minutes')}, {pl(h,' hour',' hours')} {pl(r,' minute',' minutes')}."
random.seed(784)
R = random.randint
cases = [
 dict(fn="packs", args=["585","50"], expect=packs(585,50)),
 dict(fn="weeks", args=["585","80"], expect=weeks(585,80)),
 dict(fn="cost", args=["12","6.40","585"], expect=cost(12,640,585)),
 dict(fn="time", args=["585","12"], expect=time_(585,12)),
 dict(fn="packs", args=["1","1"], expect=packs(1,1)),
 dict(fn="packs", args=["550","50"], expect=packs(550,50)),
 dict(fn="packs", args=["1000000","1000"], expect=packs(1000000,1000)),
 dict(fn="weeks", args=["1","1"], expect=weeks(1,1)),
 dict(fn="weeks", args=["560","80"], expect=weeks(560,80)),
 dict(fn="weeks", args=["1000000","100000"], expect=weeks(1000000,100000)),
 dict(fn="cost", args=["1","0.01","1"], expect=cost(1,1,1)),
 dict(fn="cost", args=["100000","999.99","1000000"], expect=cost(100000,99999,1000000)),
 dict(fn="time", args=["1","1"], expect=time_(1,1)),
 dict(fn="time", args=["60","1"], expect=time_(60,1)),
 dict(fn="time", args=["1000000","100"], expect=time_(1000000,100)),
]
for _ in range(20):
    n,b=R(1,1000000),R(1,1000); cases.append(dict(fn="packs", args=[str(n),str(b)], expect=packs(n,b)))
for _ in range(20):
    n,w=R(1,1000000),R(1,100000); cases.append(dict(fn="weeks", args=[str(n),str(w)], expect=weeks(n,w)))
for _ in range(25):
    b,p,n=R(1,100000),R(1,99999),R(1,1000000); cases.append(dict(fn="cost", args=[str(b),dec(p),str(n)], expect=cost(b,p,n)))
for _ in range(19):
    n,m=R(1,1000000),R(1,100); cases.append(dict(fn="time", args=[str(n),str(m)], expect=time_(n,m)))
errs=[["packs",["0","50"]],["packs",["1000001","12"]],["packs",["2.5","12"]],["packs",["585","0"]],["packs",["585","1001"]],
 ["weeks",["0","30"]],["weeks",["585","0"]],["weeks",["585","100001"]],["weeks",["585","1.5"]],["weeks",["1000001","30"]],
 ["cost",["0","6.40","585"]],["cost",["100001","6.40","585"]],["cost",["12","0","585"]],["cost",["12","6.405","585"]],["cost",["12","6.40","0"]],
 ["time",["0","12"]],["time",["585","0"]],["time",["585","101"]],["time",["585","6.5"]],["time",["1000001","5"]]]
json.dump(dict(cases=cases, errors=errs), open("expected.json","w"), indent=1)
print(len(cases),"cases,",len(errs),"errcases")
