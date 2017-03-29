# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists are mutable; you can add, delete, and change items. Tuples are not; once created, they
can only be changed if you reassign the tuple's name to a different tuple. Only tuples will work
as keys in dictionaries, since dictionary keys cannot be mutable (for a complicated reason involving
hashing that my roommate explained to me).

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists are organized by index, whereas sets are organized by hash (and look random to
the casual observer, i.e., me). If you want to list countries in order of population,
a list would be the way to go, since order is important. Because they're hashed, sets are
good to use to eliminate duplicates (since duplicates will always hash the same) and to look things
up quickly; performance is much faster for a set because the hash will point to a certain
spot in the set rather than a list having to go through every index spot.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is a way of defining a function. It's used when you want a (usually temporary)
way to write a function as an expression (e.g., to assign it to a variable). So, for
instance, you can use it to sort a list of names by last name:

>> names = ['James Livingston', 'Jon Greenberg', 'Ariana Strong', 'Dora Brent', 'Alex Bradford']
>> names.sort(key = lambda x: x.split()[1])
>> print(names)

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> A list comprehension is to a for loop as lambda is to a function. It's a simplified
way of creating a list; instead of a loop, it's just one expression. For example, you can make a list this way with a for loop:

>> numbers = []
>> for i in range(30):
>>     numbers.append(i)

>> And then you can make a list of the squares using list comprehension:

>> squares = [i**2 for i in numbers]

>> Or by using map:

>> def square(x):
>>     return x**2

>> squares = list(map(square, numbers)

>> If we want to make another list consisting of the even numbers, we can use filter:

>> def even(x):
>>     return x % 2 == 0

>> evens = list(filter(even, numbers))

>> Or, again, list comprehension:

>> evens = [i for i in numbers if i % 2 == 0]

>> So list comprehensions can do the same things as map and filter, but usually with less syntax.
>> Set comprehension is the same thing as list comprehension but with sets (duh). For example:

>> name = 'zoegreenjacobson'
>> vowels = 'aeiou'
>> consonants = set(i for i in name if i not in vowels)

>> And here's an example of dictionary comprehension:

>> BMGapplicants = {'jon':70, 'james':69, 'jeremiah':77, 'jules':72.5}
>> eligibles = {i:j for i,j in BMGapplicants.items() if 70<=j<=73}
---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7,850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
