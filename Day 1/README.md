# Introduction to Python 3 - Day 1

<img src="https://github.com/ComplexSec/learn-python3/blob/master/images/python4.png">

## Short Review

* Printed messages 
* Stored values in variables
* Updated variables
* Performed arithmetic
* Error handling

## In-Depth Details

<details><summary>Comments</summary>
<p>
	
* Text written in a program is called a __comment__
* Python interprets anything after a __#__ as a comment
* Comments can
	* provide context for why something is written
	* help other people understand faster
	* ignore a line of code and see how it runs without it

```python
# This is a comment in Python 3
```
</p>
</details>

<details><summary>Print</summary>
<p>
	
* The __print()__ function is used to tell a computer to talk
* Message MUST be surrounded by quotes

```python
print("There is something at work in my soul, which I do not understand.")
```

* The printed words are referred to as __output__
</p>
</details>

<details><summary>Strings</summary>
<p>

* Programmers refer to blocks of text as __strings__
* Double quotes or single quotes define a string

```python
print("JJ")
print('JJ')
```
	
</p>
</details>

<details><summary>Varaibles</summary>
<p>

* Variables are a method of storing data for reuse
* Variables assigned using the __=__ sign

```python
mesage_string = "Hello there"

# Prints "Hello there"
print(mesage_string)
```	

* This stores the message in a variable called message_string
* Variables are NOT allowed spaces or symbols in their names other than an underscore
* They cannot begin with numbers
* Can update a variable

```python
# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = "bacon roll"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner
meal = "chicken fajitas"

# Printing out dinner
print("Dinner:")
print(meal)

```

</p>
</details>

<details><summary>Errors</summary>
<p>
	
* Python refers to mistakes as __errors__ and will point to the location where it happened via the __^__ symbol
* Two common errors are __SyntaxError__ and __NameError__
* __SyntaxError__ means there is something wrong with the way it is written (wrong punctuation, command in wrong place, missing brackets, etc...)
* __NameError__ occurs when the interpreter sees a word it does not recognize


</p>
</details>

<details><summary>Numbers</summary>
<p>
	
* An integer (__int__) is a whole number - no decimal pointsand contains all numbers including negative and the number 0
* A floating-point number (__float__) is a decimal number - used to represent fractional quantities as well as precise measurements

```python
an_int = 2
a_float = 2.1

print(an_int + 3)
```

</p>
</details>


<details><summary>Calculations</summary>
<p>
	
* Python performs addition, subtraction, multiplication and division (__+__, __-__, __*__, __/__)
* Python 3 converts all ints to floats before a division

```python
print(573 - 74 + 1)
print(25 * 2)
print(10 / 5)
```	

* If dividing by zero, you will get a __ZeroDivisionError__
</p>
</details>

<details><summary>Changing Numbers</summary>
<p>

* Two variables can be added together, divided by 2 and multiplied by a third value without Python distinguishing between the varaibles and literals
* Performing arithmetic on variables does not change the variable
* Only update a variable using the __=__ sign

```python
coffee_price = 1.50
number_of_coffees = 4

print(coffee_price * number_of_coffees)
print(coffee_price)
print(number_of_coffees)

coffee_price = 2.00

print(coffee_price * number_of_coffees)
print(coffee_price)
print(number_of_coffees)
```
	
</p>
</details>

<details><summary>Exponents</summary>
<p>
	
* To do exponentiation in Python, we use double asterisks

```python
print(2 ** 10)
print(8 ** 2)
print(9 ** 3)
print(4 ** 0.5)
```

</p>
</details>

<details><summary>Modulo</summary>
<p>
	
* Modulo is indicated by __%__
* Modulo gives the remainder of a division - if number is divisible, the output will be 0

```python
print(29 % 5) # Prints 4
print(32 % 3) # Prints 2
print(44 % 2) # Prints 0
```

* Modulo is useful when we want to perform an action every nth-time the code is run

</p>
</details>

<details><summary>Concatenation</summary>
<p>
	
* The __+__ operator can add two strings - called concatenation
* Performing concatenation creates a brand new string

```python
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text

print(full_text)
```

* To add a space between the two, use the concatenation method

```python
full_text = greeting_text + " " + question_text
```

* To concatenate a string with a number, you need to make the number a string using the str() function
* If trying to print a numeric variable, use commas to pass it as a different argument

```python
birthday_string = "I am "
age = 24
birthday_string_2 = " years old"

full_birthday_string = birthday_string + str(age) + birthday_string_2

print(full_birthday_string)
print(birthday_string, age, birthday_string_2)
```

* Using str(), you can convert variables that are not strings to strings and concatenate them
* Do not need to convert a number for it to be an argument to a print statement

</p>
</details>

<details><summary>Plus Equals</summary>
<p>
	
* Python has a shorthand for updating variables (__+=__)

```python
number_of_miles = 12
number_of_miles += 2
print(number_of_miles) # Prints 14
```

* Plus equals operator can be used for string concatenation

```python
hike_caption = "What an amazing time to walk through nature!"
hike_caption += "#nofilter"
hike_caption += "#blessed"
```

</p>
</details>

<details><summary>Multi-Line Strings</summary>
<p>
	
* If you try to create a string that occupies multiple lines, it will produce a __SyntaxError__
* Python offers multi-line strings via the __"""__ or __'''__ operators

```python
leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""
```
 
</p>
</details>
