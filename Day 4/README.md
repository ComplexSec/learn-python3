# Introduction to Python 3 - Day 3

<img src="https://github.com/ComplexSec/learn-python3/blob/master/images/python7.webp">

## Short Review

* How to create a list
* How to create a list of lists using zip
* How to add elements to a list using either .append() or +
* How to use range to create list of integers

## In-Depth Details

<details><summary>What Is A List?</summary>
<p>
	
* A list is an ordered set of objects in Python
* In Python, we can create a variable called `heights` to store the height of various people

```python
heights = [61, 70, 67, 64]
```

* A list begins and ends with a square bracket
* Each item is separated by a comma
* It is considered good practice to insert a space after each comma

</p>
</details>

<details><summary>Lists II</summary>
<p>
	
* Lists can contain more than just numbers - can include names for example

```python
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
```

* Can combine multiple data types in one list

```python
ints_and_strings = [1, 2, 3, 'four', 'five', 'six']

sam_height = ['Sam', 67]
```

</p>
</details>

<details><summary>List of Lists</summary>
<p>
	
* Lists can contain other lists

```python
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]
```

</p>
</details>

<details><summary>Zip</summary>
<p>

* Suppose we already had a list of names a list of heights

```python
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 65]
```

* If we wanted to create a list of lists that paired each name with a height, we could use the command `zip`
* Zip takes two or more lists as inputs and returns an object that contains a list of pairs
* Each pair contains one element from each of the inputs

```python
names_and_heights = zip(names, heights)
print(names_and_heights)
```

* You won't see much about the object from printing it because it will return the location of this object in memory
* To see the nested lists, you can convert the zip object to a list first

```python
print(list(names_and_heights))
```

```python
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']
names_and_dogs_names = zip(names, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)
```
</p>
</details>

<details><summary>Empty Lists</summary>
<p>
	
* A list doesn't have to contain anything
* Create an empty list via `empty_list = []`
* Creating an empty list allows us to plan to fill it later

</p>
</details>

<details><summary>Growing a List: Append</summary>
<p>
	
* Can add a single element to a list using `.append()`
* Can add the element 1 by using the following command

```python
empty_list.append(1)
```

* When using `.append()` on a list that already has elements, the new element is added to the end of it

```python
orders = ['daisies', 'periwinkle']

print(orders)

orders.append('tulips')
orders.append('roses')

print(orders)
```

</p>
</details>

<details><summary>Growing a List: Plus</summary>
<p>
	
* When we want to add multiple items to a list, use the `+` to combine two lists

```python
items_sold_new = items_sold + ['biscuit', 'tart']
print(items_sold_new)
```

* In this example, we created a new variable which contained both original items and new ones
* Can inspect the original and see it did not change
* Can only use `+` with other lists
* If you want to add a single element using `+`, put it in square brackets

```python
orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

# Create new orders here:

new_orders = orders + ['lilac', 'iris']

broken_prices = [5, 3, 4, 5, 4] + [4]
```
</p>
</details>

<details><summary>Range I</summary>
<p>
	
* Often, we want to create a list of consecutive numbers
* Python gives us an easy way of creating lists using a function called `range`
* The `range` function takes a single input and generates numbers starting at 0 and ending at the number before the input

```python
my_range = range(10)
```

* This generates numbers from 0 to  9
* Just like with `zip`, the `range` function returns an object that we can convert into a list

</p>
</details>

<details><summary>Range II</summary>
<p>
	
* Can use range to generate more interesting lists
* By default range creates a list starting at 0
* Can call range with two arguments to create a list that starts at a different number

```python
my_list = range(2,9)
print(list(my_list))
```

* With one or two arguments, `range` will create a list of consecutive numbers
* If using a third argument, it creates a list that skips numbers

```python
my_range2 = range(2, 9, 2)
print(list(my_range2))
```

* This prints out each number 2, 4, 6, 8

```python
list1 = range(5, 15, 3)
list2 = range(0, 40, 5)
```

</p>
</details>

<details><summary>Review</summary>
<p>

```python
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']

age = []
age.append(42)

all_ages = [32, 41, 29] + age
name_and_age = zip(first_names, all_ages) 

ids = range(4)
```
</p>
</details>