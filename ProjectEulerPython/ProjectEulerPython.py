#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Project Euler problems solved using python
#--------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 1: Multiples of 3 and 5 
#  (sum up all multiples of 3 and 5 < 1000)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

#def MultSum(a, b, max):
#    SumSum=0
#    for i in range(1,max):
#        if i%a==0 or i%b==0:
#            SumSum+=i
#    return SumSum

#print(MultSum(3,5,1000))

#--------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 2: Even Fibonacci numbers
#  (Sum up all even Fibonacci numbers (1,2,3,5,8,13,21,34,55,...) <4 Mio)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

#def AddEvFib(max):
#    SumSum=0
#    a=1
#    b=2
#    while(b<max):
#        if b%2==0:
#            SumSum+=b
#        temp=a+b
#        a=b
#        b=temp
#    return SumSum

#print(AddEvFib(4000000))

#--------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 3: Largest prime factor of 600851475143
#  (Calculate the largest prime factor of 600851475143)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#import math as m

#def isPrime(a):
#    for i in range(2,int(m.sqrt(a)),1):   #range only accepts integers, not floats, etc.
#        if a%i==0:
#            return False
#    return True

#def LarPrFac(a):
#    i=2
#    while(i<a):
#        if isPrime(i) and a%i==0:
#            a/=i
#            i=2
#        else: 
#            i+=1
#    return a

#print(LarPrFac(600851475143))

#--------------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 4: Largest palindrome product
#  (Find the largest palindrome (e.g. 9009, 1111, 121) that can be written as product of two 3-digit numbers)
#----------------------------------------------------------------------------------------------------------------------------------------------------------

#def isPalin(a):
#    c=str(a)    #String conversion much easier than in C++
#    rev=c[::-1] #Slicing backwards, also much easier
#    if c==rev:
#        return True
#    return False

#def LargPalin(b):
#    max=0
#    for i in range(1,b+1,1):
#        for j in range(1,b+1,1):
#            if isPalin(i*j) and i*j>max:
#                max=i*j
#    return max

##print(isPalin(9876))
##print(isPalin(9009))
#print(LargPalin(999))

#----------------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 5: Smallest multiple 
#  (Find the smallest number that is evenly divisible by all numbers from 1 to 20)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#def Step(a):
#    Prod=a
#    for i in range(a-1,1,-1):
#        if Prod%i!=0:
#            print(i,'\n')
#            Prod*=i
#    return Prod

##def EvDiv(a):   #This worked in C++, because it is very fast, but took ages in python, version above is much better anyways
##    i=a
##    counter=0
##    while counter<a:
##        counter=0
##        for j in range(1,a+1,1):
##            if i%j==0:
##                counter+=1
##        i+=a
##    return i-a

#print(Step(20))
#--------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 6: Sum square difference 
#  (Find the difference of the square of the sum of all numbers <=100 and the sum of the squares of all numbers <=100)
#  (sum_i=1_to_n(i))^2 - sum_i=1_to_n(i^2), n=100
#--------------------------------------------------------------------------------------------------------------------------------------------------------

##In this case it makes sense to have a look at sum conversions before starting with programming:
##(sum_i=1_to_n(i))^2 = (0.5n(n+1))^2
##and
##sum_i=1_to_n(i^2)= (1/6)n(n+1)(2n+1)
##and (0.5n(n+1))^2 - (1/6)n(n+1)(2n+1) = 0.25n(n^3 + (2/3)n^2 - n - (2/3))

#def Dif(n):
#    return 0.25*n*(n**3+(2/3)*n**2-n-(2/3))

##print(Dif(10))
#print(Dif(100))

#--------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 7: 10001st prime
#  (Find the 10001st prime number)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

#import math

#def isPrime(n):
#    if n<=1:
#        return False
#    elif n==2 or n==3:
#        return True
#    else:
#        for i in range(2,int(math.sqrt(n)+1),1):  #It is important to add 1 to the sqrt, since the stop criterion of range is <stop not <=stop
#            if n%i==0:
#                return False
#        return True


#def nthPrime(n):
#    n-=1         #necessary because i is never 2 and thus 2 is not counted as a prime
#    i=1
#    counter=0
#    while counter<n:
#        if isPrime(i):
#            counter+=1
#        i+=2
#    return i-2

#print(nthPrime(10001))

#--------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 8: Largest product in a series
#  (Find the largest product of thirteen adjacent numbers within a series of 1000 numbers)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

