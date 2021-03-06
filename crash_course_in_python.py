# A crash course in Python

import this  # Zen of Python

# Whitespace Formatting

for i in [1, 2, 3, 4, 5]:
    print(i)
    for j in [1, 2, 3, 4, 5]:
        print(j)
        print(i + j)
    print(i)
print('done looping')

# using backslash to denote that the statement continues onto the next line.
two_plus_three = 2 + \
                 3
print(two_plus_three)

# Modules

import re
my_regex = re.compile("[0-9]+", re.I)
print(type(my_regex))

# If you already have an "re" we can use an alias.
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

# these functions/values can be used without qualifications
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

match = 10
from re import *
print(match)

# Functions
# Python functions are first class. So a function can be
# assigned to a variable.

# Example
def double(x):
    return 2*x

# function has been assigned to a variable
my_double = double

# now the above variable can be used to call the function
my_double(14)  # ans: 28

# we can even pass a function, another function as a parameter
def apply_to_one(function, value):
    '''

    :param function: a function which takes value as a parameter
    :param value:
    :return:
    '''
    return function(value)

apply_to_one(my_double, 14)  # ans: 28


# It is also easy to create short anonymous function called lambda
apply_to_one(lambda x: x*2, 14)  # ans: 28
apply_to_one(lambda x: x**2, 14)  # ans: 196

# Even we can assign lambdas to variables. But it is not recommended
another_double = lambda x: x*2  # don't do this
another_double(12)  # ans: 24

# Functions can even have default parameters.
def my_print(message = "my default message"):
    print(message)

my_print("Hello world")
my_print()

# It is sometimes useful to specify arguments by name
def subtract(a = 0, b = 0):
    return a - b

subtract(5, 4)
subtract(0, 5)
subtract(b = 5)

# Strings
#backslash is used to encode special characters
tab_string = "\t"
print(tab_string)
print(len(tab_string))

# we can create raw strings in python using r""
not_tab_string = r"\t"
print(not_tab_string)
print(len(not_tab_string))

# if raw string symbol r"" is not used, another backslash needs to be used
raw_string_not_used = "\\t"
print(raw_string_not_used)
print(len(raw_string_not_used))

# We can create multiline strings using triple-double-quotes
mutli_line_string = """This is the first line
and this is the second line
and this is the third line
"""

mutli_line_string_single = '''This is the first line
and this is the second line
and this is the third line
'''

print(mutli_line_string)
print(mutli_line_string_single)

# Exceptions
try:
    print(0/0)
except ZeroDivisionError:
    print("cannot divide by zero")

# Lists
# list is nothing but an array(as in other languages) but
# with some additional functionalities

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [[], integer_list, heterogeneous_list]

list_length = len(integer_list)
list_sum = sum(integer_list)

# we can get the nth element of a list with square brackets.
x = list(range(10))
print(x)
# an element in a list can be fetched as well as arranged
# using the square brackets
x[0] = -1
print(x)

# We can even use square brackets to slice the elements in a list
print(x)
x[:3]
x[3:]
x[1:5]
last_three = x[-3:]
print(last_three)
without_first_and_last = x[1:-1]
print(without_first_and_last)

# difference between shallow copy and deep copy
copy_of_x = x[:]
another_copy_of_x = x
copy_of_x[1] = -2
print(copy_of_x)
print(x)
another_copy_of_x[1] = -99
print(another_copy_of_x)
print(x)

# Python has in operator to check for list membership.
x = list(range(10))
1 in [1, 2, 3]  # ans: True
0 in [1, 2, 3]  # ans: False

# concatenating lists toghether.
x = [1, 2, 3]
x.extend([4, 5, 6])
x

["a", "b", "c"] + ["d", "e", "f"]
[2, 3, 4] + [5, 6, 7]

y = [2, 3, 4]
# use of extend modifies the original list
y.extend([9, 5, 4])
y

# If list should not be modified, list addition can be used
x = [1, 2, 3]
y = x + [4, 5, 6]
print(x)
print(y)

# Most of the time we will append to lists one at a time.
x = [1, 2, 3]
x.append(0)
print(x)

# insert is used to insert an item at a particular place in a list
x.insert(0, 0)
print(x)

x = [1, 2, 3]
x.append(0)
y = x[-1]
z = len(x)

