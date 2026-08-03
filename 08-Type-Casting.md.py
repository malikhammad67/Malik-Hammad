# Python Type Casting

## What is Type Casting?

Type casting is the process of converting one data type into another data type.

Python provides built-in functions for type conversion.

---

## Common Type Casting Functions

| Function | Converts To | Example |
|----------|-------------|---------|
| `int()` | Integer | `int("10")` |
| `float()` | Float | `float(5)` |
| `str()` | String | `str(100)` |
| `bool()` | Boolean | `bool(1)` |

---

## Examples

### Convert String to Integer

```python
num = "50"

num = int(num)

print(num)
```

**Output:**
```
50
```

---

### Convert Integer to Float

```python
age = 20

age = float(age)

print(age)
```

**Output:**
```
20.0
```

---

### Convert Number to String

```python
number = 100

text = str(number)

print(text)
```

**Output:**
```
100
```

---

## Key Points

- Type casting changes one data type into another.
- `int()`, `float()`, `str()`, and `bool()` are commonly used.
- Python does not change data types automatically in every situation.

---

# Practice

### 1. Convert a string into an integer.

```python
num = "25"

num = int(num)

print(num)
```

**Output:**
```
25
```

---

### 2. Convert a number into a float.

```python
value = 10

value = float(value)

print(value)
```

**Output:**
```
10.0
```

---

### 3. Convert an integer into a string.

```python
age = 18

age = str(age)

print(type(age))
```

**Output:**
```
<class 'str'>
```