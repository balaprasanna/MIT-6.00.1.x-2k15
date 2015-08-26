
Note: Using the 'range' built-in function

The standard way of using the range function is to give it a number to stop at, and range will give a list of values that start at 0 and go through the stop value minus 1. For example, calling range(stop) yields the following:

>>> range(5)
[0, 1, 2, 3, 4]

However, we can call range with some additional, optional parameters - a value to start at, and a step size. You can specify a start value by calling range(start, stop), like this:

>>> range(2, 5)
[2, 3, 4]

To specify a step size, you must specify a start value - the call is range(start, stop, stepSize), like this:

>>> range(2, 10, 2)
[2, 4, 6, 8]

Note that these parameters - start, stop, stepSize - are the same parameters that you can use when slicing a string:

>>> s = "Hello, world!"
>>> s[1:] # s[start:]
ello, world!
>>> s[1:10] # s[start:stop]
ello, wor
>>> s[1:10:3] # s[start:stop:stepSize]
eow

In this problem you'll get more practice on using range. You can also see more examples of 'range' here.
:wq

