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
from abc import ABC,abstractclassmethod
class Area