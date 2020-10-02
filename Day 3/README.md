# Introduction to Python 3 - Day 3

<img src="https://github.com/ComplexSec/learn-python3/blob/master/images/python6.png">


## Short Review

* Boolean expressions are statements that can be TRUE or FALSE
* A boolean variable is a varaible that is set to either True or False
* You can create boolean expressions using relational operators
	* Equals (==)
	* Not equals (!=)
	* Greater than (>)
	* Greater than or equal to (>=)
	* Less than (<)
	* Less than or equal to (<=)

* If statements can be used to create control flow
* Else statements can be used to execute code when conditions of an __if__ statement are NOT met
* Elif statements can be used to build additional checks into your if statements
* Try and Except statements can be used to build error control into your code


## In-Depth Details

<details><summary>Control Flow Introduction</summary>
<p>
	
* In Python, your script executes from the top down
* Programmers job to include gateways (conditional statements) to tell the PC when it should execute certain blocks

</p>
</details>

<details><summary>Boolean Expressions</summary>
<p>
	
* To build control flow into a program, you need to be able to check if something is TRUE or FALSE
* A boolean expression is a statement that can either be TRUE or FALSE
* 

</p>
</details>

<details><summary>Relation Operators: Equals and Not Equals</summary>
<p>
	
* __Relation Operators__ compare two items and return either
* Sometimes called __comparators__
* Two boolean operators are __==__ and __!=__
* These operators compare two items and return TRUE or FALSE
* Can create boolean expressions by comparing two values using these operators
* Comparing strings and integers will return boolean FALSE

</p>
</details>

<details><summary>Boolean Variables</summary>
<p>
	
* True and False are there own special type (__bool__)
* Any variable that is assigned one of these values is called a __boolean variable__
* Boolean variables can be created in several ways
* Easiest way is to simply assign True or False to a variable
* Can also set a variable equal to a boolean expression


```python
my_baby_bool = "true"

print(type(my_baby_bool))

my_baby_bool_two = True

print(type(my_baby_bool_two))
```

</p>
</details>

<details><summary>If Statements</summary>
<p>
	
* Form of a conditional statement is as follows:

```python
if is_raining:
	bring_umbrella()
```

* The colon tells the computer that what is coming next is what should be executed if the condition is met

```python
def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"
  if user_name == "angela_catlady_87":
    return "I know it is you Dave! Go away!"

  
# Enter a user name here, make sure to make it a string
user_name = "Dave"

print(dave_check(user_name))
```
</p>
</details>

<details><summary>Relation Operators 2</summary>
<p>
	
```python
def age_check(age):
	if age >= 13
	return True
```

* This function takes the users age and compares it to the number 13
* If __age__ is greater than or equal to 13, it returns TRUE

```python
def greater_than(x,y):
  if x > y:
    return x
  if y > x:
    return y
  if x == y:
    return "These numbers are the same"

def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"

print(graduation_reqs(120))
```
</p>
</details>


<details><summary>Boolean Operators: and</summary>
<p>
	
* Often, the conditions you want to check in your conditional statement require more than one boolean expression
* In these cases, you can build larger boolean expressions using __boolean operators__
* These operators combine smaller boolean expressions into larger ones
* Three boolean operators to cover:
	* and
	* or
	* not

* AND combines two boolean expressions and evaluates as True if both its components are True but False otherwise

```python
statement_one = False

statement_two = True

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
```

</p>
</details>

<details><summary>Boolean Operators: or</summary>
<p>
	
* The boolean operator __OR__ combines two expressions into a larger expression that is True if either component is True

```python
statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

def graduation_mailer(gpa, credits):
  if (gpa >= 2.0) or (credits >= 120):
    return True
```

</p>
</details>

<details><summary>Boolean Operators: not</summary>
<p>
	
* When NOT operator is applied to any boolean expression, it reverses the boolean value
* If we have a TRUE statement and apply a NOT operator, we get a FALSE statement
* In Python, the __not__ operator is applied at the very beginning of the statement

```python
not True == False
not False == True
```

```python
statement_one = False

statement_two = True

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if not (gpa >= 2.0) and not (credits >= 120):
    return "You do not meet either requirement to graduate!"
```
</p>
</details>

<details><summary>Else Statements</summary>
<p>
	
* Else statements allow us to elegantly describe what we want our code to do when certain conditions are NOT met
* Else statements always appear in conjunction with if statements

```python
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."
```
</p>
</details>

<details><summary>Else If Statements</summary>
<p>
	
* An elif statement checks another condition after the previous if statement conditions are not met
* Can use elif statements to control the order we want the program to check each of our conditional statements
* First, the if statement is checked, then each elif statement is checked from top to bottom
* Then, finally, the else code is executed if none of the previous conditions have been met

```python
def grade_converter(gpa):
  grade = "F"
  
  if gpa >= 4.0:
    grade = "A"
  elif gpa >= 3.0:
    grade = "B"
  elif gpa >= 2.0:
    grade = "C"
  elif gpa >= 1.0:
    grade = "D"
    
  return grade
```

</p>
</details>

<details><summary>Try and Except Statements</summary>
<p>
	
* Can use try and except statements to check for possible errors a user might encounter
* General syntax of a try and except statement is

```python
try:
	# some statement
except ErrorName:
	# some statement
```

* First, the statement under __try__ will be executed
* If at some point an exception is raised during this execution, such as a NameError or a ValueError and that exception matches the keyword in the except statement, then the try statement will terminate and except will execute

```python
def raises_value_error():
  raise ValueError

try:
  raises_value_error()
except ValueError:
  print("You raised a ValueError!")
```

</p>
</details>

<details><summary>Review Code</summary>
<p>
	
```python
def applicant_selector(gpa, ps_score, ec_count):
  if (gpa >= 3.0) and (ps_score>= 90) and (ec_count >= 3):
    return "This applicant should be accepted."
  elif (gpa >= 3.0) and (ps_score >= 90) and not (ec_count >= 3):
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."
```

</p>
</details>
