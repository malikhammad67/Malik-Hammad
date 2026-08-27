# 🐍 Python Sets

A **set** is an unordered collection of unique elements in Python.

Sets are useful when you want to store values **without duplicates** and perform mathematical set operations such as **union, intersection, and difference**.

```python
numbers = {10, 20, 30, 40}

print(numbers)
# {10, 20, 30, 40}
```

---

## 📌 Table of Contents

* [Creating Sets](#-creating-sets)
* [Set Characteristics](#-set-characteristics)
* [Creating an Empty Set](#-creating-an-empty-set)
* [Duplicate Values](#-duplicate-values)
* [Adding Elements](#-adding-elements)
* [Removing Elements](#-removing-elements)
* [Set Methods](#-set-methods)
* [Set Operations](#-set-operations)
* [Union](#-union)
* [Intersection](#-intersection)
* [Difference](#-difference)
* [Symmetric Difference](#-symmetric-difference)
* [Subset and Superset](#-subset-and-superset)
* [Membership Operators](#-membership-operators)
* [Looping Through Sets](#-looping-through-sets)
* [Set Comprehension](#-set-comprehension)
* [Converting Lists to Sets](#-converting-lists-to-sets)
* [Frozen Sets](#-frozen-sets)
* [Set vs List vs Tuple](#-set-vs-list-vs-tuple)
* [When to Use Sets](#-when-to-use-sets)
* [Quick Reference](#-quick-reference)
* [Key Takeaways](#-key-takeaways)

---

# 🔹 Creating Sets

Sets are created using curly brackets `{}`.

```python
numbers = {10, 20, 30, 40}

print(numbers)
# {10, 20, 30, 40}
```

A set can contain different data types:

```python
data = {10, "Python", 3.14, True}

print(data)
```

---

# 🔹 Set Characteristics

Python sets have several important characteristics.

### 1. Unordered

Sets do not maintain a guaranteed positional order.

```python
numbers = {10, 20, 30, 40}
```

You should **not rely on indexing or position** in a set.

```python
# numbers[0]  ❌
```

---

### 2. No Duplicate Values

Sets automatically remove duplicate values.

```python
numbers = {10, 20, 20, 30, 30}

print(numbers)
# {10, 20, 30}
```

This makes sets very useful for removing duplicates.

---

### 3. Mutable

You can add or remove elements from a set.

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
# {10, 20, 30, 40}
```

However, individual set elements cannot be changed directly.

---

### 4. Elements Must Be Hashable

A set can contain immutable/hashable objects such as:

```python
numbers = {1, 2, 3}
names = {"Ali", "Ahmed", "Hadi"}
coordinates = {(1, 2), (3, 4)}
```

But you cannot put a list directly inside a set:

```python
# data = {[1, 2], [3, 4]}  ❌
```

This raises a `TypeError` because lists are unhashable.

---

# 🔹 Creating an Empty Set

⚠️ This is important.

Using `{}` creates an **empty dictionary**, not an empty set.

```python
empty = {}

print(type(empty))
# <class 'dict'>
```

To create an empty set, use `set()`:

```python
empty_set = set()

print(type(empty_set))
# <class 'set'>
```

### Remember:

```python
{}       # Empty dictionary
set()    # Empty set
```

---

# 🔹 Duplicate Values

Sets automatically keep only unique values.

```python
numbers = {1, 2, 2, 3, 3, 3, 4}

print(numbers)
# {1, 2, 3, 4}
```

This is one of the biggest advantages of sets.

---

# 🔹 Adding Elements

## 1. add()

`add()` adds one element to a set.

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
# {10, 20, 30, 40}
```

If the element already exists, nothing changes.

```python
numbers.add(20)

print(numbers)
# {10, 20, 30, 40}
```

---

## 2. update()

`update()` adds multiple elements.

```python
numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)
# {10, 20, 30, 40, 50}
```

You can update a set using another set:

```python
a = {1, 2, 3}
b = {4, 5, 6}

a.update(b)

print(a)
# {1, 2, 3, 4, 5, 6}
```

---

# 🔹 Removing Elements

## 1. remove()

`remove()` removes a specific element.

```python
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)
# {10, 30}
```

⚠️ If the element does not exist, `remove()` raises a `KeyError`.

```python
# numbers.remove(100)
```

---

## 2. discard()

`discard()` also removes an element.

The difference is that `discard()` **does not raise an error** if the element doesn't exist.

```python
numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)
# {10, 30}
```

If the element doesn't exist:

```python
numbers.discard(100)

# No error
```

### `remove()` vs `discard()`

| Method      | Element Exists | Element Doesn't Exist |
| ----------- | -------------- | --------------------- |
| `remove()`  | Removes it     | ❌ `KeyError`          |
| `discard()` | Removes it     | ✅ No error            |

---

## 3. pop()

`pop()` removes and returns an arbitrary element.

```python
numbers = {10, 20, 30}

item = numbers.pop()

print(item)
print(numbers)
```

⚠️ Unlike a list, you **cannot choose an index** because sets are unordered.

```python
# numbers.pop(0)  ❌
```

---

## 4. clear()

`clear()` removes all elements.

```python
numbers = {10, 20, 30}

numbers.clear()

print(numbers)
# set()
```

---

# 🔹 Set Methods

Python provides many useful methods for working with sets.

| Method                          | Purpose                                  |
| ------------------------------- | ---------------------------------------- |
| `add()`                         | Add one element                          |
| `update()`                      | Add multiple elements                    |
| `remove()`                      | Remove an element                        |
| `discard()`                     | Remove safely                            |
| `pop()`                         | Remove arbitrary element                 |
| `clear()`                       | Remove all elements                      |
| `copy()`                        | Create a copy                            |
| `union()`                       | Combine sets                             |
| `intersection()`                | Find common elements                     |
| `difference()`                  | Find elements in one set but not another |
| `symmetric_difference()`        | Find elements that are not common        |
| `intersection_update()`         | Keep only common elements                |
| `difference_update()`           | Remove elements found in another set     |
| `symmetric_difference_update()` | Update with non-common elements          |
| `issubset()`                    | Check subset                             |
| `issuperset()`                  | Check superset                           |
| `isdisjoint()`                  | Check for no common elements             |

---

# 🔹 copy()

Creates a copy of a set.

```python
numbers = {10, 20, 30}

new_numbers = numbers.copy()

print(new_numbers)
# {10, 20, 30}
```

The two sets are separate objects.

---

# 🔥 Set Operations

Set operations are one of the most important reasons to use sets.

Suppose we have:

```python
python_students = {"Ali", "Ahmed", "Hadi", "Sara"}

java_students = {"Hadi", "Sara", "John", "Mike"}
```

Now we can perform different operations.

---

# 🔹 Union

Union combines all unique elements from both sets.

### Using `|`

```python
python_students = {"Ali", "Ahmed", "Hadi"}
java_students = {"Hadi", "Sara", "John"}

result = python_students | java_students

print(result)
# {'Ali', 'Ahmed', 'Hadi', 'Sara', 'John'}
```

### Using `union()`

```python
result = python_students.union(java_students)
```

Both produce the same set of unique elements.

### Visual idea

```text
A ∪ B

All elements from A + all elements from B
```

---

# 🔹 Intersection

Intersection returns elements that exist in **both sets**.

### Using `&`

```python
python_students = {"Ali", "Ahmed", "Hadi"}
java_students = {"Hadi", "Sara", "John"}

result = python_students & java_students

print(result)
# {'Hadi'}
```

### Using `intersection()`

```python
result = python_students.intersection(java_students)
```

### Visual idea

```text
A ∩ B

Only elements common to A and B
```

---

# 🔹 Difference

Difference returns elements that exist in the first set but **not** in the second.

### Using `-`

```python
python_students = {"Ali", "Ahmed", "Hadi"}
java_students = {"Hadi", "Sara", "John"}

result = python_students - java_students

print(result)
# {'Ali', 'Ahmed'}
```

Reverse the operation:

```python
result = java_students - python_students

print(result)
# {'Sara', 'John'}
```

### Using `difference()`

```python
result = python_students.difference(java_students)
```

---

# 🔹 Symmetric Difference

Symmetric difference returns elements that are in either set, but **not in both**.

### Using `^`

```python
python_students = {"Ali", "Ahmed", "Hadi"}
java_students = {"Hadi", "Sara", "John"}

result = python_students ^ java_students

print(result)
# {'Ali', 'Ahmed', 'Sara', 'John'}
```

`Hadi` is removed because it exists in both sets.

### Using `symmetric_difference()`

```python
result = python_students.symmetric_difference(java_students)
```

---

# 🔹 Set Operation Summary

Suppose:

```python
A = {1, 2, 3}
B = {3, 4, 5}
```

| Operation            | Syntax   | Result            |
| -------------------- | -------- | ----------------- |
| Union                | `A \| B` | `{1, 2, 3, 4, 5}` |
| Intersection         | `A & B`  | `{3}`             |
| Difference           | `A - B`  | `{1, 2}`          |
| Difference           | `B - A`  | `{4, 5}`          |
| Symmetric Difference | `A ^ B`  | `{1, 2, 4, 5}`    |

---

# 🔹 union()

Returns a new set containing all unique elements.

```python
a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)

print(result)
# {1, 2, 3, 4, 5}
```

You can combine multiple sets:

```python
a.union(b, {6, 7})
```

---

# 🔹 intersection()

Returns a new set containing only common elements.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.intersection(b)

print(result)
# {3, 4}
```

---

# 🔹 difference()

Returns elements present in the first set but not in the other.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.difference(b)

print(result)
# {1, 2}
```

---

# 🔹 symmetric_difference()

Returns elements that exist in either set but not both.

```python
a = {1, 2, 3}
b = {3, 4, 5}

result = a.symmetric_difference(b)

print(result)
# {1, 2, 4, 5}
```

---

# 🔹 intersection_update()

Updates the original set to keep only common elements.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}

a.intersection_update(b)

print(a)
# {3, 4}
```

⚠️ Unlike `intersection()`, this changes the original set.

---

# 🔹 difference_update()

Removes elements from the first set that exist in the second set.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}

a.difference_update(b)

print(a)
# {1, 2}
```

---

# 🔹 symmetric_difference_update()

Updates the original set with elements that are not common.

```python
a = {1, 2, 3}
b = {3, 4, 5}

a.symmetric_difference_update(b)

print(a)
# {1, 2, 4, 5}
```

---

# 🔹 Subset

A set is a **subset** if all its elements exist inside another set.

```python
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
# True
```

You can also use `<=`:

```python
print(a <= b)
# True
```

### Example

```text
A = {1, 2}
B = {1, 2, 3, 4}

A is a subset of B
```

---

# 🔹 Superset

A set is a **superset** if it contains all elements of another set.

```python
a = {1, 2, 3, 4}
b = {1, 2}

print(a.issuperset(b))
# True
```

You can also use `>=`:

```python
print(a >= b)
# True
```

---

# 🔹 isdisjoint()

Checks whether two sets have **no common elements**.

```python
a = {1, 2, 3}
b = {4, 5, 6}

print(a.isdisjoint(b))
# True
```

If they have a common element:

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.isdisjoint(b))
# False
```

---

# 🔹 Membership Operators

Use `in` to check whether an element exists.

```python
numbers = {10, 20, 30}

print(20 in numbers)
# True
```

Use `not in`:

```python
print(50 not in numbers)
# True
```

Sets are particularly useful for membership testing.

---

# 🔹 Looping Through Sets

You can use a `for` loop.

```python
fruits = {"apple", "banana", "orange"}

for fruit in fruits:
    print(fruit)
```

⚠️ The order of output is not something you should rely on.

---

# ❌ Sets Do Not Support Indexing

You cannot access a set using an index.

```python
numbers = {10, 20, 30}

# print(numbers[0])  ❌
```

This raises:

```text
TypeError
```

If you need indexing, convert the set to a list:

```python
numbers = {10, 20, 30}

numbers = list(numbers)

print(numbers[0])
```

---

# 🔹 Set Comprehension

Set comprehension provides a short way to create sets.

### Example

```python
squares = {x ** 2 for x in range(5)}

print(squares)
# {0, 1, 4, 9, 16}
```

With a condition:

```python
even_numbers = {x for x in range(10) if x % 2 == 0}

print(even_numbers)
# {0, 2, 4, 6, 8}
```

### General Syntax

```python
{expression for item in iterable}
```

With condition:

```python
{expression for item in iterable if condition}
```

---

# 🔹 Removing Duplicates From a List

One of the most common uses of sets is removing duplicates.

```python
numbers = [1, 2, 2, 3, 3, 4, 4]

unique_numbers = set(numbers)

print(unique_numbers)
# {1, 2, 3, 4}
```

If you need a list again:

```python
unique_numbers = list(set(numbers))

print(unique_numbers)
# [1, 2, 3, 4]
```

⚠️ The order should not be relied upon.

---

# 🔹 Converting List to Set

Use `set()`.

```python
numbers = [10, 20, 30, 20, 10]

numbers = set(numbers)

print(numbers)
# {10, 20, 30}
```

---

# 🔹 Converting Set to List

Use `list()`.

```python
numbers = {10, 20, 30}

numbers = list(numbers)

print(numbers)
```

---

# 🔹 Converting Set to Tuple

Use `tuple()`.

```python
numbers = {10, 20, 30}

numbers = tuple(numbers)

print(numbers)
# (10, 20, 30)
```

---

# 🧊 Frozen Sets

A **frozenset** is an immutable version of a set.

```python
numbers = frozenset([1, 2, 3, 4])

print(numbers)
# frozenset({1, 2, 3, 4})
```

Because a frozenset is immutable, you cannot use methods that modify it.

```python
# numbers.add(5)  ❌
# numbers.remove(1)  ❌
```

But you can perform operations such as:

```python
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print(a | b)
# frozenset({1, 2, 3, 4, 5})
```

---

# 🔹 Set vs List vs Tuple

| Feature                 | List | Tuple | Set  |
| ----------------------- | ---- | ----- | ---- |
| Syntax                  | `[]` | `()`  | `{}` |
| Ordered                 | ✅    | ✅     | ❌    |
| Mutable                 | ✅    | ❌     | ✅    |
| Duplicates              | ✅    | ✅     | ❌    |
| Indexing                | ✅    | ✅     | ❌    |
| Slicing                 | ✅    | ✅     | ❌    |
| `append()`              | ✅    | ❌     | ❌    |
| `add()`                 | ❌    | ❌     | ✅    |
| `remove()`              | ✅    | ❌     | ✅    |
| Mathematical operations | ❌    | ❌     | ✅    |
| Unique values           | ❌    | ❌     | ✅    |

---

# 🔹 When Should You Use Sets?

Use sets when:

### ✅ You need unique values

```python
emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}

print(emails)
```

Duplicates are automatically removed.

---

### ✅ You need fast membership checking

```python
allowed_users = {"Ali", "Ahmed", "Hadi"}

if "Hadi" in allowed_users:
    print("Access granted")
```

---

### ✅ You need mathematical set operations

```python
common = python_students & java_students
```

This makes finding common elements very simple.

---

# 🔹 Real-World Example

Imagine two courses:

```python
python_students = {
    "Ali",
    "Ahmed",
    "Hadi",
    "Sara"
}

web_students = {
    "Hadi",
    "Sara",
    "John",
    "Mike"
}
```

### Students in both courses:

```python
both = python_students & web_students

print(both)
# {'Hadi', 'Sara'}
```

### Students only in Python:

```python
only_python = python_students - web_students

print(only_python)
# {'Ali', 'Ahmed'}
```

### Students in either course:

```python
all_students = python_students | web_students

print(all_students)
```

Sets make these operations extremely simple.

---

# 📚 Quick Reference

| Operation            | Example            | Purpose                    |
| -------------------- | ------------------ | -------------------------- |
| Create               | `{1, 2, 3}`        | Create set                 |
| Empty set            | `set()`            | Create empty set           |
| Add                  | `s.add(4)`         | Add one element            |
| Update               | `s.update([4, 5])` | Add multiple elements      |
| Remove               | `s.remove(2)`      | Remove element             |
| Discard              | `s.discard(2)`     | Remove safely              |
| Pop                  | `s.pop()`          | Remove arbitrary element   |
| Clear                | `s.clear()`        | Remove everything          |
| Copy                 | `s.copy()`         | Copy set                   |
| Union                | `a \| b`           | Combine sets               |
| Intersection         | `a & b`            | Common elements            |
| Difference           | `a - b`            | Elements only in first set |
| Symmetric Difference | `a ^ b`            | Non-common elements        |
| Subset               | `a.issubset(b)`    | Check subset               |
| Superset             | `a.issuperset(b)`  | Check superset             |
| Disjoint             | `a.isdisjoint(b)`  | Check no common elements   |
| Membership           | `x in s`           | Check existence            |
| Convert              | `set(list)`        | List → Set                 |

---

# 🧠 Key Takeaways

* A **set stores unique elements**.
* Sets are **mutable**.
* Sets are **unordered**.
* Sets do **not support indexing or slicing**.
* Sets automatically remove **duplicate values**.
* Use `set()` to create an empty set.
* Use `add()` to add one element.
* Use `update()` to add multiple elements.
* Use `remove()` when the element should exist.
* Use `discard()` when you want to remove safely.
* Use `|` for **union**.
* Use `&` for **intersection**.
* Use `-` for **difference**.
* Use `^` for **symmetric difference**.
* Use `issubset()` and `issuperset()` for set relationships.
* Use sets when **uniqueness and membership testing** are important.

### ⭐ Remember

```text
List  → Ordered + Mutable + Duplicates
Tuple → Ordered + Immutable + Duplicates
Set   → Unordered + Mutable + Unique
```

```python
# Simple example

python = {"Ali", "Ahmed", "Hadi"}
web = {"Hadi", "Sara", "John"}

print(python | web)   # Union
print(python & web)   # Intersection
print(python - web)   # Difference
print(python ^ web)   # Symmetric Difference
```
