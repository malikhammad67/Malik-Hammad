# Data Types

## What are Data Types?

Data types define the type of value a variable stores. Python automatically identifies the data type when a value is assigned.

---

## Common Data Types

| Data Type | Description | Example |
|-----------|-------------|---------|
| `int` | Whole numbers | `20` |
| `float` | Decimal numbers | `5.8` |
| `str` | Text values | `"Python"` |
| `bool` | True or False values | `True` |

---

## Example

```python
age = 20            # int
height = 5.8        # float
name = "Ali"        # str
is_student = True   # bool
```

---

## Checking Data Type

Python uses the `type()` function to check the data type of a variable.

```python
name = "Ali"

print(type(name))
```

**Output:**
```python
<class 'str'>
```

---

## Type Conversion

Type conversion is the process of changing one data type into another.

```python
num = "100"

num = int(num)

print(num)
```

**Output:**
```python
100
```

---

## Key Points

- Python automatically detects data types.
- Variables can store different types of values.
- `type()` is used to check data types.
- Type conversion changes one data type into another.

---

# Practice

## 1. Create an integer variable and check its type.

```python
age = 20

print(type(age))
```

**Output:**
```python
<class 'int'>
```

---

## 2. Convert a string number into an integer.

```python
number = "50"

number = int(number)

print(number)
```

**Output:**
```python
50
```

---

## 3. Create variables of different data types.

```python
name = "Ali"
height = 5.8
student = True

print(type(name))
print(type(height))
print(type(student))
```

**Output:**
```python
<class 'str'>
<class 'float'>
<class 'bool'>
```