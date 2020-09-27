# Introduction to Python 3 - Day 2

## Short Review

* How to write a function
* How to give a function inputs
* How to return values from a function
* What scope means

## In-Depth Details

<details><summary>Introduction to Functions</summary>
<p>

* A function is a collection of several lines of code
* Calling a function calls all the lines at once
* Functions can be used over and over again
* The __print()__ command is a function

</p>
</details>

<details><summary>What is a Function?</summary>
<p>
	
* To call a function, we use the __function_name()__ syntax
* The brackets make the code inside the function run
* Repeated code is generally more error prone and harder to understand - functions make this easier

```python
def sing_song():
  print("You may say I'm a dreamer")
  print("But I'm not the only one")
  print("I hope some day you'll join us")
  print("And the world will be as one")
  
# call sing_song() below:

sing_song()
sing_song()
```

</p>
</details>

<details><summary>Write a Function</summary>
<p>
	
* To write a function, you must have a heading and indented block of code
* Heading starts with the keyword __def__ and the name of the function followed by brackets
* The indented block of code performs some sort of operation

```python
def greet_customer():
	print("Welcome to Engrossing Grocers")
	print("Our special is mandarin oranges")
	print("Have fun shopping")

greet_customer()
```

* The __def__ keyword tells Python that we are defining a function
* Everything indented after the __:__ is what is run when called

</p>
</details>

<details><summary>Whitespace</summary>
<p>
	
* In Python, the amount of whitespace tells the computer what is part of a function and what is not
* Indentation can be 2 spaces, 4 spaces, a tab or anything else as long as it is consistent

```python
def about_this_computer():
  print("This computer is running on version Everest Puma")
  print("This is your desktop")

about_this_computer()
```

</p>
</details>

<details><summary>Parameters</summary>
<p>
	
* Parameters are variables that you pass into the function when called

```python
def greet_customer(special_item):
	print("Welcome to the Engrossing Grocers")
	print("Our special is " + special_item + ".")
	print("Have fun shopping")
```

* Above, the special_item is referred to as __formal parameter__
* This variable name is a placeholder for the name of the item
* When calling this function, we have to provide a special_item

```python
def greet_customer(special_item):
	print("Welcome to the Engrossing Grocers")
	print("Our special is " + special_item + ".")
	print("Have fun shopping")

greet_customer("peanut butter")	
```

* The item will get printed out in the second print statement
* Values between the brackets are referred to as an __argument__ of the function call
* Argument is the information that is to be used in the execution of the function
* When called, Python assigns the formal parameter name with the actual parameter data

```python
def mult_two_add_three(number):
  print(number*2 + 3)
  
mult_two_add_three(0)
```

</p>
</details>

<details><summary>Multiple Paramters</summary>
<p>
	
* Can have multiple parameters in a function

```python
def mult_x_add_y(number, x, y):
  print(number*x + y)

mult_x_add_y(5, 2 ,3)
mult_x_add_y(1, 3 ,1)
```

</p>
</details>

<details><summary>Keyword Arguments</summary>
<p>
	
* Before, they were called __positional arguments__
* Can also pass these arguments as __keyword arguments__ where we refer to what each argument is assigned to in the function call
* Can use keyword arguments to make it explicit what each argument should refer to in the body
* Also define default arguments for a function using syntax very similiar to keyword argument syntax but used during the function definition
* If function is called WITHOUT an argument for that parameter, it relies on the default
* Once you give an argument a default value, no arguments that follow can be used positionally

```python
# Define create_spreadsheet():
def create_spreadsheet(title, row_count = 1000):
  print("Creating a spreadsheet called "+ title + " with " + str(row_count) + " rows")

# Call create_spreadsheet() below with the required arguments:
create_spreadsheet(title="Applications", row_count=10)
```

</p>
</details>

<details><summary>Returns</summary>
<p>
	
* Functions can also return a value to the user so the value can be modified or used later
* When there is a result from a function that can be stored in a variable, it is called a __returned function value__
* Use the keyword __return__ 

```python
def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age
  
my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)
print("I am "+str(my_age)+" years old and my dad is "+str(dads_age)+" years old")
```

</p>
</details>

<details><summary>Multiple Return Values</summary>
<p>
	
* Can return several values by seperating them with a comma

```python
def square_point(x_value, y_value):
	x_2 = x_value * x_value
	y_2 = y_value * y_value
	return x_2, y_2
```

* This function takes in an x value and a y value and returns them both, squared
* Get the values by assinging them both to variables when calling the funciton

```python
x_squared, y_squared = square_point(1,3)
print(x_squared)
print(y_squared)
```

```python
def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = margin + target
  return low_limit, high_limit

low, high = get_boundaries(100, 20)

```
</p>
</details>

<details><summary>Scope</summary>
<p>
	
* Variables defined inside the function do not exist outside the function
* Call these parts of a program where variables can be accessed the __scope__
* Variables defined outside the scope of a function may be accessible inside the body of the function

```python

header_string = "Our special is "

def create_special_string(special_item):
	return header_string + special_item + "."

print(create_special_string("grapes"))
```

* No error is produces as the header_string can be used inside the function because the scope is the whole file

```python

current_year = 2048

def calculate_age( birth_year):
  age = current_year - birth_year
  return age
  
print(calculate_age(1970))


```
</p>
</details>

<details><summary>Review</summary>
<p>
	
```python
def repeat_stuff(stuff, num_repeats=10):
  return stuff*num_repeats

lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)

print(song)
```

</p>
</details>
