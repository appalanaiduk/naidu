'''
Arm strong number

if the sum of nth powder of each digit equals to the number itself.

example=153,351,1634
'''
'''
#1 armstrong number
num=input('enter number:')
sum=0
for i in num:
   sum=sum+int(i)**3
if sum==int(num):
   print(num,'is armstrong number')
else:
   print(num,'is not a armstrong')
'''
'''
#2 palidrome-1
a="radar"
b=""
for i in a:
    b=i+b
if a==b:
    print(a,"is a palidrome")
else:
    print(a,"is not palidrome")

'''
'''
#palindrome-2
a="means"
print(a[::-1])
'''
'''
#3fibonic series
n1=1
n2=2
new=0
while new<55:
     print(new,end=" ")
     new=n1+n2
     n1=n2
     n2=new
'''

'''
#4 even or odd
num=[2,3,4,5,7,10]
for i in num:
    if i%2==0:
        print(i,"even number")
    else:
        print(i,"not even")
'''
'''
#5 prime number
num=10
for i in range (2,num):
  if num % i == 0:
    print(num,"is not prime")
    break
else:
  print(num,"is prime")
'''
#6 Find the Factorial of the Number using Recursion

def fac(n):
    if n == 0:
        return 1
    return n*fac(n - 1)
n=5
a=fac(n)
print(a)







































