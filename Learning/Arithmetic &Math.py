import math
friends = 0
#friends = friends + 5

friends += 5
#friends = friends -3
friends = friends - 3

#friends = friends * 5
friends *= 10

friends = friends / 2
friends /= 2

# ** is = ^
#friends = friends**2
friends **=2

# % is a reminader
# // divides without decimals
half_friends = friends/2 
remainder = friends % 2


print(friends)
print(remainder)
print(half_friends)

#round()is a  bulit in round fouction
x = 3.14
y = 4
z = -5

#abs = abouslute from 0 as whole number

rounded = round(z)
print(rounded)

z /= 2
d = abs(z)
print(d)

# pow(4,3) = 4^3

result = pow(d, 3)
print(result)

# max(1,2,3) = maxuimum between (1,2,3) = 3
# min does the oppsite 

q = max(z, result, y)
print(q)

#pi 
#e
print(math.pi)
print(math.e)

#sqrt 
l = 9
poop = math.sqrt(l)
print(poop)

# ceil will always round a flooting point number up
#floor  will always round a number down

m =9.1
n =9.9

print(math.ceil(m))
print(math.floor(n))