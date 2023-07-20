x=5
y=7.6
z=3+2j
print(type(x))
print(type(y))
print(type(z))
print(isinstance(z,complex))
print(isinstance(x,int))
print(isinstance(y,float))
# -------------------------#
print("""i am a
      brillent man""")
print("i am a brillent man")
# ----------------------------
f=7
def abhi():
    global f
    print(f)
    f=8
abhi()
print(f)
# ----------------------------
import keyword
print(keyword.kwlist)
help("keywords")
# ----------------------------
x=34
y=0
try:
    d=x//y
    print(d)
except ZeroDivisionError:
    print("The operation cant carried out")
finally:
    print("The block is ended")
# ---------------------------------------
def abhi():
    pass
def anathu():
    return
print(anathu())
def jas():
    a=9
    return a
print(jas())
# --------------------------------------
a=0
print(a)
del a
try:
    print(a)
except NameError:
    print("Not possible it is alredy deleted from reference:-")
#-------------------------------------------------------
for i in range(1,10,2):
    print(i)
#-------------------------------------------------------
for i in range(10):
    pass
#-------------------------------------------------------
ls=[1,2,3,4,5]
for i in ls:
    
    if i==0:
        continue
    print(i)
#-------------------------------------------------------
for i in ls:
    
    if i==0:
        break
    print(i)
#-------------------------------------------------------
for i in ls:
    
 continue
#-------------------------------------------------------
print('tag')
for i in ls:
    if i==1:
        pass
    print(i)
#-------------------------------------------------------
print('section')
for i in (ls):
    if i==1:
        continue
    print(i)
    
#-------------------------------------------------------
print("section")
string="abhinand is a good motivator"
print(string[:])
print(string[0:28])# slicingabhinand is a good motivator

#------------------------------------------------
print('section')
print(1 in ls)
print(1 not in ls)
#--------------------------
print('Formatting using % operator')
Integer=12
Float=1020
String='abhi'
print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %f\nHi I am string ... My value is %s"%(Integer,Float,String))

#----------------------------------------
print('Repetation')
print(2*ls)
print("concantaion")
v=[9,8,5,6,1,2]
print(ls+v)

#------------------------------
l=1,12,54,1,65,465
for i in l:
    print(i,end=" ")
try:
    l[0]=100
    print(l)
except TypeError:
    print()
    print('assignement is not possible')
finally:
    print("The operation for assigning values for a tuple after assigning is not possible it is immutable")
#-------------------------------------------
print('set')
print('set are mutable but only have unique values in it and cant contain immutable objects liks list and dic')
set1={1,2.5,'abhinand',(42,5)}
print(set1)
print(type(set1))
try:
    set2={{1:45}}
except:
    print("those dict and list are unhadhable in type")
#------------------------------------------------------------
s={}
print(type(s))
s1=set()
print(type(s1))
#--------------------------------------------------------
i1={1:"Abhi",'Age':26, 'Proffession':'Engineer'}
print(i1)
print(type(i1))
for x,y in i1.items():
    print(x,y)
#----------------in-heritance-------aslo their is polymorphisum is thier by over ridden the same speak functions
class Animal:
    def __init__(self,name):
        self.name=name
    def Speak(self):
        print("Animal Speak")
class Dog(Animal):
    def speak(self):
        print(f"The dog name is :{self.name} and it willl sepak like bow bow ")
class Bird(Animal):
    def Speak(self):
        print(f"The bird name {self.name} will speak like craw craw")
dog=Dog("gilli")
bird=Bird("Tete")
bird.Speak()
dog.speak()
#-----------------Encapsulation in python--------------------------
class Car:
    def __init__(self):
        self._brand="ford"
        self._milege=0
    def get_brand(self):
        return self._brand
    def get_milege(self):
        return self._milege
    def set_milege(self,milege):
        if milege>0:
            self._milege=milege
        else:
            print("It is not valid the milege")
    def drive(self,distance):
        self._milege+=distance
car=Car()
print(car.get_brand( ))
car.set_milege(500)
print(car.get_milege())
car.drive(600)
print(car.get_milege())
#-------------------data abstraction in python------------------------
from abc import abstractmethod,ABC
class Shape:
    @abstractmethod
    def Area(self):
        pass
    def Perimeter(self):
        pass
class Rectnagle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def Area(self):
        return self.width*self.length
    def Perimeter(self):
        return 2*(self.length+self.width)
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        return 3.14*self.radius*self.radius
    def Perimeter(self):
        return 2*3.14*self.radius
