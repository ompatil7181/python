# # perii = 2*(l+b)
# l = int(input("value of l of reactangle: "))
# b = int(input("value of b of reactangle: "))
# peri = 2*(l+b)
# print("perii of rectangle",peri)

# # area = 0.5*w*h
# h = int(input("value of h of traingle: "))
# w = int(input("value of w of traingle: "))
# area = 0.5*h*w 
# print("area of triangle ",area)

# # peri = x+y+z
# x = int(input("value of x of traingle: "))
# y = int(input("value of y of traingle: "))
# z = int(input("value of z of traingle: "))
# peri = x+y+z 
# print("peri of triangle",peri)


# a = int(input("8 values for avr: "))
# b = int(input("8 values for avr: "))
# c = int(input("8 values for avr: "))
# d = int(input("8 values for avr: "))
# e = int(input("8 values for avr: "))
# f = int(input("8 values for avr: "))
# g = int(input("8 values for avr: "))
# h = int(input("8 values for avr: "))
# sum = a+b+c+d+e+f+g+h
# # avg = sum/8
# # print(avg)
# print(sum)

# n= int(input())
# sum = n*(n+1)/2
# print(sum)

# 280 
# r =int(input())
# area= 3.14*r*r/2
# print(area)
# add = 76.93+280 
# print(add)

# 2*(l+b)
# x+y+z = 20+15+5 
# 40 + 40 = 80
# l = int(input())
# l = int(input())

# b = 8
# l=10
# r=3
# rect =l*b
# # print(rect)
# area_cir = 3.14*r*r
# # print(area_cir)
# total = rect - area_cir
# print(total)



# l = 10*10
# t = 0.5*10*15
# total = l+t
# print(total)


# l=10
# b=20
# h=15
# p = 3*l+2*b
# print(p)


# tf = 108
# tc = ((tf-32)*5)/9
# print(tc)

# days = 98
# week = days/7
# rem_days = days%7
# print(week)
# print(rem_days)


# m=9564
# km = 9564/1000
# print(km)

# kg = 4.5
# gm = kg*1000
# print(gm)

# hr = 3.5
# min = hr*60
# print(min)
# sec = min*60
# print(sec)

# print(chr(97))
# print(ord('a'))

# p=int(input())
# t=int(input())
# r=int(input())
# si = p*t*r/100
# print(si)

# a=int(input())
# b=int(input())
# c=int(input())
# c=a
# a=b 
# b=c
# print(a)
# print(b)
# print(c)

# x=10
# y=20

# x= x^y
# y= x^y
# x= x^y
# print("x",x)
# print("y",y)


# a='a'
# b='b'
# A='A'
# B='B'
# print(chr(97))
# print(chr(98))
# print(chr(65))
# print(chr(66))
# print(ord('a'))
# print(ord('b'))
# print(ord('A'))
# print(ord('B'))


# print(50)

# x=50
# print(x)

# y=int(input("print y "))
# print("y: ",y)

# print("print thhe value ")
# z= int(input())
# print("z: ",z)

                    #    20-01-2026
                    #    Nested-if


# x = int(input("x :"))
# y = int(input("y :"))

# if x>y:
#     print("x is bigger")

# if y>x:
#     print("y is bigger")

# if x==y:
#     print("both are equal")

# x = int(input("x :"))

# if x>0:
#     print("x is positive")

# if x<0:
#     print("x is negative")

# if x==0:
#     print("no is neutral")


# x = int(input("x :"))
# y = int(input("y :"))
# z = int(input("z :"))

# if x>y and x>z :
#     print("x is greater")

# if y>x and y>z :
#     print("y is greater")

# if z>y and z>x :
#     print("z is greater")

# if x==y and y==z :
#     print("x is greater")



# x = int(input("x :"))
# if x%4==0 or x%400==0 and x%100!=0:
#     print("leap year")

# x = int(input("x :"))
# if x%4==0 and x%100!=0 or x%400==0 :
#     print("leap year")


                                                    #   21-01-026
                                                    #  if else 

# n = int(input("n :"))
# if n%2==0:
#     print("n is even")
# else:   
#     print("n is odd15")


# n = int(input("n :"))
# if n%2!=0:
#     print("n is odd")
# else:   
#     print("n is even")


# n = int(input("n :"))
# if n>=18:
#     print("n is eligible to vote")
# else:   
#     print("n is not eligible to vote")


# leap year
# n = int(input("n :"))
# if n%4==0 and n%100!=0 or n%400==0 :
#     print("leap year")  
# else:
#     print("not a leap year")    


# find the buzz no
# n = int(input("Enter a number: "))

