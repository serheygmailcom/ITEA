
# 1!

l=[x for x in range(100) if x%2==0]

print(l)

# 2!

capitals={
    'UA':"Kiev",
    'FR':"Paris",
    'IT':"Rome"}

countries=["UA", "FR", "RO"]

res=[capitals.get(x) for x in countries if x in capitals]

print(res)

#3!

res=["FizzBuzz" if x == 15  else
    ("Fizz" if x % 3 == 0 else
    ("Buzz" if x % 5 == 0 else x)) for x in range(1,101)]

print(res)

#4

def bank(sum, years, pc):
    res=sum*(1+pc/100)**years
    return "After {0:.1f} years your deposit sum would become {1:.2f}".format(years, res)

print(bank(100,30,13))
