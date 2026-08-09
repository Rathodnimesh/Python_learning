s=input("Enter your string:")

al=0
nm=0
sp=0

for i in s:
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
         nm=nm+1
    elif i.isspace():
         sp=sp+1


##upper
##lower
##spacial 




print("Totla Alphabets:",al)
print("Total numerics:",nm)
print("Total spaces:",sp)










         
