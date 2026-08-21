  #01234567890123 (+)positive index 
s="abcd efgh ijkl"

print(s[2:13])
#cd efgh ijk

print(s[3:10])
#d efgj

print(s[4:9:2])
# efgh
#fh

print(s[1:12:2])
#bcd efgh ij
#bdeg j

print(s[1:11:3])
#bcd efgh i
#b g i

print(s[1:13:4])
#bcd efgh ijk
# be       

s="abcd efgh ijkl"
 # 43210987654321  (-) nagtive index

print(s[-12:-2])
#cd efgh ij

print(s[-14:-5])
#abcd efgh 

print(s[-11:-4])
#d efgh

print(s[-13:-3])
#bcd efgh i

print(s[-12:-6:4])
#cd efg
#cf

print(s[-12:-2:2])
#cd efgh ij
#cfhj


print(s[-13:-3:2])
#bcd efgh i
#bdeg

print(s[::-2])
# abcd efgh ijkl
#ljgedb




print(s[::2])
# abcd efgh ijkl
#ljgedb


print(s[::-3])
#abcd efgh ijkl
#ligb

print(s[-11:-3:4])
#d efgh i
#dg



print(s[-12:-4:5])
#cd efgh i
#cg      

s="abcd efgh ijkl"
#  43210987654321

print(s[:-4:-5])
#aei      
      
