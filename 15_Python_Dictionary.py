# 🐍 Python Dictionaries

A **dictionary** is a collection of **key-value pairs** in Python.

Dictionaries are used to store data where every value is associated with a unique key.

```python
student = {
    "name": "Hadi",
    "age": 20,
    "language": "Python"
}

print(student)
```

Output:

```text
{'name': 'Hadi', 'age': 20, 'language': 'Python'}
```

---

## 📌 Table of Contents

* [Creating a Dictionary](#-creating-a-dictionary)
* [Dictionary Characteristics](#-dictionary-characteristics)
* [Keys and Values](#-keys-and-values)
* [Accessing Values](#-accessing-values)
* [get() Method](#-get-method)
* [Adding Items](#-adding-items)
* [Updating Items](#-updating-items)
* [Removing Items](#-removing-items)
* [Dictionary Methods](#-dictionary-methods)
* [keys()](#-keys)
* [values()](#-values)
* [items()](#-items)
* [update()](#-update)
* [setdefault()](#-setdefault)
* [pop()](#-pop)
* [popitem()](#-popitem)
* [clear()](#-clear)
* [copy()](#-copy)
* [Looping Through Dictionaries](#-looping-through-dictionaries)
* [Checking Keys](#-checking-keys)
* [Dictionary Length](#-dictionary-length)
* [Nested Dictionaries](#-nested-dictionaries)
* [Dictionary Comprehension](#-dictionary-comprehension)
* [Copying Dictionaries](#-copying-dictionaries)
* [Dictionary Unpacking](#-dictionary-unpacking)
* [Merging Dictionaries](#-merging-dictionaries)
* [Converting to Dictionary](#-converting-to-dictionary)
* [Dictionary vs List vs Tuple vs Set](#-dictionary-vs-list-vs-tuple-vs-set)
* [Real-World Example](#-real-world-example)
* [Quick Reference](#-quick-reference)
* [Key Takeaways](#-key-takeaways)

---

# 🔹 Creating a Dictionary

Dictionaries are created using curly brackets `{}`.

Each item has a:

```text
key : value
```

Example:

```python
person = {
    "name": "Hadi",
    "age": 20,
    "city": "Islamabad"
}
```

You can also create a dictionary using `dict()`:

```python
person = dict(
    name="Hadi",
    age=20,
    city="Islamabad"
)

print(person)
```

---

# 🔹 Dictionary Characteristics

Python dictionaries have several important characteristics.

### 1. Key-Value Structure

Every item consists of a key and its value.

```python
student = {
    "name": "Hadi",
    "age": 20
}
```

Here:

```text
"name" → key
"Hadi" → value

"age" → key
20     → value
```

---

### 2. Keys Must Be Unique

A dictionary cannot have two different values under the same key.

```python
student = {
    "name": "Hadi",
    "age": 20,
    "name": "Ali"
}

print(student)
```

Output:

```text
{'name': 'Ali', 'age': 20}
```

The second `"name"` replaces the first one.

---

### 3. Dictionaries Are Mutable

You can add, remove, and update items.

```python
student = {
    "name": "Hadi",
    "age": 20
}

student["age"] = 21

print(student)
```

Output:

```text
{'name': 'Hadi', 'age': 21}
```

---

### 4. Dictionaries Preserve Insertion Order

Modern Python dictionaries preserve the order in which items are inserted.

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(data)
```

The insertion order is preserved.

---

### 5. Values Can Be Any Data Type

Dictionary values can be strings, numbers, lists, tuples, sets, dictionaries, etc.

```python
data = {
    "name": "Hadi",
    "age": 20,
    "skills": ["Python", "HTML", "CSS"],
    "active": True
}
```

---

### 6. Keys Must Be Hashable

Keys must be hashable, so common key types include:

```python
data = {
    "name": "Hadi",
    1: "One",
    (10, 20): "Coordinates"
}
```

A list cannot be used as a dictionary key:

```python
# data = {[1, 2]: "Numbers"}  ❌
```

---

# 🔹 Keys and Values

A dictionary contains **keys** and **values**.

```python
student = {
    "name": "Hadi",
    "age": 20,
    "course": "Python"
}
```

Keys:

```text
name
age
course
```

Values:

```text
Hadi
20
Python
```

---

# 🔹 Accessing Values

You can access a value using its key.

```python
student = {
    "name": "Hadi",
    "age": 20,
    "course": "Python"
}

print(student["name"])
# Hadi

print(student["age"])
# 20
```

---

## ⚠️ KeyError

If you try to access a key that doesn't exist:

```python
print(student["city"])
```

Python raises:

```text
KeyError
```

For safer access, use `get()`.

---

# 🔹 get()

`get()` returns the value associated with a key.

```python
student = {
    "name": "Hadi",
    "age": 20
}

print(student.get("name"))
# Hadi
```

If the key doesn't exist:

```python
print(student.get("city"))
# None
```

You can provide a default value:

```python
print(student.get("city", "Unknown"))
# Unknown
```

### `[]` vs `get()`

```python
student["city"]
# KeyError if missing
```

```python
student.get("city")
# None if missing
```

---

# 🔹 Adding Items

You can add a new key-value pair using square brackets.

```python
student = {
    "name": "Hadi",
    "age": 20
}

student["city"] = "Islamabad"

print(student)
```

Output:

```text
{'name': 'Hadi', 'age': 20, 'city': 'Islamabad'}
```

---

# 🔹 Updating Items

If the key already exists, assigning a new value updates it.

```python
student = {
    "name": "Hadi",
    "age": 20
}

student["age"] = 21

print(student)
```

Output:

```text
{'name': 'Hadi', 'age': 21}
```

---

# 🔹 Adding Multiple Items

Use `update()`.

```python
student = {
    "name": "Hadi",
    "age": 20
}

student.update({
    "city": "Islamabad",
    "language": "Python"
})

print(student)
```

Output:

```text
{
    'name': 'Hadi',
    'age': 20,
    'city': 'Islamabad',
    'language': 'Python'
}
```

---

# 🔹 Removing Items

Python provides several ways to remove dictionary items.

---

## 1. pop()

`pop()` removes a specific key and returns its value.

```python
student = {
    "name": "Hadi",
    "age": 20,
    "city": "Islamabad"
}

age = student.pop("age")

print(age)
# 20

print(student)
# {'name': 'Hadi', 'city': 'Islamabad'}
```

You can provide a default value:

```python
student.pop("country", "Not Found")
```

This prevents an error if the key doesn't exist.

---

# 🔹 popitem()

`popitem()` removes and returns the **last inserted key-value pair**.

```python
student = {
    "name": "Hadi",
    "age": 20,
    "city": "Islamabad"
}

item = student.popitem()

print(item)
# ('city', 'Islamabad')

print(student)
# {'name': 'Hadi', 'age': 20}
```

---

# 🔹 del

`del` removes an item using its key.

```python
student = {
    "name": "Hadi",
    "age": 20
}

del student["age"]

print(student)
# {'name': 'Hadi'}
```

⚠️ If the key doesn't exist, `del` raises `KeyError`.

You can also delete the entire dictionary:

```python
del student
```

---

# 🔹 clear()

`clear()` removes all dictionary items.

```python
student = {
    "name": "Hadi",
    "age": 20
}

student.clear()

print(student)
# {}
```

---

# 🔹 Dictionary Methods

Important dictionary methods:

| Method         | Purpose                     |
| -------------- | --------------------------- |
| `get()`        | Get a value safely          |
| `keys()`       | Return all keys             |
| `values()`     | Return all values           |
| `items()`      | Return key-value pairs      |
| `update()`     | Add/update multiple items   |
| `setdefault()` | Get value or insert default |
| `pop()`        | Remove specific key         |
| `popitem()`    | Remove last inserted pair   |
| `clear()`      | Remove everything           |
| `copy()`       | Create a copy               |
| `fromkeys()`   | Create dictionary from keys |

---

# 🔹 keys()

`keys()` returns a view containing all keys.

```python
student = {
    "name": "Hadi",
    "age": 20,
    "city": "Islamabad"
}

print(student.keys())
```

You can loop through the keys:

```python
for key in student.keys():
    print(key)
```

Output:

```text
name
age
city
```

---

# 🔹 values()

`values()` returns a view containing all values.

```python
student = {
    "name": "Hadi",
    "age": 20,
    "city": "Islamabad"
}

print(student.values())
```

Loop through values:

```python
for value in student.values():
    print(value)
```

Output:

```text
Hadi
20
Islamabad
```

---

# 🔹 items()

`items()` returns all key-value pairs.

```python
student = {
    "name": "Hadi",
    "age": 20
}

print(student.items())
```

You can unpack key and value while looping:

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Hadi
age 20
```

This is one of the most commonly used dictionary operations.

---

# 🔹 update()

`update()` adds new items or changes existing items.

```python
student = {
    "name": "Hadi",
    "age": 20
}

student.update({
    "age": 21,
    "city": "Islamabad"
})

print(student)
```

Output:

```text
{
    'name': 'Hadi',
    'age': 21,
    'city': 'Islamabad'
}
```

Existing keys are updated, while new keys are added.

---

# 🔹 setdefault()

`setdefault()` returns the value of a key.

If the key doesn't exist, it adds the key with the specified default value.

```python
student = {
    "name": "Hadi"
}

age = student.setdefault("age", 20)

print(age)
# 20

print(student)
# {'name': 'Hadi', 'age': 20}
```

If the key already exists:

```python
student = {
    "name": "Hadi",
    "age": 20
}

student.setdefault("age", 30)

print(student)
# {'name': 'Hadi', 'age': 20}
```

The existing value is not replaced.

---

# 🔹 copy()

Creates a shallow copy of a dictionary.

```python
student = {
    "name": "Hadi",
    "age": 20
}

new_student = student.copy()

print(new_student)
# {'name': 'Hadi', 'age': 20}
```

The copied dictionary is a separate dictionary.

---

# 🔹 fromkeys()

`fromkeys()` creates a dictionary from a sequence of keys.

```python
keys = ["name", "age", "city"]

student = dict.fromkeys(keys)

print(student)
```

Output:

```text
{'name': None, 'age': None, 'city': None}
```

You can provide a default value:

```python
student = dict.fromkeys(keys, "Unknown")

print(student)
```

Output:

```text
{
    'name': 'Unknown',
    'age': 'Unknown',
    'city': 'Unknown'
}
```

---

# 🔹 Looping Through Dictionaries

## Loop Through Keys

```python
student = {
    "name": "Hadi",
    "age": 20,
    "city": "Islamabad"
}

for key in student:
    print(key)
```

---

## Loop Through Values

```python
for value in student.values():
    print(value)
```

---

## Loop Through Key-Value Pairs

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

Output:

```text
name: Hadi
age: 20
city: Islamabad
```

---

# 🔹 Checking Keys

Use `in` to check whether a key exists.

```python
student = {
    "name": "Hadi",
    "age": 20
}

print("name" in student)
# True

print("city" in student)
# False
```

Use `not in`:

```python
print("city" not in student)
# True
```

⚠️ `in` checks **keys**, not values.

```python
print("Hadi" in student)
# False
```

To check values:

```python
print("Hadi" in student.values())
# True
```

---

# 🔹 Dictionary Length

Use `len()` to count key-value pairs.

```python
student = {
    "name": "Hadi",
    "age": 20,
    "city": "Islamabad"
}

print(len(student))
# 3
```

---

# 🔹 Nested Dictionaries

A dictionary can contain another dictionary.

```python
students = {
    "student1": {
        "name": "Hadi",
        "age": 20
    },
    "student2": {
        "name": "Ali",
        "age": 22
    }
}
```

Access nested values:

```python
print(students["student1"]["name"])
# Hadi
```

Another example:

```python
print(students["student2"]["age"])
# 22
```

---

# 🔹 Dictionary With Lists

Dictionary values can contain lists.

```python
student = {
    "name": "Hadi",
    "skills": [
        "Python",
        "HTML",
        "CSS"
    ]
}

print(student["skills"])
```

Access a list element:

```python
print(student["skills"][0])
# Python
```

---

# 🔹 Dictionary With Tuples

```python
student = {
    "name": "Hadi",
    "coordinates": (33.6844, 73.0479)
}

print(student["coordinates"])
```

---

# 🔹 Dictionary Comprehension

Dictionary comprehension provides a short way to create dictionaries.

### Basic Example

```python
squares = {
    x: x ** 2
    for x in range(5)
}

print(squares)
```

Output:

```text
{
    0: 0,
    1: 1,
    2: 4,
    3: 9,
    4: 16
}
```

---

## 🔸 Dictionary Comprehension With Condition

```python
even_squares = {
    x: x ** 2
    for x in range(10)
    if x % 2 == 0
}

print(even_squares)
```

Output:

```text
{
    0: 0,
    2: 4,
    4: 16,
    6: 36,
    8: 64
}
```

### General Syntax

```python
{key: value for item in iterable}
```

With a condition:

```python
{key: value for item in iterable if condition}
```

---

# 🔹 Copying Dictionaries

There are different ways to copy dictionaries.

### Using copy()

```python
original = {
    "name": "Hadi",
    "age": 20
}

new = original.copy()
```

### Using dict()

```python
new = dict(original)
```

Both create a new dictionary.

---

# 🔹 Dictionary Unpacking

Python allows dictionaries to be unpacked using `**`.

```python
student = {
    "name": "Hadi",
    "age": 20
}

new_student = {
    **student,
    "city": "Islamabad"
}

print(new_student)
```

Output:

```text
{
    'name': 'Hadi',
    'age': 20,
    'city': 'Islamabad'
}
```

---

# 🔹 Merging Dictionaries

You can merge dictionaries using `|`.

```python
a = {
    "name": "Hadi"
}

b = {
    "age": 20
}

result = a | b

print(result)
```

Output:

```text
{'name': 'Hadi', 'age': 20}
```

You can also use `update()`:

```python
a = {
    "name": "Hadi"
}

b = {
    "age": 20
}

a.update(b)

print(a)
```

---

# 🔹 What Happens When Keys Are Duplicated During Merge?

If two dictionaries have the same key, the value from the second dictionary wins.

```python
a = {
    "name": "Hadi",
    "age": 20
}

b = {
    "age": 21,
    "city": "Islamabad"
}

result = a | b

print(result)
```

Output:

```text
{
    'name': 'Hadi',
    'age': 21,
    'city': 'Islamabad'
}
```

`21` replaces `20`.

---

# 🔹 Converting to Dictionary

You can create a dictionary from key-value pairs.

```python
data = [
    ("name", "Hadi"),
    ("age", 20),
    ("city", "Islamabad")
]

student = dict(data)

print(student)
```

Output:

```text
{
    'name': 'Hadi',
    'age': 20,
    'city': 'Islamabad'
}
```

---

# 🔹 Dictionary From Two Lists

You can combine two lists using `zip()`.

```python
keys = ["name", "age", "city"]
values = ["Hadi", 20, "Islamabad"]

student = dict(zip(keys, values))

print(student)
```

Output:

```text
{
    'name': 'Hadi',
    'age': 20,
    'city': 'Islamabad'
}
```

---

# 🔥 Real-World Example

Dictionaries are heavily used in real Python applications.

For example, storing user information:

```python
user = {
    "id": 101,
    "username": "hadi",
    "email": "hadi@example.com",
    "skills": ["Python", "Django", "JavaScript"],
    "is_active": True
}
```

Access information:

```python
print(user["username"])
# hadi

print(user["skills"])
# ['Python', 'Django', 'JavaScript']
```

Check whether a user is active:

```python
if user["is_active"]:
    print("User is active")
```

---

# 🌐 Dictionaries and JSON

Dictionaries are extremely important in **web development and APIs** because JSON data has a structure very similar to Python dictionaries.

Example JSON-like data:

```python
response = {
    "status": "success",
    "user": {
        "name": "Hadi",
        "age": 20
    }
}

print(response["user"]["name"])
# Hadi
```

This is why dictionaries are essential for working with:

* APIs
* JSON
* Flask
* Django
* FastAPI
* Databases
* Web applications

---

# 🔹 Dictionary vs List vs Tuple vs Set

| Feature         | List       | Tuple      | Set         | Dictionary     |
| --------------- | ---------- | ---------- | ----------- | -------------- |
| Syntax          | `[]`       | `()`       | `{}`        | `{key: value}` |
| Ordered         | ✅          | ✅          | ❌           | ✅              |
| Mutable         | ✅          | ❌          | ✅           | ✅              |
| Duplicates      | ✅          | ✅          | ❌           | Keys ❌         |
| Indexing        | ✅          | ✅          | ❌           | ❌              |
| Key-Value pairs | ❌          | ❌          | ❌           | ✅              |
| Unique keys     | ❌          | ❌          | —           | ✅              |
| Main use        | Collection | Fixed data | Unique data | Key-value data |

---

# 🔹 When Should You Use Dictionaries?

Use dictionaries when data has a clear **key → value relationship**.

### Example

Instead of:

```python
student = ["Hadi", 20, "Python"]
```

You can use:

```python
student = {
    "name": "Hadi",
    "age": 20,
    "language": "Python"
}
```

The dictionary is easier to understand because every value has a meaningful key.

---

# 🔹 Common Dictionary Mistakes

## ❌ Using a List as a Key

```python
# data = {
#     [1, 2]: "numbers"
# }
```

Lists are not hashable.

### ✅ Use a Tuple

```python
data = {
    (1, 2): "numbers"
}
```

---

## ❌ Accessing a Missing Key

```python
student = {
    "name": "Hadi"
}

# print(student["age"])  ❌
```

### ✅ Use get()

```python
print(student.get("age"))
# None
```

Or:

```python
print(student.get("age", 0))
# 0
```

---

# 📚 Quick Reference

| Operation       | Example            | Purpose              |
| --------------- | ------------------ | -------------------- |
| Create          | `{"name": "Hadi"}` | Create dictionary    |
| Access          | `d["name"]`        | Get value            |
| Safe access     | `d.get("name")`    | Get value safely     |
| Add             | `d["age"] = 20`    | Add item             |
| Update          | `d["age"] = 21`    | Change value         |
| Multiple update | `d.update({...})`  | Add/update items     |
| Keys            | `d.keys()`         | Get keys             |
| Values          | `d.values()`       | Get values           |
| Items           | `d.items()`        | Get key-value pairs  |
| Remove          | `d.pop("age")`     | Remove key           |
| Remove last     | `d.popitem()`      | Remove last pair     |
| Delete          | `del d["age"]`     | Delete key           |
| Clear           | `d.clear()`        | Remove all           |
| Copy            | `d.copy()`         | Create copy          |
| Default         | `d.setdefault()`   | Get/insert default   |
| Length          | `len(d)`           | Count items          |
| Membership      | `"name" in d`      | Check key            |
| Merge           | `d1 \| d2`         | Combine dictionaries |

---

# 🧠 Key Takeaways

* A dictionary stores **key-value pairs**.
* Dictionaries are **mutable**.
* Dictionary keys must be **unique**.
* Dictionary keys must be **hashable**.
* Dictionary values can be **any data type**.
* Use `d[key]` to access a value.
* Use `get()` for safer access.
* Use `update()` to add or update multiple items.
* Use `pop()` to remove a specific key.
* Use `popitem()` to remove the last inserted pair.
* Use `keys()` to get keys.
* Use `values()` to get values.
* Use `items()` to get key-value pairs.
* Dictionaries can contain **lists, tuples, sets, and other dictionaries**.
* Dictionary comprehensions provide a concise way to create dictionaries.
* Dictionaries are heavily used with **JSON and APIs**.

---

# ⭐ Remember

```text
List       → Collection of values
Tuple      → Fixed collection of values
Set        → Collection of unique values
Dictionary → Key → Value pairs
```

### Simple Example

```python
student = {
    "name": "Hadi",
    "age": 20,
    "skills": ["Python", "Django"]
}

print(student["name"])
print(student["age"])
print(student["skills"])
```

### The Most Important Dictionary Methods

```python
get()
keys()
values()
items()
update()
setdefault()
pop()
popitem()
clear()
copy()
```

> 💡 **Tip:** If you are learning Python for web development, make sure you become very comfortable with dictionaries. You will use them constantly when working with APIs, JSON, Flask, Django, and FastAPI.
