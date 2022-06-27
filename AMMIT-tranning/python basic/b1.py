'''
map() --->
The map() function executes a specified function
 for each item in an iterable. The item is sent to the function as a parameter.


map(fun, iter) -->

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.


The split() method splits a string into a list.

we can specify the separator, default separator is any whitespace.
EX 

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)
'''

a,b = map(int, input("enter two no.").split(" "))
print(a)
print(b)