# last_digit = n % 100

# if last_digit == 7 or n % 7 == 0:
#     print("Buzz number ")
# else:
#     print("Not a Buzz number")
# print(last_digit)


# automorphic no

# n = int(input("Enter a number: "))
# last_digit = n*n
# if last_digit % 10 == n:
#     print("Automorphic number ")
# else:
#     print("Not an Automorphic number")


                            #   22-01-2026
                            # Nested if else 



# x = int(input("x :"))
# y = int(input("y :"))
# eligble_age = x
# eligble_weight = y
# if eligble_age>=18 and eligble_weight>=47: 
#     print("eligible to donate blood")
# else :
#     print("not eligible to donate blood")


# p = int(input("p :"))
# c = int(input("c :"))
# m = int(input("m :"))
# if p>=60 and c>=60 and m>=70:
#     print("passed in all subjects") 
      
#     if p+c+m >=200 or p+c >= 135 :
#         print("passed in all subjects and you are selected")
#     else:
#         print("you are not selected ")
        
# else:
#     print("failed in one or more subjects")


                                    #   27-01-2026
                                    #   loops

# i=0 
# while(i<=100):
#     if(i%2==0):
#         print(i)
#         i=i+1

# i=1 
# while(i<=100):
#     print(i,"=",i*i)
#     i=i+1


# normal
# i=0
# while(i<=100):
#     print(i)
#     i=i+1

# even if
# i=0
# while(i<=100):
#     if(i%2==0):
#         print(i)
#     i=i+1

# even
# i=0
# while(i<=100):
#     print(i)
#     i=i+2

# odd if
# i=1
# while(i<=100):
#     if(i%2!=0):
#         print(i)
#     i=i+2

#odd
# i=1
# while(i<=100):
#     print(i,"=",i*i)
#     i=i+2



                                                          #28-01-2026

# i=1
# while(i<=100):
#     print(i,"=",i*i*i)
#     i=i+2



# i =450 
# while(i>=250):
#     print(i)
#     i=i-2 

# a=350
# while(a<=750):
#     if(a%2!=0):
#         print(a)
#     a=a+1

# a=751
# while(a>=451):
#     if(a%2!=0):
#         print(a)
#     a=a-1


# a=1
# while(a<=200):
#     print(a,"=",a*a,"a*a*a",a*a*a)
#     a=a+1

# a=150
# while(a>=1):
#     print(a)
#     a=a-2

# a=149
# while(a>=1):
#     print(a)
#     a=a-2 

# a=300
# while(a<=600):
#     if(a%3==0 and a%2==0):
#         print(a)
#     a=a+1


# a=900
# while(a>=750):
#     if(a%7==0 and a%2==0):
#         print(a,"=",a*a*a)
#     a=a-1

# b=450
# while(b<=650):
#     print(b)
#     b=b+1

# b=601
# while(b>=300):
#     print(b)
#     b=b-2

# a=200
# while(a<=800):
#     if(a%5==0 or a%10==0):
#         print(a)
#     a=a+1

# a=1000
# while(a>=1):
#     if (a%4==0 and a%6==0):
#         print(a,"=",a*a)
#     a=a-1

# b=500
# while(b>=1):
#     print(b)
#     b=b-1

                                                        #  29-01-2026                                

# for i in range(0,101,2):
#     print(i)

# factoprial
# n=12
# i=1
# while(i<=n):
#     if n%i==0:
#       print(i)
#     i=i-1


# i=1
# n=12
# while(i<=n):
#     if n%i==0:   
#         print(i)
#     i=i+1   


# i=int(input("enter a number: "))
# n=1
# for n in range(1,i+1):
#     if i%n==0:
#         print(n)


# i=int(input("enter a number: "))
# for n in range(i,0,-1):
#     if i%n==0:
#         print(n)


#fibbonaci series 
# n=int(input("enter a number: "))
# a=0     
# b=1

# i=0
# while(i<n):
#     c=a+b
#     a=b
#     b=c
#     print(c)
#     i=i+a


# n=int(input("enter a number: "))
# a=0     
# b=1
# i=0
# for i in range(0,n):
#     c=a+b
#     a=b
#     b=c 
#     print(c)
#     i=i+a

# n=int(input("enter a number: "))
# if n%2!=0:
#     print("weird")
# else:
#     if n>=2 and n<=5:
#         print("Not weird")
#     else:
#         if n>=6 and n<=20:
#             print("Weird")
#         else:
#             print("Not Weird")
#         # print("Even number outside range 2-5")

a = int(input("Enter first number: "))
print(a)

c = int(input("Enter first number: "))
print(c)