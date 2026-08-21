def simple_genrator():
    yield 1
    yield 2
    yield 3
           
gen=simple_genrator()


print(next(gen))
print(next(gen))
print(next(gen))

