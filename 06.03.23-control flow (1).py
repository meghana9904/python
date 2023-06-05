#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Let's Fuel Up!
#A vehicle needs 10 times the amount of fuel than the distance it travels. However, it must always carry a minimum of 100 fuel before setting off.

#Create a function which calculates the amount of fuel it needs, given the distance.

#Examples
#calculate_fuel(15) ➞ 150

#calculate_fuel(23.5) ➞ 235

#calculate_fuel(3) ➞ 100
#Notes
#Distance will be a number greater than zero.
#Return 100 if the calculated fuel turns out to be less than 100.

def calculate_fuel(distance):
    fuel = distance * 10
    if fuel < 100:
        return 100
    else:
        return fuel


# In[2]:


calculate_fuel(15) 


# In[3]:


#2.Find the Bug: Returning the Container
#The packaging system is running wild! The candy is lying loose all over in the warehouse, the cereal is missing, and bread is stuffed in a bottle. What is going on here? The candy should be in plastic and the bread should be in a bag.

#The packaging machine is running the get_container() function to retrieve the container of a product. But something is not right...

#Examples
#get_container("Bread") ➞ "bag"

#get_container("Beer") ➞ "bottle"

#get_container("Candy") ➞ "plastic"

#get_container("Cheese") ➞ None
def get_container(product):
    matches = {"Bread" : "bottle","Milk" : "bottle","Beer" : "bottle","Eggs" : "carton","Cerials" : "box","Candy" : None,"Cheese" : None}
    return matches[product]


# In[4]:


get_container("Bread")


# In[7]:


#3.No Conditionals?
#Write a function that returns 0 if the input is 1, and returns 1 if the input is 0.

#Examples
#flip(1) ➞ 0

#flip(0) ➞ 1
#Notes
#Try completing this challenge without using any:

#Conditionals
#Ternary operators
#Negations
#Bit operators

def flip(value):
    if value==0:
        return 1
    elif value==1:
        return 0


# In[8]:


flip(0)


# In[9]:


flip(1)


# In[10]:


#4.Truthy or Falsy?
#A "truthy" value is a value that translates to True when evaluated in a Boolean context. All values are truthy unless they're defined as falsy.

#All falsy values are as follows:

#False
#None
#0
#[]
#{}
#""
#Create a function that takes an argument of any data type and returns 1 if it's truthy and 0 if it's falsy.

#Examples
#is_truthy(0) ➞ 0

#is_truthy(False) ➞ 0

#is_truthy("") ➞ 0

#is_truthy("False") ➞ 1
def is_truthy(value):
    if value:
        return 1
    else:
        return 0


# In[11]:


is_truthy(0)


# In[12]:


is_truthy("False")


# In[13]:


#5.Say "Hello" Say "Bye"
#Write a function that takes a string name and a number num (either 0 or 1) and return "Hello" + name if num is 1, otherwise return "Bye" + name.

#Examples
#say_hello_bye("alon", 1) ➞ "Hello Alon"

#say_hello_bye("Tomi", 0) ➞ "Bye Tomi"

#say_hello_bye("jose", 0) ➞ "Bye Jose"

def say_hello_bye(str,num):
    if num==1:
        return "hello"+" "+str
    elif num==0:
        return "Bye"+" "+str


# In[14]:


say_hello_bye("Tomi",0)


# In[1]:


#6.Darts is a target game played by throwing feathered darts at a circular board with numbered spaces. Our darts game is the simplest of all games. The score of a single turn is calculated based on the distance from the middle. You need to create a function that takes the dart location as two cartesian coordinates (x, y) and returns a score based on the distance from the middle, aka Bullseye (x=0, y=0).

#Bullseye and inner circle scores = 10 points
#Middle ring scores = 5 points
#Outer ring scores = 1 point
#Outside the target = 0 points
#We play it simple so a dart in the double or treble ring counts as usual and does not affect the segment score.

#Board and circle radius is as follows:

