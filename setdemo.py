s1={1,2,3,4,5}
s2={1,3,5,6,7,8}

print(s1)
print(s2)

s1.add(101)
print(s1)



print(s1.difference(s2))
s1.discard(101)

print(s1)
print(s1.intersection(s2))

s1.pop()
print(s1)


s1.remove(3)
print(s1)


print(s1.union(s2))

s3={10,20,30}
s1.update(s3)
print(s1)


for i in s1:
    print(i)

print(list(s1))
l1=[10,20,30,40,50,10,20]
s4=set(l1)
print(s4)
print(list(s4))