# unpacking lists

# we will get ValueError if we don't have same number of elements on both sides
x, y = [1,2]

# It is common to use _ for a value you're going to throw away
_, y = [1,2]

# Tuples
# Tuples are lists immutable cousins. Immutable means "can't be modified"

my_list = [1,2]
my_tuple = (1,2)
other_tuple = 3, 4
print(other_tuple)
print(type(other_tuple))
another_tuple = 3, 4, 5, 6
print(another_tuple)
print(type(another_tuple))
my_list[1] = 3
print(my_list)

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")

# Tuples are a convienient way to return multiple values from functions:
def sum_and_product(x,y):
    return (x+y),(x*y)

sp = sum_and_product(2,3)
print(sp)
print(type(sp))

s, p = sum_and_product(5, 10)
print(s, type(s))
print(p, type(p))

# Tuples and lists can be used for multiple assignments:
x, y = 1, 2
x, y = y, x

# Dictionaries:
# Associates values with keys and allows you to quickly retrieve the value
# corresponding to a given key:

empty_dict = {}
empty_dict2 = dict()

grades = {"Joel" : 80, "Tim" : 95}
print(grades, type(grades))

# To get a value using key
joels_grade = grades["Joel"]

# But you'll get a KeyError if you ask for a key that is not in the dictionary:
try:
    grades["Karvendhan"]
except KeyError:
    print("No grade for Karvendhan!")

for key, value in grades.items():
    print(key, value)

# you can check for the existence of the key using in
karvendhan_has_grade = "Karvendhan" in grades
joel_has_grade = "Joel" in grades
print(joel_has_grade)

# Dictionaries have a get method that returns a default value (instead of raising an exception)
# when you look up a key that's not in the dictionary.

# 0 is the default value returned when Key doesn't match
grades.get("Joel", 0)

# 0 is the default value returned when Key doesn't match
grades.get("Kate", 0)

# default default is None
grades.get("No One")

# You assign the key-value pairs using the same square brackets
grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)
print(num_students)  # ans: 3

# Now Kate will have a grade
grades.get("Kate")

# We will frequently use dictionary as a simple way to represent structured data.
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet.get("hashtags")

tweet_keys = tweet.keys()
print(tweet_keys, type(tweet_keys))
tweet_values = tweet.values()
print(tweet_values, type(tweet_values))
tweet_items = tweet.items()
print(tweet_items, type(tweet_items))

"user" in tweet_keys  # uses  slow dict in
"user" in tweet  # uses fast dict in Pythonic
"joelgrus" in tweet_values

"user" in tweet_items
("user", "joelgrus") in tweet_items

# dictionary keys are immutable # we can't use lists as keys in the dictionary
# however a tuple can be used as a key in the dictionary.

# defaultdict
# Calculating the number of words in a document by using words as "key"
# and using count as "values".

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

word_counts = {}
for word in "forgiveness in better than permission".split():
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

print(word_counts)

# Third approach is to use .get method of the dictionary.
# It behaves really gracefully

word_counts = dict()
for word in "forgiveness is better than permission than".split():
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

print(word_counts)

from collections import defaultdict
word_counts = defaultdict(int)
for word in "forgiveness is better than permission than".split():
    word_counts[word] += 1

print(word_counts)

# default dict can be useful with list or dict or even your own functions
dd_list = defaultdict(list)
dd_list[2].append(1)
print(dd_list[2])

dd_dict = defaultdict(dict)
dd_dict[2]["mani"] = 4
print(dd_dict[2])

dd_dict["joel"]["city"] = "Seattle"
print(dd_dict["joel"])

