#-------------------------------------------------------
# Print out 'e' using indexing

s = 'hello'
print (s[1])
#-------------------------------------------------------
# Reverse the string using slicing
s ='hello'
print (s[::-1])

#-------------------------------------------------------
s ='hello'
# Print out the 'o'

# Method 1:
print (s[-1])

# Method 2:
print (s[4])


#-------------------------------------------------------
# Method 1:
x = [0,0,0]
print (x)

# Method 2:
x=list()
#-------------------------------------------------------
# Build list [0,0,0]
x.extend([0,0,0])

print (x)
#-------------------------------------------------------
list3 = [1,2,[3,4,'hello']]
list3[2][2]='goodbye'
print(list3)

#-------------------------------------------------------
list4 = [5,3,4,6,1]

# function for sorting the list
list4.sort()

# print the list after sorting
print(list4)
#-------------------------------------------------------

d = {'simple_key':'hello'}

# Grab 'hello'

#grab the word "hello"
d['simple_key']

#-------------------------------------------------------
d = {'k1':{'k2':'hello'}}

# Grab 'hello'

#grab the word "hello"
d['k1']['k2']


#-------------------------------------------------------
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello

#grab the word "hello"
d['k1'][0]['nest_key'][1][0]



d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

#Grab hello

#grab the word "hello"
d['k1'][2]['k2'][1]['tough'][2][0]



#-------------------------------------------------------
planet = "Earth"

diameter = 12742

print('The diameter of {} is {} kilometers'.format(planet,diameter))

#-------------------------------------------------------


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
#grab the word "hello"

lst[3][1][2][0]

#-------------------------------------------------------

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
#-------------------------------------------------------

#grab the word "hello"

d['k1'][3]['tricky'][3]['target'][3]

#-------------------------------------------------------
# swap two variables

# set two variables x,y
x = 1
y = 2

# Swap two variables by using third variable
temp = x
x = y
y = temp

# print two variables after swap
print("x = ", x)
print("y = ", y)
#-------------------------------------------------------