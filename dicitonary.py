d={101:"Disha",900:"Ajay",345:"Nimesh",567:"Smit",678:"Dhwanit"}



print(d)
print(d[567])


print(d.get(567))

print(d.items())

print(d.keys())

print(d.values())
print(d.pop(567))
print(d)

print(d.popitem())
print(d)


d1={567:"smit",678:"Dhawanit"}
d.update(d1)

print(d)


d[900]="jigar"
print(d)


for i in d:
      print(i," : ",d[i])    
