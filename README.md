#python tets

#Python Notes and summery about Functional programming, Lambdas, map() function, filter(), generator
[200~Functional programming in python
 
Functional programming is a general concept which states that the code should be contained in functions. Functional programming allows us to reuse the code as many number of times we want. It not only makes the code efficient but also maintainable. Functional programming can be implemented by the use of functions in our code.
 
 
 Lambdas in Python
 
The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name. These functions are throw-away functions, i.e. they are just needed where they have been created. Lambda functions are mainly used in combination with the functions filter(), map() and reduce().


The general syntax of a lambda function is quite simple:
lambda argument_list: expression


The argument list consists of a comma separated list of arguments and the expression is an arithmetic expression using these arguments. You can assign the function to a variable to give it a name.


The following example of a lambda function returns the sum of its two arguments:

>>> f = lambda x, y : x + y
>>> f(1,1)
2


The map() Function:

The advantage of the lambda operator can be seen when it is used in combination with the map() function.
map() is a function with two arguments:

r = map(func, seq)

The first argument func is the name of a function and the second a sequence (e.g. a list) seq. map() applies the function func to all the elements of the sequence seq. It returns a new list with the elements changed by func


Filtering:
The function filter(function, list) offers an elegant way to filter out all the elements of a list, for which the function function returns True.The function filter(f,l) needs a function f as its first argument. f returns a Boolean value, i.e. either True or False. This function will be applied to every element of the list l. Only if f returns True will the element of the list be included in the result list.


Example:
>>> fib = [0,1,1,2,3,5,8,13,21,34,55]
>>> result = filter(lambda x: x % 2, fib)
>>> print (list(result))
[1, 1, 3, 5, 13, 21, 55]
>>> result = filter(lambda x: x % 2 == 0, fib)
>>> print (list(result))
[0, 2, 8, 34]
>>>


Generators:
Generators are a special kind of function, which enable us to implement or generate iterators.Iterators are a fundamental concept of Python.Mostly, iterators are implicitly used, like in the for loop of Python.A generator is a function that produces a sequence of results instead of a single value. Generators are a simple and powerful possibility to create or to generate iterators. These iterators are called generator objects. On the surface they look like functions, but there is both a syntactic and a semantic difference. Instead of return statements you will find inside of the body of a generator only yield statements, i.e. one or more yield statements.

Python oops 
#Python oops Inheritance 
