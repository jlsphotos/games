import random
import time


# print("Spining Wheel")
# time.sleep(random.randint(1,3))
reds = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
blacks = (2, 4, 6, 8, 10, 11,13, 15, 17, 20, 22, 24,26, 28, 29, 31, 33, 35)


def spin_the_wheel():
    spin = random.randint(0,36)
    return spin


def check_colour(n):
    if n in reds:
        return "Red"
    elif n in blacks:
        return "Black"
    else:
        return "Green"


def check_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


def check_dozen(n):
    if n in range(1,12):
        return "1st Dozen"
    elif n in range(13,24):
        return "2nd Dozen"
    elif n in range(25,36):
        return "3rd Dozen"
    else:
        return "zero"
def high_low(n):
    if n > 18:
        return "High"
    else:
        return "Low"

result = spin_the_wheel()
colour = check_colour(result)
oddness = check_odd(result)
dozen = check_dozen(result)
highlow = high_low(result)




print("The result is %s %s. \nThe number is %s.\nis the %s\nAnd is %s " % (result, colour, oddness,dozen,highlow))
res = []

'''
f = open('results.txt','w')

start = time.time()
for i in range(200000):
    r = spin_the_wheel()
    res.append(r)
f.write('%s\n' % (res))
f.close()
length = time.time() - start
print(" time taken %s" % (length) )
'''
black = 0
red = 0
green = 0
f = open('results.txt', 'r')
nums = f.read().split(',')

for res in nums:
    res = int(res)
    col = check_colour(res)

    if col == 'Black':
        black = black + 1
    elif col == 'Red':
        red += 1
    else:
        green += 1

f.close()

print(black)
print(red)
print(green)





