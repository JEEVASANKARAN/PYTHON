sum=lambda x,y :x+y
print("Sum of 5 and 3 is :" , sum(5,3))
square=lambda x:x*x
print("Square of 6 is :",square(6))
numbers=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda x:x%2==0,numbers))
print("Even numbers are :",even)
squares =list(map(lambda x:x*x,numbers))
print("square of numbers :",squares)