#Board radius and outer circle radius = 10 units
#Middle circle radius = 5 units
#Inner circle radius = 1 unit
#Short Description
#Convert cartesian coordinates (x, y) to polar coordinates (R, phi) and return the score based on the R value. R > 10 gives 0 points, 10 >= R > 5 gives 1 point, 5 >= R > 1 gives 5 points, R <= 1 gives 10 points.

#Examples
#darts_scoring(0, 0) ➞ 10

#darts_scoring(3, 2) ➞ 5

#darts_scoring(0, -0.8) ➞ 10
#Notes
#X, Y values can be both positive and negative.
#X, Y values can be int and float.
#No wrong type values will be given.


def calculate_dart_score(x,y):
    distance=(x**2+y**2)**0.5
    if distance<=1:
        return 10
    elif distance<=5:
        return 5
    elif distance<=10:
        return 1
    else:
        return 0


# In[2]:


calculate_dart_score(0,0)


# In[1]:


#7.Create a function that takes a list (slot machine outcome) and returns True if all elements in the list are identical, and False otherwise. The list will contain 4 elements.

#Examples
#test_jackpot(["@", "@", "@", "@"]) ➞ True

#test_jackpot(["abc", "abc", "abc", "abc"]) ➞ True

#test_jackpot(["SS", "SS", "SS", "SS"]) ➞ True

#test_jackpot(["&&", "&", "&&&", "&&&&"]) ➞ False

#test_jackpot(["SS", "SS", "SS", "Ss"]) ➞ False
#Notes
#The elements must be exactly identical for there to be a jackpot.

def test_jackpot(lst):
    lst=[]
    for y in lst:
         if y[0]==y[1]==y[2]==y[3]:
            return True
         else:
            return False


# In[2]:


test_jackpot(["@","@","@","@"])


# In[3]:


#8.Create a function that takes an array of hurdle heights and a jumper's jump height, and determine whether or not the hurdler can clear all the hurdles.

#A hurdler can clear a hurdle if their jump height is greater than or equal to the hurdle height.

#Examples
#hurdle_jump([1, 2, 3, 4, 5], 5) ➞ True

#hurdle_jump([5, 5, 3, 4, 5], 3) ➞ False

#hurdle_jump([5, 4, 5, 6], 10) ➞ True

#hurdle_jump([1, 2, 1], 1) ➞ False
#Notes
#Return True for the edge case of an empty array of hurdles. (Zero hurdles means that any jump height can clear them).


def f1(hurdle_height,jump_height):
    for x in hurdle_height:
        if jump_height<x:
            return True
        else:
            return False


# In[4]:


f1([1,2,3,4,7],jump_height=6)


# In[7]:


#9Create a function that takes a number as its argument and returns a list of all its factors.

#Examples
#factorize(12) ➞ [1, 2, 3, 4, 6, 12]

#factorize(4) ➞ [1, 2, 4]

#factorize(17) ➞ [1, 17]
#Notes
#The input integer will be positive.
#A factor is a number that evenly divides into another number without leaving a remainder. The second example is a factor of 12, because 12 / 2 = 6, with remainder 0.

def factorize(n):
    factors=[]
    for i in range(1,n+1):
        if n%i==0:
            factors.append(i)
    return factors
        


# In[8]:


factorize(12)


# In[11]:


#10.Create a function that goes through the array, incrementing (+1) for each odd-valued number and decrementing (-1) for each even-valued number.

#Examples
#transform([1, 2, 3, 4, 5]) ➞ [2, 1, 4, 3, 6]

#transform([3, 3, 4, 3]) ➞ [4, 4, 3, 4]

#transform([2, 2, 0, 8, 10]) ➞ [1, 1, -1, 7, 9]
#Notes
#N/A

def transform(value):
    result=[]
    for num in value:
        if num%2==0:
            result.append(num-1)
        else:
            result.append(num+1)
    return result


# In[12]:


transform([1, 2, 3, 4, 5])

