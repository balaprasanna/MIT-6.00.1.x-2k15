#temp = 120
#if temp > 85:
#   print "Hot"
#elif temp > 100:
#   print "REALLY HOT!"
#elif temp > 60:
#   print "Comfortable" 
#else:
#   print "Cold"


#temp = '32'
#if temp > 85:
#   print "Hot"
#elif temp > 62:
#   print "Comfortable" 
#else:
#   print "Cold" 



#temp = 50
#if temp > 85:
#   print "Hot"
#elif temp > 100:
#   print "REALLY HOT!"
#elif temp > 60:
#   print "Comfortable"
#else:
#   print "Cold"
# 


school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1

print 'numVowels is: ' + str(numVowels)
print 'numCons is: ' + str(numCons)