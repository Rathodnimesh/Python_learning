l=[1,2,3,10,20,"Tops","True","python","false",100,200,300,"java",10,20,1,2,3]
#  0 1 2 3  4    5      6       7        8     9   0   1    2    3  4  5 6 7


print(l[:10:10])
#1

print(l[3::15])
#10




print(l[::7])
#1,"python",20



print(l[7:8:9])
#"python"

print(l[2:5])
#3,10,20

l=[1,2,3,10,20,"Tops","True","python","false",100,200,300,"java",10,20,1,2,3]
#  8 7 6 5  4    3      2        1        0    9    8  7     6    5 4  3 2 1

print(l[:-15:12])
# 1

print(l[:-11:2])
#1,3,20,"True"

print(l[:-15:2])
#3,1

print(l[-5::5])
#10

print(l[-15:-10:5])
#10

print(l[-9::-5])
#100,20

print(l[:-14:2]) # 1 3
# last ma 2 hoy to left side

print(l[:-14:-2])
#-2 hoy to right  side the saru thye

l=[1,2,3,10,20,"Tops","True","python","false",100,200,300,"java",10,20,1,2,3]
#  8 7 6 5  4    3      2        1        0    9    8  7     6    5 4  3 2 1

print(l[-14:-2])
