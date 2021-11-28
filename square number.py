#with generator
def create_squares_gen(n):
    for x in range(n):
        yield x**2
mynum=create_squares_gen(10)
print(mynum)
print(next(mynum)) #0
print(next(mynum)) #1
#print(next(mynum)) #4
for result in create_squares_gen(10):
    print(result)