#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1 Create a function that takes a boolean variable flag and returns it as a string.
#Examples
#bool_to_string(True) ➞ "True"

#bool_to_string(False) ➞ "False"


def bool_to_string(flag):
    if flag==True:
        return "True"
    else:
        return "False"


# In[4]:


bool_to_string(True)


# In[5]:


#2 Create a function that returns True when num1 is equal to num2; otherwise return False.
#Examples
#is_same_num(4, 8) ➞ False

#is_same_num(2, 2) ➞  True

#is_same_num(2, "2") ➞ False


def f1(num1,num2):
    if num1==num2:
        return True
    else:
        return False


# In[6]:


f1(2,5)


# In[7]:


#3 Create a function that takes a number as its only argument and returns True if it's less than or equal to zero, otherwise return False.
#Examples
#less_than_or_equal_to_zero(5) ➞ False

#less_than_or_equal_to_zero(0) ➞ True

#less_than_or_equal_to_zero(-2) ➞ True


def number(value):
    if value<=0:
        return True
    else:
        return False


# In[8]:


number(-2)


# In[9]:


#4 Emmy has written a function that returns a greeting to users. However, she's in love with Mubashir, and would like to greet him slightly differently. She added a special case in her function, but she made a mistake.
#Can you help her?
#Examples
#greeting("Matt") ➞ "Hello, Matt!"

#greeting("Helen") ➞ "Hello, Helen!"

#greeting("Mubashir") ➞ "Hello, my Love!"

def emmy(person_name):
    if person_name=="Mubashir":
       print("hello,my Love!")
    else:
        print("hello, person_name")


# In[10]:


emmy("Mubashir")


# In[11]:


#5 Create a function that takes two arguments. Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10.
#Examples
#makes10(9, 10) ➞ True

#makes10(9, 9) ➞ False

#makes10(1, 9) ➞ True

def operation(num1,num2):
    if num1==10 or num2==10 or num1+num2==10:
        return True
    else:
        return False


# In[12]:


operation(1,9)


# In[13]:


#6 Create a function that takes three arguments prob, prize, pay and returns True if prob * prize > pay; otherwise return False.
#To illustrate:
#profitable_gamble(0.2, 50, 9)
#... should yield True, since the net profit is 1 (0.2 * 50 - 9), and 1 > 0.

def profitable_gamble(prob,prize,pay):
    if prob*prize>pay:
        return True
    else:
        return False


# In[14]:


profitable_gamble(0.2,50,9)


# In[15]:


#7 Create a function that takes an integer and returns True if it's divisible by 100, otherwise return False.
#Examples
#divisible(1) ➞ False

#divisible(1000) ➞ True

#divisible(100) ➞ True

def divisible(num):
    if num%100==0:
        return True
    else:
        return False


# In[16]:


divisible(1)


# In[17]:


divisible(200)


# In[18]:


#8 Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
#Examples
#comp("AB", "CD") ➞ True

#comp("ABC", "DE") ➞ False

#comp("hello", "edabit") ➞ False

def comp(string1,string2):
    if len(string1)==len(string2):
        return True
    else:
        return False


# In[19]:


comp("abbhhjedj","hiwhihw")


# In[20]:


#9 Given a string, return True if its length is even or False if the length is odd.

#Examples
#odd_or_even("apples") ➞ True
# The word "apples" has 6 characters.
# 6 is an even number, so the program outputs True.

#odd_or_even("pears") ➞ False
# "pears" has 5 letters, and 5 is odd.
# Therefore the program outputs False.

#odd_or_even("cherry") ➞ True

def word(string):
    if len(string)%2==0:
        return True
    else:
        return False


# In[22]:


word("apple")


# In[23]:


word("applee")


# In[24]:


#10 Create a function that takes a string; we'll say that the front is the first three characters of the string. If the string length is less than three characters, the front is whatever is there. Return a new string, which is three copies of the front.
#Examples
#front3("Python") ➞ "PytPytPyt"

#front3("Cucumber") ➞ "CucCucCuc"

#front3("bioshock") ➞ "biobiobio"

def f1(string):
    if len(string)<3:
        return string
    else:
        return string[:3]*3


# In[25]:


f1("meghana")


# In[26]:


#11 Given a string, return True if its length is even or False if the length is odd.
#Examples
#odd_or_even("apples") ➞ True
# The word "apples" has 6 characters.
# 6 is an even number, so the program outputs True.

#odd_or_even("pears") ➞ False
# "pears" has 5 letters, and 5 is odd.
# Therefore the program outputs False.

#odd_or_even("cherry") ➞ True


def f1(string):
    if len(string)%2==0:
        return True
    else:
        return False


# In[28]:


f1("meghaa")


# In[29]:


#12 Is the Number Even or Odd?
#Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers.