c=Circle(3)
r=Rectnagle(4,3)
print(c.Area())
print(r.Area())
print(c.Perimeter())
print(r.Perimeter())
#-------------------defaut arguments in python------------------
def numbers(x,y=30):
    print("First number is :- ",x,end=" ")
    print()
    print("Second number is :-",y,end=" ")
    print()
numbers(2)
numbers(12,56)
#-------------------defaut arguments in python------------------
print()
print("Section")
def n(n1,n2):
    print(n1)
    print(n2)
n(n2=89,n1=56)#key Word in a fucntion       
#-------------------- variable length arguments in python--
print()
print("Section")
def variable_length_args(*a):
    for i in a:
        print(i,end=" ")
variable_length_args(12,1,456,4,69,8)
#-------------------- variable length arguments kwrwgs send the data as a key values pair in python--
print()
print("Section")
def variable_length_kwrgs(**b):
    for x,y in b.items():
        print(x,y,end=" ")
variable_length_kwrgs(name="abhi",name2 ='elis')
#-----------------------Lambada fucntions----------
print()
print()
print("Section")
add=lambda num:1/num
print("The reciproiocal of the number is ",add(2))

print("Add numbers using lambda functions")
add1=lambda x,y:x+y
print(add1(12,13))

print("Is palindrome or not ")
result=lambda s:s==s[::-1]
s="malayalam"
print(result(s))
print(s[::-1])

print("Filter the odd elements in the list using along with lambda")
oddnum=list(filter(lambda n:n%2==0,ls))
ls=[2,12,545,45,4,5]
print(oddnum)

print("The square of all valuse in the list")
print(list(map(lambda x:x**2 ,ls)))
print("Factorial of a number by using a lambada and recrusion")
factorial=lambda n:1 if n==0 else n*factorial(n-1)
print(factorial(6))

print()
sor=[(1,2),(5,6),(8,1),(7,9)]
print("Sorted a a tuples by using it is second element")
print(sorted(sor,key=lambda n:n[1]))

print()
print("Convert the list of string in a list to upper case using lamda function")
lowercase=['abhinand','ananthu','jasmin']
uppercase=list(map(lambda x:x.upper(),lowercase))
print(uppercase)

print()
print("Distructor in python")
class Employee:
    def __init__(self):
        print("Employee Created")
    def __del__(self):
        print("Destructor called")
def Creating_object():
    print("Making a object")
    obj=Employee()
    print("Functions is ended")
    return obj
print("Calling the creating object function")
obj=Creating_object()
print("Programme is ended")

print()
print("Expection in python")
g=0
n=8

try:
    res=n/g
except ZeroDivisionError:
    print("The operation cant be alloweded")
else:
    print("Exit")
finally:
    print("The problem is solved ")
# nums=[21,45,88,4]
# if len(nums)>3:
#     raise Exception(" length of the given list must be greter than 3")

#----------------------Modules------------------------
# print("Modules")
# import abc # all module
# from abc import ABC
# import abc as a
#---------------List comprehension in python---------
lst=[num for num in range(30) if num % 2==0]
print(lst)
# inp=[int(input("Enter the numbers to store in list :- ")) for i in range(10)]
# print(inp)

#-------------------Itererator------------------------------------
print()
my_list=[12,54,87,87,8,78,785,4,5]  
my_iter=iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
try:
    print(next(my_iter))
except StopIteration:
    print("Range is reached")
finally:
    print("Finshed")

h=[56,64,465,4]
l=['a','d','v','t']
c=zip(h,l)
print(c)

print()
print('Genrator in python')
def simple():
    for i in range(10):
        if i % 2==0:
            yield i
for i in simple():
    print(i)

print('Section')
print()
def counter(n):
    while n>0:
        yield n
        print("After Yield")
        n-=1
o=counter(3)
print(next(o))
print(next(o))
print(next(o))

print("Section for decoraters")
print()
def outer():
    def inner():
        print('Abhi')
try:
    call=inner()
    print(call)
except NameError:
    print("The lexical scope of the inner function is only limited inside the outer function we need some other techniques to solve this")
finally:
    print("Cleared")
def outer_1():
    def inner_1():
        print("I am inside a outer")
    return inner_1
call_1=outer_1()
call_1()    

print("Example of the above two")
print()
def divide(x,y):
    print(x/y)
def outer_div(fun):
    def inner(x,y):
        if x<y:
            x,y=y,x
        return fun(x,y)
    return inner
caller_3=outer_div(divide)
caller_3(2,4)
print("We modified the function without modifying anything inside the function hence it is known as decorater")

print("Using @ decorter key word")

def outer_2(fun):
    def inner(x,y):
        if x<y:
            x,y=y,x
        return fun(x,y)
    return inner    
@outer_2
def div_(x,y):
    r=(x/y)
    print(r)
    
div_(2,4)