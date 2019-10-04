#Assignment Questions

#Q1 Swap two variables without using 3rd variable.

a=20
b=50
'''
print("value of a: ",a," value of b: ",b)
a,b = b,a
print("value of a: ",a," value of b: ",b)
'''
      #******************
'''
print("value of a: ",a," value of b: ",b)
a=a+b
b=a-b
a=a-b
print("value of a: ",a,"value of b: ",b)
'''
      #******************
#Q2 Accept marks from user and print the corresponding grade
'''
m1=int(input("Enter grade: "))

if m1>= 75:
      print("Grade A")
elif m1>= 55:
      print("Grade B")
elif m1>= 35:
      print("Grade C")
else:
      print("Phir Milenge!")
'''
#Q3 accept a number from user - if it is divisible by 3, print "Three",
#   if it is divisble by 7 print "seven" and if divisble by both, then print
#   "Three - Seven"
'''
m1=int(input("Enter a number: "))

if (m1%3 ==0 and m1%7 ==0):
      print("Three - Seven")
elif m1%3 ==0:
      print("Three")
elif m1%7 ==0:
      print("Seven")
else:
      print("Not divisble by 3 Or 7")
'''
#Q4 Accept a number from the user and check if it is odd or even number( % operator)
'''
m1=int(input("Enter a number: "))

if m1%2==0:
      print(m1,"Is Even")
else:
      print(m1,"Is Odd")
'''

#Q5 Accept a number from the user check if it is odd or even number(do not use % operator)
'''
m1=int(input("Enter a number: "))

if m1/2 == m1//2:
      print(m1," is even")
else:
      print(m1," is odd")
'''
#Q6 Accept principal amount, rate and years of investment then find the simple interest.
'''
p = int(input("Enter Principal amount: "))
n = int(input("Enter No of years: "))
r = int(input("Enter rate of Interest: "))

si = (p*n*r)/100

print("Simple Interest is: ",si)
'''
#Q7 Rectangle wala problem

#Q8 Accept 10 numbers from user and calculate their sum(Do not use array)
'''
sum= 0
for i in range(10) :
      m1 = int(input("Enter number: "))
      sum += m1
print("Sum is ", sum)
'''

#Q9 Accept a number from user and find the factorial of the number
'''
product =1
m1= int(input("Enter a number: "))
m2 = m1
while m1 >1:
      digit = m1%10
      product *= digit
      m1 -=1
print("Factorial of",m2," is ",product)

#logic v2
n = int(input("enter element: "))
fact =1
for i in range (n,1,-1):
      fact*=i
print("factorial of ",n,"is ",fact)

'''
#Q10 Accept 10 numbers from the user & count how many of the digits are positive, negative or zero
'''
l =[]
p=0
n=0
z=0
for i in range(10):
      m1 = int(input("Enter a number: "))
      if m1>0:
            p+=1
      elif m1<0:
            n+=1
      else:
            z+=1
      l.append(m1)
print("List: ",l,"\n")
print("Positive =",p,"Negative =",n,"Zero =",z)
'''
#Q11 Accept a number from user and calculate the sum of digits of the number
'''
sum = 0
m1 = int(input("Enter a number: "))
m2 = m1

while m1!=0:
      digit = m1%10
      sum += digit
      m1 = m1//10
print("Sum of digits of ",m2," is",sum)

'''

#Q12 Accept a number from the user and reverse it.
#    Accept a number from the user and check if it is palindrome number or not.
'''
m1 = int(input("Enter a number: "))
m2 = m1
number = 0
while m1!=0:
      digit = m1%10
      number = number*10 + digit
      m1 = m1//10

print("Reverse of ",m2,"is ",number)

if number == m2:
      print(m2," is a palindrome")
else:
      print(m2," is not a palindrome")
'''
#Q13 Accept a number from the user and print a table for that number
'''
m1 = int(input("Enter a number: "))
for i in range(1,11):
      print(m1,"x",i,"=",m1*i)

'''
#Q14 accept a number from user and check if it is a special number or not?
'''
m1 = int(input("Enter a number: "))
m2 = m1
sum = 0
while m1!=0:
      fact =1
      digit =m1%10
      for i in range(digit,1,-1):
            fact*=i
      sum = sum + fact
      m1 = m1//10
if m2 == sum:
      print(m2," Is a special number")
else:
      print(m2," Is not a special number")
'''

#Q15 Accept a number from user and check if its an Armstrong number or not?
'''
m1 = int(input("Enter a number: "))
m2 = m3 = m1
sum = 0
count = 0
number = 0
while m1!=0:
      digit = m1%10
      count +=1
      m1= m1//10
digit = 0
while m2!=0:
      digit = m2%10
      number = number + digit**count
      m2 = m2//10
if number == m3:
      print(m3,"is an armstrong")
else:
      print(m3,"is not an armstrong")
'''

#Q16Go on accepting number from the user until user enters 0 and calculate the sum of these numbers
'''
l = []
sum = 0
while True:
      m1 = int(input("Enter number: "))
      if m1 == 0:
            break
      l.append(m1)
      sum += m1
print("Sum is", sum)
      
'''

#Q17 Accept a number from the user and print next 5 numbers
'''
m1 = int(input("Enter a number"))
for i in range(m1,m1+m1):
      print(i)
'''