#file=open('Problem_8.txt','r')         #file is opened with a permission to read, w for write, if second argument is forgotten file is cleared!!!

#f=file.readlines()                     #reads file line by line into a list (first line = f[0])

#res = "".join(f)                       #joins all lines to one element (list of strings -> string)
#res=res.replace('\n','')               #replaces all line breaks with nothing (==> removes them)
#res=list(res)                          #turns string into list of chars
#res = list(map(int, res))              #converts all elements from char to int (most elegant way)
##print(res)

#L=len(res)

#NrDig=13                               #Number of digits within the 1000 digit series the product of which shall be calculated
#Max=0                                  #Variable for maximum value of product
#Prod=1                                 #Variable to store each product

#for i in range(0,L,1):                 #Outer loop that loops over all elements of the list
#    if Prod>Max:                       #Comparison of current product and maximum value
#        Max=Prod                       #Replacing maximum value with current product if greater
#    Prod=1                             #Setting product back to one after each element
#    for j in range(0,NrDig,1):         #Inner loop over all elements of the product, NrDig can be used because stop condition is <NrDig
#        a=i+j                          #For each iteration the position within the list is calculated
#        if(a>=L-1):                    #If the end of the list is reached
#            a-=L                       #it skips back to the first element
#        Prod*=res[a]                   #The product is multiplied with each element of the 13 digits

#print(Max)                             #prints maximum product of NrDig elements in a row of the 1000 digit number

#file.close()                           #file is closed

#--------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Problem 9: Special Pythagorean triplet
# (Find the numbers a,b and c for which a^2+b^2=c^2 and a+b+c=1000
#--------------------------------------------------------------------------------------------------------------------------------------------------------

##a+b+sqrt(a^2+b^2)=1000

#import math

#a=0

#for i in range(0,400,1):
#    if(a==1):                                                #This requires some calculation for each iteration but saves on total iterations
#        break
#    for j in range(0,400,1):
#        if i+j+math.sqrt(i**2+j**2)==1000:
#            print(str(i),",",str(j),",",str(1000-i-j),"\n")
#            print(i*j*(1000-i-j))
#            a=1                                              #this is used to break the outer loop
#            break                                            #this only breaks the inner loop

#--------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 10: Summation of primes
#  (Sum up all primes <2 000 000)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

#import math

#def isPrime(n):
#    #if n<=1:                                 #Only commented to improve runtime, see below
#    #    return False
#    #elif n==2 or n==3:
#    #    return True
#    #else:
#    for i in range(2,int(math.sqrt(n)+1),1):  #Left out the first part of isPrime for better runtime and added 2+3=5 to the sum
#        if n%i==0:
#            return False
#    return True

#Sum=0
#for i in range(5,2000000,2):                  #Started at 5 for better runtime of isPrime
#    if isPrime(i):
#        Sum+=i

#print(Sum+5)                                  #Works but runtime is at least a minute


#--------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 11: Largest product in a grid
#  (Find the largest product of four adjacent numbers (up, down, right, left, diagonally) within a 20X20 grid)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

#import numpy as np

#file=open('Problem_11.txt','r')                #file is opened with a permission to read, w for write, if second argument is forgotten file is cleared!!!
#f=file.readlines()                             #reads file line by line into a list
#grid_raw=[]                                    #new grid list of strings
#for line in f:
#    grid_raw.append(line.rstrip('\n'))         #content of f is copied to grid without the line breaks

#grid=[]      
#for line in grid_raw:                          #each line of the grid is split into the respective numbers
#    grid.append(line.split())

#Max=0

#for i in range(17):                            #loop over the first 16 lines of the grid
#    for j in range(17):                        #loop over the first 16 columns of the grid
#        Prod1=Prod2=Prod3=Prod4=1              #four products are created and set to 1
#        for k in range(4):                     #loop over four elements
#            Prod1*=int(grid[i][j+k])           #product over horizontal objects
#            Prod2*=int(grid[i+k][j])           #product over vertical objects
#            Prod3*=int(grid[i+k][j+k])         #product over diagonal objects left upper to right lower
#            if(i>=3):                  
#                Prod4*=int(grid[i-k][j+k])     #product over diagonal objects left lower to right upper
#        Max=max(Max,Prod1,Prod2,Prod3,Prod4)   #maximum value is set to maximum of products and former maximum
        
#print(Max)

#file.close()                           #file should always be closed after use

#--------------------------------------------------------------------------------------------------------------------------------------------------------
