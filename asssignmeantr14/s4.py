n=[1,2,3,4,5,6,7,8,9]
t=9
s=set()
p=set()
for i in n:
    b=t-i
    if b in s:
        p.add(tuple(sorted(i,b)))
    s.add(i)
print(f"pairs:{t}:",list(p))