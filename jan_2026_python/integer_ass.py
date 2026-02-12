# question 1 : sum of first 5 even num 
num = [2,4,6,8,10]
total=0
for i in num:
   total = total + i
print(total)

#question 1 calculaye the product of first 10 natural num 
num= [1,2,3,4,5,6,7,8,9,10] 
product = 1 
for i in num:
   product = product * i 
print (product)


#question 2 find the remainder when 156 divided by 7 
a=7
b=156
c= b%a
print(c)

#question 3 cal the square of 25 
a=25 
c= a** 2 
print ("square of a num is :", c)

#question 4 calculate the cube root of 125 
num = 125 
b= num**3
print ("the cube root of a num is :",b )

#question 5 cal sum of digits of a number 12345
num = "12345"
sum =0 
for i in num :
   sum= sum +int (i) 
print(sum)

#question 6 check 97 is a prime 
num =97 
for i in range (2,num):
   if num % i==0 :
      print("its not a prime num ")
else:
    print ("prime number")

#question 7 Find the factorial of 8
fact=1
for i in range (1,9):
   fact= fact*i
print(fact)

#question 8 Calculate the average of numbers: 15, 23, 31, 42, 56"
a= [15,23,31,42,56]
b= len(a)
sum=0
for i in a :
   sum=sum+i
avg= sum/b
print(avg)

# que 9 Find the greatest common divisor (GCD) of 48 and 36
a=48
b=36
gcd=1
for i in range (1,min(a,b)+1):
   if a%i==0 and b%i==0:
      gcd= i
print(gcd)
#que 10 Calculate the sum of first 20 odd numbers
total=0
for i in range (1,41):
   if i % 2 !=0:

    total = total+i 
print (total)
     
   