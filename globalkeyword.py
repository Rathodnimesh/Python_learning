print("---global----")
def myfun():
    global name
    print("1st",name)
    name="python language"
    print("2nd",name)
    name="Django"

name="python"
myfun()
print("3rd",name)


print("---local---")
def myfun1():
    print("name:",name)

name="python"
myfun1()



print("---global without keyword")

def myfun2():
    name="python language"
    print("Name:",name)

name="python"
print("Name:",name)
myfun2()







