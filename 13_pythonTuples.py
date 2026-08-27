# 🐍 Python Tuples

A **tuple** is an ordered collection of elements in Python.

The main difference between a tuple and a list is that **tuples are immutable**, meaning their elements cannot be changed after the tuple is created.

```python
numbers = (10, 20, 30, 40)
```

---

## 📌 Table of Contents

* [Creating Tuples](#-creating-tuples)
* [Tuple Characteristics](#-tuple-characteristics)
* [Accessing Tuple Elements](#-accessing-tuple-elements)
* [Negative Indexing](#-negative-indexing)
* [Tuple Slicing](#-tuple-slicing)
* [Tuple Immutability](#-tuple-immutability)
* [Adding and Removing Elements](#-adding-and-removing-elements)
* [Tuple Methods](#-tuple-methods)
* [Built-in Functions](#-built-in-functions-with-tuples)
* [Looping Through Tuples](#-looping-through-tuples)
* [Tuple Unpacking](#-tuple-unpacking)
* [Extended Unpacking](#-extended-unpacking)
* [Nested Tuples](#-nested-tuples)
* [Tuple Concatenation](#-tuple-concatenation)
* [Tuple Repetition](#-tuple-repetition)
* [Membership Operators](#-membership-operators)
* [Converting Between Lists and Tuples](#-converting-between-lists-and-tuples)
* [Tuple vs List](#-tuple-vs-list)
* [When to Use Tuples](#-when-to-use-tuples)
* [Quick Reference](#-quick-reference)

---

# 🔹 Creating Tuples

Tuples are usually created using parentheses `()`.

```python
numbers = (10, 20, 30, 40)

print(numbers)
# (10, 20, 30, 40)
```

You can also create a tuple without parentheses:

```python
numbers = 10, 20, 30

print(numbers)
# (10, 20, 30)
```

Python automatically treats comma-separated values as a tuple.

---

## 📦 Empty Tuple

An empty tuple can be created using:

```python
empty_tuple = ()

print(empty_tuple)
# ()
```

You can also use the `tuple()` function:

```python
empty_tuple = tuple()
```

---

# ⚠️ Creating a Tuple With One Element

A single-element tuple **must contain a comma**.

```python
number = (10,)

print(type(number))
# <class 'tuple'>
```

Without the comma:

```python
number = (10)

print(type(number))
# <class 'int'>
```

### ❌ Not a tuple

```python
number = (10)
```

### ✅ Tuple

```python
number = (10,)
```

The comma is what makes it a tuple.

---

# 🔹 Tuple Characteristics

Python tuples have several important characteristics:

### 1. Ordered

Elements maintain their position.

```python
colors = ("red", "green", "blue")

print(colors[0])
# red
```

### 2. Immutable

Elements cannot be changed.

```python
numbers = (10, 20, 30)

# numbers[0] = 100
# TypeError
```

### 3. Allow Duplicates

```python
numbers = (10, 20, 20, 30)

print(numbers)
# (10, 20, 20, 30)
```

### 4. Can Store Different Data Types

```python
data = (10, "Python", 3.14, True)

print(data)
```

### 5. Can Contain Other Tuples

```python
nested = ((1, 2), (3, 4))

print(nested)
```

---

# 🔹 Accessing Tuple Elements

Tuple indexing starts from `0`.

```python
fruits = ("apple", "banana", "orange")

print(fruits[0])
# apple

print(fruits[1])
# banana

print(fruits[2])
# orange
```

### Index Positions

```text
apple     banana     orange
  0          1          2
```

---

# 🔹 Negative Indexing

Negative indexing allows you to access elements from the end.

```python
fruits = ("apple", "banana", "orange")

print(fruits[-1])
# orange

print(fruits[-2])
# banana

print(fruits[-3])
# apple
```

### Negative Positions

```text
apple     banana     orange
 -3        -2         -1
```

---

# 🔹 Tuple Slicing

Slicing allows you to extract a portion of a tuple.

Syntax:

```python
tuple[start:stop]
```

Example:

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
# (20, 30, 40)
```

The `stop` index is not included.

---

## 🔸 Common Slicing Examples

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[:3])
# (10, 20, 30)

print(numbers[2:])
# (30, 40, 50)

print(numbers[1:4])
# (20, 30, 40)

print(numbers[:])
# (10, 20, 30, 40, 50)
```

---

## 🔄 Reverse a Tuple

```python
numbers = (10, 20, 30, 40)

print(numbers[::-1])
# (40, 30, 20, 10)
```

---

# 🔒 Tuple Immutability

Tuples cannot be modified after creation.

```python
numbers = (10, 20, 30)

numbers[0] = 100
```

This produces:

```text
TypeError: 'tuple' object does not support item assignment
```

You cannot directly:

* Change an element
* Add an element
* Remove an element

For example:

```python
numbers = (10, 20, 30)

# numbers.append(40)   ❌
# numbers.remove(20)   ❌
# numbers[0] = 100     ❌
```

---

# 🔹 Adding and Removing Elements

Because tuples are immutable, they don't have methods like:

```python
append()
remove()
insert()
pop()
clear()
```

However, you can create a **new tuple**.

```python
numbers = (10, 20, 30)

numbers = numbers + (40,)

print(numbers)
# (10, 20, 30, 40)
```

The original tuple wasn't modified. A new tuple was created.

---

# 🔹 Tuple Methods

Tuples have only **two built-in methods**.

## 1. count()

`count()` returns the number of times a value appears.

```python
numbers = (10, 20, 20, 30, 20)

print(numbers.count(20))
# 3
```

### Another Example

```python
colors = ("red", "blue", "red", "green")

print(colors.count("red"))
# 2
```

---

## 2. index()

`index()` returns the position of the first occurrence of a value.

```python
numbers = (10, 20, 30, 40)

print(numbers.index(30))
# 2
```

If the value doesn't exist:

```python
numbers = (10, 20, 30)

# numbers.index(100)
```

Python raises:

```text
ValueError
```

---

# 🔹 Built-in Functions With Tuples

Python provides several useful functions that work with tuples.

---

## len()

Returns the number of elements.

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
# 4
```

---

## max()

Returns the largest value.

```python
numbers = (10, 50, 20, 30)

print(max(numbers))
# 50
```

---

## min()

Returns the smallest value.

```python
numbers = (10, 50, 20, 30)

print(min(numbers))
# 10
```

---

## sum()

Returns the total of numeric elements.

```python
numbers = (10, 20, 30)

print(sum(numbers))
# 60
```

---

## sorted()

Returns a **new list** containing sorted elements.

```python
numbers = (30, 10, 20)

result = sorted(numbers)

print(result)
# [10, 20, 30]
```

⚠️ Notice that `sorted()` returns a **list**, not a tuple.

---

## tuple()

Converts an iterable into a tuple.

```python
numbers = [10, 20, 30]

result = tuple(numbers)

print(result)
# (10, 20, 30)
```

Another example:

```python
letters = tuple("Python")

print(letters)
# ('P', 'y', 't', 'h', 'o', 'n')
```

---

# 🔹 Looping Through Tuples

You can use a `for` loop to access every element.

```python
fruits = ("apple", "banana", "orange")

for fruit in fruits:
    print(fruit)
```

Output:

```text
apple
banana
orange
```

---

## 🔢 Loop With Index

You can use `range()` and `len()`:

```python
fruits = ("apple", "banana", "orange")

for i in range(len(fruits)):
    print(i, fruits[i])
```

Output:

```text
0 apple
1 banana
2 orange
```

---

# 🔹 enumerate()

`enumerate()` gives you both the index and the value.

```python
fruits = ("apple", "banana", "orange")

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output:

```text
0 apple
1 banana
2 orange
```

This is usually cleaner than manually using `range()`.

---

# 🔹 Tuple Unpacking

Tuple unpacking allows you to assign tuple values to multiple variables.

```python
person = ("Hadi", 20, "Python")

name, age, language = person

print(name)
# Hadi

print(age)
# 20

print(language)
# Python
```

The number of variables must normally match the number of values.

```python
numbers = (10, 20, 30)

a, b, c = numbers

print(a)
# 10

print(b)
# 20

print(c)
# 30
```

---

# 🔹 Extended Unpacking

Using `*`, you can collect multiple values into a list.

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
# 10

print(middle)
# [20, 30, 40]

print(last)
# 50
```

Notice that `middle` becomes a **list**.

---

# 🔹 Nested Tuples

A tuple can contain other tuples.

```python
numbers = (
    (1, 2),
    (3, 4),
    (5, 6)
)

print(numbers[0])
# (1, 2)

print(numbers[0][1])
# 2
```

Nested tuples are useful for representing structured data.

---

# 🔹 Tuple Concatenation

You can combine tuples using `+`.

```python
a = (1, 2, 3)
b = (4, 5, 6)

result = a + b

print(result)
# (1, 2, 3, 4, 5, 6)
```

This creates a **new tuple**.

---

# 🔹 Tuple Repetition

The `*` operator can repeat a tuple.

```python
numbers = (1, 2)

result = numbers * 3

print(result)
# (1, 2, 1, 2, 1, 2)
```

---

# 🔹 Membership Operators

You can check whether an element exists using `in`.

```python
numbers = (10, 20, 30)

print(20 in numbers)
# True
```

Using `not in`:

```python
print(50 not in numbers)
# True
```

---

# 🔹 Comparing Tuples

Tuples can be compared using comparison operators.

```python
a = (1, 2, 3)
b = (1, 2, 4)

print(a == b)
# False

print(a < b)
# True
```

Python compares elements from left to right.

---

# 🔹 Converting Lists to Tuples

Use `tuple()` to convert a list into a tuple.

```python
numbers = [10, 20, 30]

numbers = tuple(numbers)

print(numbers)
# (10, 20, 30)
```

---

# 🔹 Converting Tuples to Lists

Use `list()` to convert a tuple into a list.

```python
numbers = (10, 20, 30)

numbers = list(numbers)

print(numbers)
# [10, 20, 30]
```

This is useful when you need to modify the data.

Example:

```python
numbers = (10, 20, 30)

numbers = list(numbers)

numbers.append(40)

numbers = tuple(numbers)

print(numbers)
# (10, 20, 30, 40)
```

---

# 🔹 Tuple vs List

| Feature    | List  | Tuple |
| ---------- | ----- | ----- |
| Syntax     | `[]`  | `()`  |
| Mutable    | ✅ Yes | ❌ No  |
| Ordered    | ✅ Yes | ✅ Yes |
| Duplicates | ✅ Yes | ✅ Yes |
| Indexing   | ✅ Yes | ✅ Yes |
| Slicing    | ✅ Yes | ✅ Yes |
| `append()` | ✅ Yes | ❌ No  |
| `remove()` | ✅ Yes | ❌ No  |
| `sort()`   | ✅ Yes | ❌ No  |
| `count()`  | ✅ Yes | ✅ Yes |
| `index()`  | ✅ Yes | ✅ Yes |

---

# 🔹 When Should You Use Tuples?

Use a tuple when the data **should not change**.

### Example: Coordinates

```python
coordinates = (33.6844, 73.0479)
```

### Example: Days of the Week

```python
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)
```

### Example: RGB Color

```python
red = (255, 0, 0)
```

Tuples are useful for representing **fixed collections of related values**.

---

# 🔹 Important Tuple Concepts

### Tuple is Immutable

```python
data = (10, 20, 30)

# data[0] = 100  ❌
```

### Tuple Can Be Unpacked

```python
person = ("Hadi", 20)

name, age = person
```

### Tuple Can Be Nested

```python
data = ((1, 2), (3, 4))
```

### Tuple Can Contain Mutable Objects

A tuple itself cannot be changed, but it can contain a mutable object such as a list.

```python
data = ([1, 2], 3)

data[0].append(4)

print(data)
# ([1, 2, 4], 3)
```

The tuple still points to the same list; the **list inside it** was modified.

---

# 📚 Quick Reference

| Operation      | Example       | Result                |
| -------------- | ------------- | --------------------- |
| Create         | `(1, 2, 3)`   | Tuple                 |
| Access         | `t[0]`        | First element         |
| Negative index | `t[-1]`       | Last element          |
| Slice          | `t[1:3]`      | Part of tuple         |
| Count          | `t.count(2)`  | Number of occurrences |
| Index          | `t.index(2)`  | Position              |
| Length         | `len(t)`      | Number of elements    |
| Maximum        | `max(t)`      | Largest value         |
| Minimum        | `min(t)`      | Smallest value        |
| Sum            | `sum(t)`      | Total                 |
| Sort           | `sorted(t)`   | New sorted list       |
| Convert        | `tuple(list)` | Tuple                 |
| Unpack         | `a, b = t`    | Assign values         |
| Concatenate    | `t1 + t2`     | New tuple             |
| Repeat         | `t * 2`       | Repeated tuple        |
| Membership     | `x in t`      | `True` / `False`      |

---

# 🧠 Key Takeaways

* A tuple is an **ordered collection**.
* Tuples are **immutable**.
* Tuples allow **duplicate values**.
* Tuples support **indexing and slicing**.
* Tuples can contain **different data types**.
* Tuples can contain **lists and other tuples**.
* Tuples have only **two methods: `count()` and `index()`**.
* Tuples support **unpacking**.
* Use tuples when your collection of values should generally remain **unchanged**.

```python
# Example

student = ("Hadi", 20, "Python")

name, age, subject = student

print(name)
print(age)
print(subject)
```

### ⭐ Remember

> **List = Mutable `[ ]`**
> **Tuple = Immutable `( )`**