dd_pair = defaultdict(lambda : [0, 0])
print(dd_pair, type(dd_pair)
dd_pair[2][1] = 1
print(dd_pair)

# Counter
# Counter turns a sequence of values into defaultdict(int)-like object
# mapping keys to counts. We will primarily use it to create histograms.

from collections import Counter
Counter((1,2,1,3,4,3,4))
c = Counter([0, 1, 2, 0])

# counting words in a document becomes ridiculously easy here
word_counts = Counter("forgiveness is better than permission than".split())
print(word_counts)

# most_common is very important when we use the Counter.
for word, count in word_counts.most_common(2):
    print(word, count)

# Sets
# A data structure which represents a collection of distinct elements.
s = set()
print(s, type(s))
s.add(1)
# set s has been modified now
print(s)
s.add(2)
# again set s has been modified
print(s)
s.add(2)
print(s)
print(len(s))
2 in s
3 in s

"""
sets are used for 2 main reasons.
1) "in" is a very fast operation on sets
2) to find the distinct items in a collection
"""

stopwords_list = ["a", "an", "at", "yet", "you", "has", "zip", "hasn't", "been", "make", "make", "a", "yet", "zip"]
"zip" in stopwords_list
"zip" in set(stopwords_list)

item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)
item_set = set(item_list)
num_distinct_items = len(item_set)
print(num_distinct_items)
print(item_set)
distinct_item_list = list(item_set)
print(distinct_item_list)

# Control Flow

if 1 > 2:
    message = "if only 1 were greater than 2"
elif 1 > 3:
    message = "elif stands for else if"
else:
    message = "when all else fails use else(if you want to)"
print(message)
'''
4%2 - remainder
4//2  - quotient
'''

# we can also write a ternary if-then-else on one line, used occasionally.
parity = "even" if 4%2 == 0 else "odd"
print(parity)

# Python has a while loop
x = 0
while x < 10:
    print(x, "is less than 10")
    x += 1

for x in range(10):
    print(x, "is less than 10")

# If you need more-complex logic, you can use continue and break:
for x in range(10):
    if(x == 3):
        continue
    if(x == 5):
        break
    print(x)

# Truthiness
# Booleans are captialized in python

one_is_less_than_two = 1 < 2
print(one_is_less_than_two)
true_equals_false = True == False
print(true_equals_false)

# Python uses None to indicate Nonexistent value
x = None
print(x == None)  # Not Pythonic
print(x is None)  # Pythonic

"""
Python lets you use any value where it expects a Boolean. 
The following are all "Falsy".

1) False
2) None
3) [] (an empty list)
4) {} (an empty dict)
5) ""
6) set()
7) 0
8) 0.0

Pretty much everything else is treated as True. This allows you to easily use if 
statement to test for empty lists or empty strings or empty dictionaries and so on.

"""

import random
def return_a_string():
    decide_factor = random.choice(range(10))
    if decide_factor > 5:
        return "John Doe"
    else:
        return ""

for i in range(10):
    s = return_a_string()
    if s:
        first_char = s[0]
    else:
        first_char = ""
    print("character: ",first_char)

# A Simpler way of doing the same is:
def return_a_string():
    decide_factor = random.choice(range(10))
    if decide_factor > 5:
        return "John Doe"
    else:
        return ""

s = return_a_string()
# looks like intersection is going on with the use of and
first_char = s and s[0]

def return_a_number():
    decide_factor = random.choice(range(10))
    if decide_factor > 5:
        return 5
    else:
        return None

x = return_a_number()
safe_x = x or 0

# Difference between all and any function.
all([True, 1, {3}])
all([True, 1, {}])
any([True, 1, {}])
any([]) # False, no truthy elements in the list
all([]) # True, no falsy elements in the list
all([True, 1, []])

# The Not so Basics
# little more advanced Python features

# Sorting
# Every Pyhton list has a sort method that sorts the list in its place. If you
# don't want to mess up your list, you can use the sorted function, which returns a new list
x = [4, 1, 2, 3]
# the original list x has been modified
x.sort()
print(x)
# If you don't want the list to be modified use sorted.
x = [4, 1, 2, 3]
y = sorted(x)
print(x)
print(y)

x = [4, 1, 2, 3]
sorted(x,reverse = True)
x.sort(reverse = True)
print(x)

# Instead of naively comparing one element with another, we can compare the results of a
# function
x = [-4, 1, -2, 3]
sorted(x)  # ans: [-4, -2, 1, 3]
# comparing the elements using a function
sorted(x, key=abs)  # ans: [1, -2, 3, -4]
sorted(x, key=abs, reverse = True)  # ans: [-4, 3, -2, 1]

document = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. " \
           "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, " \
           "when an unknown printer took a galley of type and scrambled it to make a type specimen book. " \
           "It has survived not only five centuries, but also the leap into electronic typesetting, " \
           "remaining essentially unchanged. It was popularised in the 1960s with the release of " \
           "Letraset sheets containing Lorem Ipsum passages, and more recently with desktop " \
           "publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# count the number of words in the document
from collections import Counter
word_counts = Counter(document.lower().split())
print(type(word_counts), word_counts) # Looks like Counter can be used just like a dictionary

import operator
print(word_counts)
sorted(word_counts.items(), key = operator.itemgetter(1), reverse = True)

# List Comprehensions
# Frequently, you'll want to transform a list into another list,
# by choosing only certain elements, or by transforming elements,
# or both. The Pythonic way of doing this is list comprehensions.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list into another list, by choosing only certain elements
[i for i in lst if i > 5]

even_numbers = [x for x in range(10) if x%2 == 0]
print(even_numbers)  # ans:  [0, 2, 4, 6, 8]
squares = [x*x for x in range(6)]
print(squares)  # [0, 1, 4, 9, 16, 25]
even_squares = [x*x for x in range(10) if x%2 == 0]
print(even_squares)

# Turning lists into dictionaries or sets
# dict comprehensions
square_dict = {x:x*x for x in range(6)}
print(square_dict)  # ans: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(square_dict.keys())  # ans: dict_keys([0, 1, 2, 3, 4, 5])
print(square_dict.values()) # ans: dict_values([0, 1, 4, 9, 16, 25])

# Set comprehensions
square_set = {x*x for x in range(6)}
print(square_set)  # ans: {0, 1, 4, 9, 16, 25}

# if you don't need the value from the list, it's conventional
# to use an underscore as the variable.

zeroes = [0 for _ in even_numbers]
print(zeroes)  # ans: [0, 0, 0, 0, 0]

# A list comprehension can include multiple fors:

pairs = [(x, y)
         for x in range(10)
         for y in range(10)
         ]
print(pairs)

increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x+1, 10)
                    ]

print(increasing_pairs)

# List comprehensions are used almost everywhere

# Generators and Iterators
# A generator is something that you can iterate over
# but whose values are produced only as needed(lazily).

# creating a generator
def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in lazy_range(10000):
    print(i)
    if i == 2135:
        break

# In python 3 range itself is lazy. So we can create infinit sequence
def natural_numbers():
    i = 1
    while True:
        yield i
        i += 1

lazy_evens_below_20 = (x for x in lazy_range(20) if x % 2 == 0)
print(lazy_evens_below_20)  # output: <generator object <genexpr> at 0x00000159BF195258>
print(list(lazy_evens_below_20))  # output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Randomness
import random

# random.random() produces numbers uniformly between 0 and 1
four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)  # [0.9959300131135868, 0.9672660103214821, 0.323568384329169, 0.5024164052421923]

random.seed(10)  # for reproducible random numbers
print(random.random())  # output: 0.5714025946899135

random.randrange(10)  # range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.randrange(3, 10)  # range = [3, 4, 5, 6, 7, 8, 9]

up_to_ten = list(range(10))
random.shuffle(up_to_ten)
print(up_to_ten)

# if you need to pick one element from a list you can use random.choice
my_best_friend = random.choice(["Alice", "Bob", "Charlie", "Debie"])
print(my_best_friend)  # output: Bob

# randomly choose a sample of elements without replacement, we can use random.sample()
lottery_numbers = range(60)
random.sample(lottery_numbers, 6)  # output: [38, 22, 24, 26, 18, 52]

# To randomly choose a sample of elements with replacement, we can use random.choice()
[random.choice(range(10)) for _ in range(4)]  # output: [9, 0, 3, 2]


# Regular Expressions
# They provide a way of searching text.

import re

print(re.match("a", "cat"))  # output: None
print(not re.match("a", "cat"))  # output: True (as None is considered to be False in Python)
re.search("a", "cat")
not re.search("c","dog")
len(re.split("[ab]", "carbs")) == 3
"R-D-" == re.sub("[0-9]", "-", "R2D2")  # replace digits with dashes

print(all([not re.match("a", "cat"), re.search("a", "cat"), not re.search("c","dog"), \
           len(re.split("[ab]", "carbs")) == 3, "R-D-" == re.sub("[0-9]", "-", "R2D2")]))










































































