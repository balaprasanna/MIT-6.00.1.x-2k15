 #L3 Problem 5a (2/2 points)

#In this problem you'll be given a chance to practice writing some for loops.

#1. Convert the following code into code that uses a for loop.

print 2
print 4
print 6
print 8
print 10
print "Goodbye!"

1

for num in range(2,12,2):

#2

    print num

#3

print('Goodbye!')

#correct

#correct


# There are many ways to solve this problem! Here is one:
for count in range(11):
    if count != 0 and count % 2 == 0:
        print count
print "Goodbye!"

# Here is another:
for count in range(2, 12, 2):
    print count
print "Goodbye!"

#Test results
#CORRECT
#See full output
#See full output
#L3 Problem 5b (2/2 points)

#2. Convert the following code into code that uses a for loop.

print "Hello!"
print 10
print 8
print 6
print 4
print 2

#1

print('Hello!')

#2

for count in range(10,0,-2):

#3

    print count

correct

correct


# There are always many ways to solve a programming problem. Here is one:
print "Hello!"
for num in range(0, 10, 2):
    print 10 - num

# Here is another:
print "Hello!"
for num in range(10, 0, -2):
    print num

#Test results
#CORRECT
#See full output
#See full output
#L3 Problem 5c (3/3 points)

#3. Write a for loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:

#21

#which is 1 + 2 + 3 + 4 + 5 + 6.


total = 0

2

for count in range(abs(end)+1):

#3

    total += count

#4

print(str(total))

#correct

#correct
#Test results