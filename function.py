newlist = [ 2, 4, 5, 5, 8, 9, 7]
#newlist = input("enter a list for map function")
#newlist = newlist.split()
#print(newlist)
result = list(map(lambda x : x*2,newlist))
print(f'Map function working: {result}')

newlist= [1,2,3,4,5,6,7,8,9]
#newlist = input("Enter a list for filter function")
#newlist = newlist.split()
#print(newlist)
result = list(filter(lambda x : x%2==0, newlist))
print(f'Filter dunction is working: {result}')

def fectorial(x):
    if x == 1:
        return 1
    else:
        return x*(fectorial(x-1))
x = int(input("Enter a number for fectorial: "))
result = fectorial(x)
print(f'Recursion is working: {result}')