#Examples
#isEvenOrOdd(3) ➞ "odd"

#isEvenOrOdd(146) ➞ "even"

#isEvenOrOdd(19) ➞ "odd"


def isevenorodd(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"


# In[30]:


isevenorodd(23)


# In[31]:


#13 Create a function that takes in a word and determines whether or not it is plural. A plural word is one that ends in "s".
#Examples
#is_plural("changes") ➞ True

#is_plural("change") ➞ False

#is_plural("dudes") ➞ True

#is_plural("magic") ➞ False

def plural(word):
    if word[-1]=="s":
        return True
    else:
        return False


# In[33]:


plural("pens")


# In[34]:


#14  Create a function that takes a string (a random name). If the last character of the name is an "n", return True, otherwise return False.
#Examples
#is_last_character_n("Aiden") ➞ True

#is_last_character_n("Piet") ➞ False

#is_last_character_n("Bert") ➞ False

#is_last_character_n("Dean") ➞ True

def string(name):
    if name[-1]=="n":
        return True
    else:
        return False


# In[35]:


string("pen")


# In[45]:


#15 Find the Bug: Returning the Container
#The packaging system is running wild! The candy is lying loose all over in the warehouse, the cereal is missing, and bread is stuffed in a bottle. What is going on here? The candy should be in plastic and the bread should be in a bag.

#The packaging machine is running the get_container() function to retrieve the container of a product. But something is not right...

#Examples
#get_container("Bread") ➞ "bag"

#get_container("Beer") ➞ "bottle"

#get_container("Candy") ➞ "plastic"

#get_container("Cheese") ➞ None

def get_container(product):
    matches = {
"Bread" : "bottle",
"Milk" : "bottle",
"Beer" : "bottle",
"Eggs" : "carton",
"Cerials" : "box",
"Candy" : None,
"Cheese" : None
}
    return matches[product]


# In[46]:


get_container("Bread")


# In[48]:


#16 Flip the Boolean
#Due to a programming concept known as truthiness, certain values can be evaluated to (i.e. take the place of) booleans. For example, 1 (or any number other than 0) is often equivalent to True, and 0 is often equivalent to False.

#Create a function that returns the opposite of the given boolean, as a number.

#Examples
#flip_bool(True) ➞ 0

#flip_bool(False) ➞ 1

#flip_bool(1) ➞ 0

#flip_bool(0) ➞ 1


def flip_bool(value):
    if value>=1:
        return True
    else:
        return False


# In[49]:


flip_bool(1)


# In[50]:


flip_bool(0)


# In[51]:


#17.Write a function that accepts base (decimal), height (decimal) and shape ("triangle", "parallelogram") as input and calculates the area of that shape.
#Examples
#area_shape(2, 3, "triangle") ➞ 3

#area_shape(8, 6, "parallelogram") ➞ 48

#area_shape(2.9, 1.3, "parallelogram") ➞ 3.77

def shapes(base,height,shape="triangle"or"parallelogram"):
    if shape=="triangle":
        area_of_triangle=0.5*base*height
        return area_of_triangle
    else:
        area_of_parallelogram=base*height
        return area_of_parallelogram


# In[52]:


shapes(3,2,"parallelogram")


# In[53]:


shapes(4,6,"triangle")


# In[1]:


#18 You will need to write three unfinished logic gates. Continue to write the three logic gates: AND, OR, and NOT.
#Examples
#AND(1, 1) ➞ 1
#AND(0, 0) ➞ 0

#OR(1, 0) ➞ 1
#OR(1, 1) ➞ 1

#NOT(0) ➞ 1
#NOT(1) ➞ 0
def AND_gate(a,b):
    return a and b
def OR_gate(a,b):
    return a and b
def NOT_gate (a,b):
    return a and b
a=input("type 1 or 0 :")
b=input("type 1 or 0 :")

output_AND=AND_gate(a,b)
print("AND gate output :",output_AND)

output_OR=OR_gate(a,b)
print("OR agte output :",output_OR)

output_NOT=NOT_gate(a,b)
print("NOT gate output :",output_NOT)


# In[2]:


#19. A bartender is writing a simple program to determine whether he should serve drinks to someone. He only serves drinks to people 18 and older and when he's not on break.
#Given the person's age, and whether break time is in session, create a function which returns whether he should serve drinks.
#Examples
#should_serve_drinks(17, True) ➞ False

#should_serve_drinks(19, False) ➞ True

#should_serve_drinks(30, True) ➞ False

def bartender(age,break_time="yes"or"no"):
    if age>=18 and break_time=="yes":
        return "serve"
    else:
        return "no_serving"


# In[3]:


bartender(7,"no")


# In[10]:


#20.Write a function that returns the string "even" if the given integer is even, and the string "odd" if it's odd.

def even_or_not(string):
    remainder=bool(string%2)
    if remainder==True:
       return "odd"
    else:
        return "even"


# In[11]:


even_or_not(24)


# In[13]:


#21. Create a function that takes a string txt and a number n and returns the repeated string n number of times.

#If given argument txt is not a string, return Not A String !!

#Examples
#repeat_string("Mubashir", 2) ➞ "MubashirMubashir"

#repeat_string("Matt", 3) ➞ "MattMattMatt"

#repeat_string(1990, 7) ➞ "Not A String !!"

def repeat_string(string,times):
    new_string=string*times
    return new_string


# In[14]:


repeat_string("meghana",2)


# In[15]:


repeat_string("pen",4)


# In[58]:


#22.Taxi Journey
#A taxi journey costs $3 for the first kilometer travelled. However, all kilometers travelled after that will cost $2 each.

#Create a function which returns the distance that the taxi must've travelled, given the cost as a parameter.

#Examples
#journey_distance(3) ➞ 1
# The first kilometer costs $3

#journey_distance(9) ➞ 4
# The first kilometer costs $3 plus the other three kilometers (costing $2 each)

#journey_distance(5) ➞ 2

def journey(cost):
    distance=1
    if cost==3:
        return 1
    else:
        return distance+int((cost-3)/2)


# In[59]:


journey(3)


# In[61]:


journey(9)


# In[56]:


#23 Given a list that contains the fulcrum "f", the effort "e", and the load "l", write a function that determines whether or not the list shows a first class lever, second class lever, or a third class lever.

#Examples
#determine_lever(["e", "f", "l"]) ➞ "first class lever"

#determine_lever(["e", "l", "f"]) ➞ "second class lever"

#determine_lever(["f", "e", "l"]) ➞ "third class lever"

def determine_lever(falcrum,effort,load):
                    if falcrum=="middle"and effort=="right"and load=="left":
                        return "1st class lever"
                    elif  falcrum=="left"and effort=="right"and load=="middle":
                        return "2nd class lever"
                    else:
                        return "3rd class lever"


# In[57]:


determine_lever("middle","right","left")


# In[62]:


#23 Movie Theatre Admittance
#Write a function that checks whether a person can watch an MA15+ rated movie. One of the following two conditions is required for admittance:

#The person is at least 15 years old.
#They have parental supervision.
#The function accepts two parameters, age and is_supervised. Return a boolean.

#Examples
#accept_into_movie(14, True) ➞ True

#accept_into_movie(14, False) ➞ False

#accept_into_movie(16, False) ➞ True

def accept_into_movie(age,parent="yes"or"no"):
    if age>15 or age==15 and parent=="yes":
        return True
    else:
        return False


# In[63]:


accept_into_movie(16,"yes")


# In[74]:


#24 Word Numbers!
#Create a function that returns a number, based on the string provided. Here is a list of all digits:

#String	Number
#"one"	1
#"two"	2
#"three"	3
#"four"	4
#"five"	5
#"six"	6
#"seven"	7
#"eight"	8
#"nine"	9
#"zero"	0
#Examples
#word("one") ➞ 1

#word("two") ➞ 2

#word("nine") ➞ 9

def word(var1):
    number={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
    return number[var1]


# In[75]:


word("one")


# In[ ]:


#25. Write a function that uses the ternary operator to return "yeah" if b is True, and "nope" otherwise.

#Examples
#yeah_nope(True) ➞ "yeah"

#yeah_nope(False) ➞ "nope"


# In[8]:


#26.Which Generation Are You?
#Try finding your ancestors and offspring with code.

#Create a function that takes a number x and a character y ("m" for male, "f" for female), and returns the name of an ancestor (m/f) or descendant (m/f).

#If the number is negative, return the related ancestor.
#If positive, return the related descendant.
#You are generation 0. In the case of 0 (male or female), return "me!".
#Examples
#generation(2, "f") ➞ "granddaughter"

#generation(-3, "m") ➞ "great grandfather"

#generation(1, "f") ➞ "daughter"

def find_relative_name(x, y):
    generations = int(x)
    gender = y.lower()

    if generations == 0:
        return "me!"

    if gender == "m":
        if x < 0:
            return "ancestor " + str(generations) + " generations up"
        else:
            return "descendant " + str(generations) + " generations down"

    if gender == "f":
        if x < 0:
            return "ancestress " + str(generations) + " generations up"
        else:
            return "descendant " + str(generations) + " generations down"

    return "Invalid gender specified. Please use 'm' for male or 'f' for female."


# In[9]:


find_relative_name(1,"f")


# In[ ]:


#27.A Day at the Market
#Backpack Bill and Wallet Will set off for the annual festival. As they approach the stalls, Bill retorts that he'll be able to bring home more stuff than Will. Taking this as a challenge, Will refutes and a competition spurs into action.

#Backpack Bill has an infinite inventory space, but a limited number of coins.
#Wallet Will has an infinite number of coins, but a limited inventory space.
#Create a function that returns the name of the man who can bring home the most items. The parameters are given as follows:

#Bill's amount of money.
#Will's amount of inventory space.
#The item's price.
#The item's size.
#Worked Example
#who_wins_tonight(40, 95, 5, 10) ➞ "Will"

# The item costs 5 coins and takes up 10 inventory spaces.
# Bill can only buy a maximum of 8 items (40 coins DIV 5 = 8).
# Will can only bring home a maximum of 9 items. (95 inventory spaces DIV 10 = 9).
# Will is the winner.
#Examples
#who_wins_tonight(20, 20, 5, 10) ➞ "Bill"

#who_wins_tonight(10, 2, 20, 1) ➞ "Will"

#who_wins_tonight(3, 7, 2, 5) ➞ "Tie"
#Notes
#DIV means a floored division. That means you round down after dividing.
#Return "Tie" if both men can afford the same amount of stuff.
#All numbers will be positive integers.

def who_wins_tonight(Bill's amount of money,Will's amount of inventory space,The item's price,The item's size):
    


# In[5]:


#28.Integer in Range?
#Create a function that validates whether a number n is within the bounds of lower and upper. Return False if n is not an integer.

#Examples
#int_within_bounds(3, 1, 9) ➞ True

#int_within_bounds(6, 1, 6) ➞ False

#int_within_bounds(4.5, 3, 8) ➞ False
#Notes
#The term "within bounds" means a number is considered equal or greater than a lower bound and lesser (but not equal) to an upper bound, (see example #2).
#Bounds will be always given as integers.

def int_within_bounds(integer,lower,upper):
    if integer in range(lower,upper):
        return True
    else:
        return False


# In[7]:


int_within_bounds(6,1,5)


# In[ ]:


#29.Minimal IV: if-elif-else Inferno
#Check the principles of minimalist code in the intro to the first challenge.

#In the Code tab you will find a code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section below.

#Write a function that returns the boolean True if the given number is zero, the string "positive" if the number is greater than zero or the string "negative" if it's smaller than zero.

#Tips
#Executing a return will effectively end your function.

#For example, the code:

#def compare_to_100(x):
    #if x > 100:
        #return "greater"
    #elif x < 100:
        #return "smaller"
    #else:
        #return "equal"
#Can be simplified to:

#def compare_to_100(x):
    #if x > 100:
        #return "greater"
    #if x < 100:
        #return "smaller"
    #return "equal"
#If x is greater than 100, Python will not execute the code past the first return.
#If x is smaller than 100, Python will not execute the code inside the first if statement or past the second return.
#If x is equal to 100, Python will not execute the code inside the two if statements.
#This can only be used if you have a return inside your if statement.
#Bonus
#Further simplification of the code above:

#def compare_to_100(x):
    #return "greater" if x > 100 else "smaller" if x < 100 else "equal"
#Notes
#This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your suggestions in the Comments.
#Readability is indeed a subjective concept. Let's discuss it! Feel free to leave your opinion in the Comments.
#You can find all the exercises in this series over here.


# In[13]:


#30.Is the Water Boiling?
#Create a function that determines if the temp of the water is considered boiling or not. temp will be measured in Fahrenheit and Celsius.

#Examples
#is_boiling("212F") ➞ True

#is_boiling("100C") ➞ True

#is_boiling("0F") ➞ False
#Notes
#The boiling point of water is 212F in Fahrenheit and 100C in Celsius.

def is_boiling(temp,type="F"or"C"):
    if type=="F":
        if temp>=212:
            return True
        else:
            return False
    if type=="C":
        if temp>=100:
            return True
        else:
            return False
    


# In[14]:


is_boiling(212,"F")


# In[15]:


is_boiling(200,"F")


# In[16]:


is_boiling(212,"C")


# In[17]:


is_boiling(2,"C")


# In[18]:


is_boiling(101,"C")


# In[31]:


#31.Largest Numbers
#Create a function that takes two arguments of a list of numbers lst and a constant number n and returns the n largest numbers from the given list.

#Examples
#largest_numbers(2, [4, 3, 2, 1]) ➞ [3, 4]

#largest_numbers(1, [7, 19, 4, 2]) ➞ [19]

#largest_numbers(3, [14, 12, 57, 11, 18, 16]) ➞ [16, 18, 57]

#largest_numbers(0, [1, 3, 4, 2]) ➞ []
#Notes
#The returned list must be sorted in ascending order.

def largest_numbers(n,lst):
    return sorted(lst,reverse=True)[:n]


# In[25]:


largest_numbers(2,[4,3,2,1])


# In[26]:


largest_numbers(3, [6,9,2,10,16,0])


# In[27]:


largest_numbers(2, [3,9,4,27,85])


# In[32]:


#32.Length and Element of Range
#Create a function that takes a range object r, index i, and returns a list where the first element is the number of elements in the range object, and the second element is the element of the range object at the given index.

#Examples
#length_element(range(2, 4), 0) ➞ [2, 2]

#length_element(range(12, 15, 2), 1) ➞ [2, 14]

#length_element(range(40, 50, 3), 2) ➞ [4, 46]

def length_element(r, i):
    length = len(r)
    element = r[i]
    return [length, element]


# In[34]:


length_element(range(2,4),0)


# In[35]:


length_element(range(12, 15, 2), 1)


# In[6]:


#33.Minimal IX: This or That
#Check the principles of minimalist code in the intro to the first challenge.

#In the Code tab you will find a code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section below.

#Write a function that returns the first truthy argument passed to the function. If all arguments are falsy, return the string "not found". The function will be called with a minimum of one and a maximum of four arguments: a, b, c, d.

#Tips
#The operator or can be used to assign or return the first truthy value among two or more elements. If no truthy value is found, the last element will be returned.

#For example, the code:

#def one_of_these(a, b, c):
    #return a if a else b if b else c
#Can be simplified to:

#def one_of_these(a, b, c):
    #return a or b or c
    
def first_one(a,b,c,d):
    if bool(a) == True:
        return a
    elif bool(b) == True:
        return b
    elif bool(c) == True:
        return c
    elif bool(d) == True:
        return d
    else:
        return "not found"


# In[9]:


first_one(b,c,d)


# In[10]:


#34.Is It a Triangle?
#Create a function that takes three numbers as arguments and returns True if it's a triangle and False if not.

#Examples
#is_triangle(2, 3, 4) ➞ True

#is_triangle(3, 4, 5) ➞ True

#is_triangle(4, 3, 8) ➞ False
#Notes
#a, b and, c are the side lengths of the triangles.
#Test input will always be three positive numbers.

def is_triangle(a,b,c):
    if a+b>c or b+c>a or c+a>b:
        return True
    else:
        return False
    


# In[11]:


is_triangle(2,3,4)


# In[13]:


#35.Truthy or Falsy?
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


# In[14]:


is_truthy(0)


# In[15]:


is_truthy("")


# In[16]:


is_truthy("False")


# In[17]:


#36.Both Zero, Negative or Positive
#Write a function that returns True if both numbers are:

#Smaller than 0, OR ...
#Greater than 0, OR ...
#Exactly 0
#Otherwise, return False.

#Examples
#both(6, 2) ➞ True

#both(0, 0) ➞ True

#both(-1, 2) ➞ False

#both(0, 2) ➞ False

def both(num1,num2):
    if num1<0 and num2<0:
        return True
    elif num1>0 and num2>0:
        return True
    elif num1==0 and num2==0:
        return True
    else:
        return False


# In[18]:


both(6,2)


# In[19]:


both(-1,2)


# In[26]:


#37.cleaning Up Messy Lists
#Create a function that takes a list. This list will contain numbers represented as strings.

#Your function should split this list into two new lists. The first list should contain only even numbers. The second only odd. Then, wrap these two lists in one main list and return it.

#Return an empty list if there are no even numbers, or odd.

#Examples
#clean_up_list(["8"]) ➞ [[8], []]

#clean_up_list(["11"]) ➞ [[], [11]]

#clean_up_list(["7", "4", "8"]) ➞ [[4, 8], [7]]

#clean_up_list(["9", "4", "5", "8"]) ➞ [[4, 8], [9, 5]]


def clean_up_list(lst):
    even = []
    odd = []
    
    for num_str in lst:
        num = int(num_str)
        
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    return [even, odd]



# In[27]:


clean_up_list(["7","8"])


# In[28]:


#38.Valid Variable Names
#When creating variables, the variable name must always start with a letter and cannot contain spaces, though numbers and underscores are allowed to be contained in it also.

#Create a function which returns True if a given variable name is valid, otherwise return False.

#Examples
#variable_valid("result") ➞ True

#variable_valid("odd_nums") ➞ True

#variable_valid("2TimesN") ➞ False

def variable_valid(variable_name):
    return variable_name.isidentifier()


# In[29]:


variable_valid("result")


# In[31]:


variable_valid("2odd_nums")


# In[32]:


#39.In a board game, a piece may advance 1-6 tiles forward depending on the number rolled on a six-sided die. If you advance your piece onto the same tile as another player's piece, both of you earn a bonus.

#Can you reach your friend's tile number in the next roll? Create a function that returns if it's possible to earn a bonus when you roll the die.

#Examples
#possible_bonus(3, 7) ➞ True

#possible_bonus(1, 9) ➞ False

#possible_bonus(5, 3) ➞ False


def possible_bonus(your_tile, friend_tile):
    difference = int(friend_tile - your_tile)
    return 1 <= difference <= 6


# In[33]:


possible_bonus(3,7)


# In[34]:


possible_bonus(1,9)


# In[35]:


#40.Are the Numbers Equal?
#Create a function that takes two integers and checks if they are equal.

#Examples
#is_equal(5, 6) ➞ False

#is_equal(1, 1) ➞ True

#is_equal("1", 1) ➞ False

def is_equal(num1,num2):
    if num1==num2:
        return True
    else:
        return False


# In[36]:


is_equal(5,6)


# In[37]:


is_equal("1", 1)


# In[47]:


#41.Say "Hello" Say "Bye"
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


# In[48]:


say_hello_bye("jose",0)


# In[50]:


#42.Limit a Number's Value
#Create a function that takes three number arguments — one number as an input and two additional numbers representing the endpoints of a closed range — and return the number limited to this range.

#If the number falls within the range, the number should be returned.
#If the number is less than the lower limit of the range, the lower limit should be returned.
#If the number is greater than the upper limit of the range, the upper limit should be returned.
#Examples
#limit_number(5, 1, 10) ➞ 5

#limit_number(-3, 1, 10) ➞ 1

#limit_number(14, 1, 10) ➞ 10

#limit_number(4.6, 1, 10) ➞ 4.6

def limit_number(num,lower_limit,upper_limit):
    if num in range(lower_limit,upper_limit):
        return num
    


# In[51]:


limit_number(5,1,10)


# In[55]:


limit_number(1,-3, 10)


# In[66]:


#43.Hello; Hello World; World
#Write a function that takes an integer and:

#If the number is a multiple of 3, return "Hello".
#If the number is a multiple of 5, return "World".
#If the number is a multiple of both 3 and 5, return "Hello World".
#Examples
#hello_world(3) ➞ "Hello"

#hello_world(5) ➞ "World"

#hello_world(15) ➞ "Hello World"

def hello_world(num):
    if num%3==0 and num%5==0:
        return "Hello World"
    elif num%5==0:
        return "World"
    elif num%3==0 :
        return "Hello"


# In[67]:


hello_world(3)


# In[68]:


hello_world(5)


# In[69]:


hello_world(15)


# In[70]:


#44.Edabit's Markdown Formatting
#Edabit allows for markdown formatting, meaning that it's possible to format words by surrounding text with special characters. For example, to get bold text, you surround the text with double asterisks, like this **bold**.

#Here is a list of the possible formatting options in Edabit and how to apply them:

#**bold**
#_italics_
#`inline code`
#~~strikethrough~~
#Challenge
#Given a string and a style character, return the newly formatted string. Style characters are single letters that represent the different types of formatting.

#For the purposes of this challenge, the style characters are as follows:

#"b" is for bold
#"i" is for italics
#"c" is for inline code
#"s" is for strikethrough
#Examples
#md_format("Bold", "b") ➞ "**Bold**"

#md_format("leaning text", "i") ➞ "_leaning text_"

#md_format("Edabit", "c") ➞ "`Edabit`"

#md_format("That's a strike!", "s") ➞ "~~That's a strike!~~"

def md_format(string, style):
    formatting_symbols = {
        "b": "**",
        "i": "_",
        "c": "`",
        "s": "~~"
    }
    if style in formatting_symbols:
        return formatting_symbols[style] + string + formatting_symbols[style]
    else:
        return string


# In[71]:


md_format("Bold", "b")


# In[72]:


md_format("leaning text", "i")


# In[73]:


md_format("Edabit", "c") 


# In[74]:


md_format("That's a strike!", "s")


# In[75]:


#45.Primitive Darts Game
#Darts is a target game played by throwing feathered darts at a circular board with numbered spaces. Our darts game is the simplest of all games. The score of a single turn is calculated based on the distance from the middle. You need to create a function that takes the dart location as two cartesian coordinates (x, y) and returns a score based on the distance from the middle, aka Bullseye (x=0, y=0).

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


# In[76]:


calculate_dart_score(0,0)


# In[78]:


calculate_dart_score(3, 2)


# In[79]:


#46. Write a function that returns True if a year is a leap, otherwise return False.
#A year is a "leap year" if it lasts 366 days, instead of 365 in a typical year. That extra day is added to the end of the shortest month, creating February 29.
#A leap year occurs every four years, and will take place if the year is a multiple of four. The exception to this is a year at the beginning of a century (for example, 1900 or 2000), where the year must be divisible by 400 to be a leap year.
#Look at the examples, and if you need help, look at the resources panel.
#Examples
#leap_year(1990) ➞ False

#leap_year(1924) ➞ True

#leap_year(2021) ➞ False

def check_for_leap(year):
    if year%4==0:
        return  True
    else:
        return False


# In[81]:


check_for_leap(1990)


# In[87]:


#47.The pH Scale
#Given a pH value, return whether that value is "alkaline" (greater than 7), "acidic" (less than 7), or "neutral" (7). Return "invalid" if the value given is less than 0 or greater than 14.

#Examples
#pH_name(5) ➞ "acidic"

#pH_name(8.7) ➞ "alkaline"

#pH_name(7) ➞ "neutral"

def pH_name(value):
    if float(value)<7:
        return "alkaline"
    elif float(value)==7:
        return "neutral"
    elif float(value) in range(8,15):
        return "acidic"


# In[88]:


pH_name(5)


# In[90]:


pH_name(8)


# In[91]:


#48. Create a function that takes an array of hurdle heights and a jumper's jump height, and determine whether or not the hurdler can clear all the hurdles.
#A hurdler can clear a hurdle if their jump height is greater than or equal to the hurdle height.
#Examples
#hurdle_jump([1, 2, 3, 4, 5], 5) ➞ True

#hurdle_jump([5, 5, 3, 4, 5], 3) ➞ False

#hurdle_jump([5, 4, 5, 6], 10) ➞ True

#hurdle_jump([1, 2, 1], 1) ➞ False

def f1(hurdle_height,jump_height):
    for x in hurdle_height:
        if jump_height<x:
            return True
        else:
            return False


# In[92]:


f1([1,2,3,4,7],jump_height=6)


# In[101]:


#49.What Type of Triangle?
#Create a function which returns the type of triangle, given the side lengths. Return the following values if they match the criteria.

#No sides equal: "scalene"
#Two sides equal: "isosceles"
#All sides equal: "equilateral"
#Less or more than 3 sides given: "not a triangle"
#Examples
#get_triangle_type([2, 6, 5]) ➞ "scalene"

#get_triangle_type([4, 4, 7]) ➞ "isosceles"

#get_triangle_type([8, 8, 8]) ➞ "equilateral"

#get_triangle_type([3, 5, 5, 2]) ➞ "not a triangle"
def get_triangle_type(num1,num2,num3):
    num1=list(num1)
    num2=list(num2)
    num3=list(num3)
    if num1!=num2!=num3:
        return "scalene"
    elif num1==num2 or num2==num3 or num3==num1:
        return "isosceles"
    elif num1==num2==num3:
        return "equilateral"
    else:
        return "not a triangle"


# In[102]:


get_triangle_type([2],[6],[5])


# In[103]:


#50.Capture the Rook
#Write a function that returns True if two rooks can attack each other, and False otherwise.

#Examples
#can_capture(["A8", "E8"]) ➞ True

#can_capture(["A1", "B2"]) ➞ False

#can_capture(["H4", "H3"]) ➞ True

#can_capture(["F5", "C8"]) ➞ False

def can_capture(rooks):
    rook1 = rooks[0]
    rook2 = rooks[1]
    
    if rook1[0] == rook2[0] or rook1[1] == rook2[1]:
        return True
    else:
        return False


# In[104]:


can_capture(["A8", "E8"])


# In[105]:


can_capture(["A1", "B2"])


# In[109]:


#51.How Many Digits?
#Given an integer n. Your task is to find how many digits this integer contains without using str or len methods!

#Examples
#sum_digits(100) ➞ 3

#sum_digits(1000) ➞ 4

#sum_digits(1) ➞ 1

def sum_digits(n):
    count = 0
    if n == 0:
        return 1
    while n != 0:
        count += 1
        n //= 10
    return count


# In[110]:


sum_digits(100)


# In[1]:


#52.Create a function that takes in a two-dimensional list and returns the number of sub-lists with only identical elements.

def count_identical(lst):
    count = 0
    for sub_lst in lst:
        if len(set(sub_lst)) == 1:
            count += 1
    return count


# In[2]:


lst = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]
print(count_identical(lst))


# In[3]:


#53. Create a function that takes a number (from 1 to 12) and returns its corresponding month name as a string. For example, if you're given 3 as input, your function should return "March", because March is the 3rd month.
#Number
#Month Name
#1
#January
#2
#February
#3
#March
#4
#April
#5
#May
#6
#June
#7
#July
#8
#August
#9
#September
#10
#October
#11
#November
#12
#December

#Examples
#month_name(3) ➞ "March"

#month_name(12) ➞ "December"

#month_name(6) ➞ "June"

def get_month_name(month_number):
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    if month_number < 1 or month_number > 12:
        return "Invalid month number"
    else:
        return months[month_number - 1]





# In[4]:


get_month_name(3)


# In[5]:


#54.Little Dictionary
#Create a function that takes an initial word and extracts any words that start with the same letters as the initial word.

#Examples
#dictionary("bu", ["button", "breakfast", "border"]) ➞ ["button"]

#dictionary("tri", ["triplet", "tries", "trip", "piano", "tree"]) ➞ ["triplet", "tries", trip"]

#dictionary("beau", ["pastry", "delicious", "name", "boring"]) ➞ []
#Notes
#If none of the words match, return an empty list.
#Keep the filtered list in the same relative order as the original list of words.

def dictionary(initial_word, words):
    extracted_words = []
    for word in words:
        if word.startswith(initial_word):
            extracted_words.append(word)
    return extracted_words


# In[6]:


dictionary("bu", ["button", "breakfast", "border"]) 


# In[7]:


dictionary("beau", ["pastry", "delicious", "name", "boring"]) 


# In[1]:


#55.Return the Four Letter Strings
#Create a function that takes a list of strings and returns the words that are exactly four letters.

#Examples
#is_four_letters(["Tomato", "Potato", "Pair"]) ➞ ["Pair"]

#is_four_letters(["Kangaroo", "Bear", "Fox"]) ➞ ["Bear"]

#is_four_letters(["Ryan", "Kieran", "Jason", "Matt"]) ➞ ["Ryan", "Matt"]
def is_four_letters(words):
    four_letter_words = []
    for word in words:
        if len(word) == 4:
            four_letter_words.append(word)
    return four_letter_words


# In[3]:


is_four_letters(["Tomato", "Potato", "Pair"])


# In[8]:


#56.Chinese Zodiac
#Create a function that takes a year as an argument and returns the corresponding Chinese zodiac.

#Examples
#chinese_zodiac(2021) ➞ "Ox"

#chinese_zodiac(2020) ➞ "Rat"

#chinese_zodiac(1933) ➞ "Rooster"
#Notes
#The list of animals used can vary slightly, so check the Resources tab for the list that you will need for this challenge.
def chinese_zodiac(year):
    zodiac_signs = {
        0: "Rat",
        1: "Ox",
        2: "Tiger",
        3: "Rabbit",
        4: "Dragon",
        5: "Snake",
        6: "Horse",
        7: "Goat",
        8: "Monkey",
        9: "Rooster",
        10: "Dog",
        11: "Pig"
    }

    zodiac_index = (year - 1900) % 12

    return zodiac_signs[zodiac_index]


# In[9]:


chinese_zodiac(2021) 


# In[ ]:


#57.Chocolate Dilemma
#Two sisters are eating chocolate, whose pieces are represented as subarrays of [l x w].

#Write a function that returns True if the total area of chocolate is the same for each sister.

#To illustrate:

#test_fairness([[4, 3], [2, 4], [1, 2]],
#[[6, 2], [4, 2], [1, 1], [1, 1]])
#➞ True

#// Agatha's pieces: [4, 3], [2, 4], [1, 2]
#// Bertha's pieces: [6, 2], [4, 2], [1, 1], [1, 1]

#// Total area of Agatha's chocolate
#// 4x3 + 2x4 + 1x2 = 12 + 8 + 2 = 22

#// Total area of Bertha's chocolate is:
#// 6x2 + 4x2 + 1x1 + 1x1 = 12 + 8 + 1 + 1 = 22
#Examples
#test_fairness([[1, 2], [2, 1]], [[2, 2]]) ➞ true

#test_fairness([[1, 2], [2, 1]], [[2, 2], [4, 4]]) ➞ false

#test_fairness([[2, 2], [2, 2], [2, 2], [2, 2]], [[4, 4]]) ➞ true

#test_fairness([[1, 5], [6, 3], [1, 1]], [[7, 1], [2, 2], [1, 1]]) ➞ false
#Notes
#N/A


# In[5]:


#58.You FAILEDPASSED the Exam
#Here is a trainwreck of a photo:

#You FAILEDPASSED the Exam Required mark is 85% Your score 85%

#The challenge is to fix all of the bugs in this incredibly messy code, which the code in the image might've actually looked like (probably not)! The code given will output the same middle two lines as in the image shown above.

#First parameter is the user's score.
#Second parameter is the required score.
#Examples
#grade_percentage("85%", "85%") ➞ "You PASSED the Exam"

#grade_percentage("99%", "85%") ➞ "You PASSED the Exam"

#grade_percentage("65%", "90%") ➞ "You FAILED the Exam"
#Notes
#Note that inputs will be given as a string percentage number.
#Maintain all capitalization.
#Feel free to declutter and refactor code if it helps!

def grade_percentage(user_score, required_score):
    user_score = int(user_score[:-1])  
    required_score = int(required_score[:-1]) 

    if user_score >= required_score:
        return "You PASSED the Exam"
    else:
        return "You FAILED the Exam"


# In[6]:


grade_percentage("85%", "85%") 


# In[7]:


grade_percentage("65%", "90%")

