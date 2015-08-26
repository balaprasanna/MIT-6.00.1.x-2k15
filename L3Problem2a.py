# L3 Problem 2a 

#In this problem you'll be given a chance to practice writing some while loops.
#
#1. Convert the following into code that uses a while loop.
#
#print 2
#print 4
#print 6
#print 8
#print 10
#print Goodbye!


# My approach 
var = 0;
while (var < 10):
    var += 2;
    print(str(var))
print('Goodbye!')


# Solution
#----------------
# There are many ways to solve this problem! Here is one:
num = 2
while num < 11:
    print num
    num += 2
print "Goodbye!"

# Here is another:
num = 2
while num <= 10:
    print num
    num += 2
print "Goodbye!"

# And another:
num = 0
while True:
    num += 2
    print num
    if num >= 10:
        print "Goodbye!" 
        break

# And one more:
num = 1
while num <= 10:
    if num % 2 == 0:
        print num
    num += 1
print "Goodbye!"

# There are always many, many different ways to solve a programming
# problem. Here are just four examples and surely there are quite
# a few more.






#2. Convert the following into code that uses a while loop.
#
#print Hello!
#print 10
#print 8
#print 6
#print 4
#print 2

#My Approach

print('Hello!')
var = 10;
while (var > 0):
    print(str(var))
    var -= 2;

#SOLUTION
#-------------------------
# There are always many ways to solve a programming problem. Here is one:
print "Hello!"
num = 10
while num > 0:
    print num
    num -= 2

# Here is another:
num = 11
print "Hello!"
while num > 1:
    num -= 1
    if num %2 == 0:
        print num
        
#3. Write a while loop that sums the values 1 through end, inclusive.
#end is a variable that we define for you. So, for example, 
#if we define end to be 6, your code should print out the result:


#My Approach
total = 0
while (end > 0):
    total += end
    end -= 1
print(str(total))


#SOLUTION
# Here is one of a few ways to solve this problem:
total = 0
current = 1
while current <= end:
    total += current
    current += 1

print total
