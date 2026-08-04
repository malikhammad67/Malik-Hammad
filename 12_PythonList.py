# Python Lists

## What is a List?

A **list** is a collection of multiple items stored in a single variable.

Lists are:
- Ordered
- Changeable (Mutable)
- Allow duplicate values

Lists are created using square brackets `[]`.

---

## Creating a List

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)
```

**Output:**
```
['Apple', 'Banana', 'Mango']
```

---

## List Items

A list can store different data types.

```python
data = ["Ali", 20, 3.5, True]

print(data)
```

**Output:**
```
['Ali', 20, 3.5, True]
```

---

## Accessing List Items

List indexing starts from `0`.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
print(fruits[-1])
```

**Output:**
```
Apple
Banana
Mango
```

---

## List Slicing

Slicing is used to get a part of a list.

**Syntax:**

```python
list[start:end]
```

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
```

**Output:**
```
[20, 30, 40]
[10, 20, 30]
[30, 40, 50]
```

---

## Change List Items

Lists are mutable, so you can change their values.

```python
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)
```

**Output:**
```
['Apple', 'Orange', 'Mango']
```

---

## Add Items to a List

### `append()`

Adds an item to the end of the list.

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)
```

**Output:**
```
['Apple', 'Banana', 'Mango']
```

---

### `insert()`

Adds an item at a specific position.

```python
fruits = ["Apple", "Mango"]

fruits.insert(1, "Banana")

print(fruits)
```

**Output:**
```
['Apple', 'Banana', 'Mango']
```

---

## Remove Items from a List

### `remove()`

Removes a specific item.

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)
```

**Output:**
```
['Apple', 'Mango']
```

---

### `pop()`

Removes an item by index.

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.pop(1)

print(fruits)
```

**Output:**
```
['Apple', 'Mango']
```

---

### `del`

Deletes an item or the entire list.

```python
numbers = [10, 20, 30]

del numbers[1]

print(numbers)
```

**Output:**
```
[10, 30]
```

---

## List Length

Use `len()` to find the number of items.

```python
fruits = ["Apple", "Banana", "Mango"]

print(len(fruits))
```

**Output:**
```
3
```

---

## Loop Through a List

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

**Output:**
```
Apple
Banana
Mango
```

---

## Check if an Item Exists

Use the `in` operator.

```python
fruits = ["Apple", "Banana", "Mango"]

print("Banana" in fruits)
```

**Output:**
```
True
```

---

## Common List Methods

| Method | Description |
|---------|-------------|
| `append()` | Adds an item to the end |
| `insert()` | Adds an item at a specific index |
| `remove()` | Removes a specific item |
| `pop()` | Removes an item by index |
| `clear()` | Removes all items |
| `copy()` | Creates a copy of the list |
| `sort()` | Sorts the list |
| `reverse()` | Reverses the list |
| `count()` | Counts occurrences of an item |
| `index()` | Returns the index of an item |

---

## Sort a List

```python
numbers = [5, 2, 9, 1]

numbers.sort()

print(numbers)
```

**Output:**
```
[1, 2, 5, 9]
```

---

## Reverse a List

```python
numbers = [1, 2, 3, 4]

numbers.reverse()

print(numbers)
```

**Output:**
```
[4, 3, 2, 1]
```

---

## Copy a List

```python
fruits = ["Apple", "Banana"]

new_list = fruits.copy()

print(new_list)
```

**Output:**
```
['Apple', 'Banana']
```

---

## Key Points

- Lists store multiple values in one variable.
- Lists are ordered and mutable.
- Lists allow duplicate values.
- Indexing starts from `0`.
- Negative indexing starts from `-1`.
- Use `append()` to add items.
- Use `remove()` or `pop()` to delete items.
- Use `len()` to find the list length.

---

# Practice

### 1. Create a list and print it.

```python
colors = ["Red", "Green", "Blue"]

print(colors)
```

**Output:**
```
['Red', 'Green', 'Blue']
```

---

### 2. Add a new item.

```python
numbers = [10, 20]

numbers.append(30)

print(numbers)
```

**Output:**
```
[10, 20, 30]
```

---

### 3. Remove an item.

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)
```

**Output:**
```
['Apple', 'Mango']
```

---

### 4. Find the length of a list.

```python
animals = ["Cat", "Dog", "Lion"]

print(len(animals))
```

**Output:**
```
3
```

---

### 5. Loop through a list.

```python
numbers = [1, 2, 3]

for num in numbers:
    print(num)
```

**Output:**
```
1
2
3
```