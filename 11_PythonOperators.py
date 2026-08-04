# Python Operators

## What are Operators?

Operators are special symbols used to perform operations on variables and values.

Example:

```python
a = 10
b = 5

print(a + b)
```

**Output:**
```
15
```

---

# Types of Operators in Python

Python has the following types of operators:

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Identity Operators
- Membership Operators
- Bitwise Operators

---

# 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 3` |
| `-` | Subtraction | `5 - 3` |
| `*` | Multiplication | `5 * 3` |
| `/` | Division | `10 / 2` |
| `%` | Modulus (Remainder) | `10 % 3` |
| `**` | Exponent (Power) | `2 ** 3` |
| `//` | Floor Division | `10 // 3` |

---

## Examples

### Addition

```python
print(10 + 5)
```

**Output:**
```
15
```

---

### Division

```python
print(10 / 2)
```

**Output:**
```
5.0
```

---

### Modulus

```python
print(10 % 3)
```

**Output:**
```
1
```

---

### Exponent

```python
print(2 ** 4)
```

**Output:**
```
16
```

---

### Floor Division

```python
print(10 // 3)
```

**Output:**
```
3
```

---

# 2. Assignment Operators

Assignment operators are used to assign values to variables.

| Operator | Example | Same As |
|----------|---------|---------|
| `=` | `x = 5` | Assign value |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 2` | `x = x - 2` |
| `*=` | `x *= 2` | `x = x * 2` |
| `/=` | `x /= 2` | `x = x / 2` |
| `%=` | `x %= 2` | `x = x % 2` |
| `**=` | `x **= 2` | `x = x ** 2` |
| `//=` | `x //= 2` | `x = x // 2` |

---

## Example

```python
x = 10

x += 5

print(x)
```

**Output:**
```
15
```

---

# 3. Comparison Operators

Comparison operators compare two values and return either `True` or `False`.

| Operator | Description |
|----------|-------------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

## Example

```python
print(20 > 10)
print(5 == 3)
```

**Output:**
```
True
False
```

---

# 4. Logical Operators

Logical operators combine multiple conditions.

| Operator | Description |
|----------|-------------|
| `and` | True if both conditions are true |
| `or` | True if at least one condition is true |
| `not` | Reverses the Boolean value |

---

## Examples

### `and`

```python
print(10 > 5 and 20 > 15)
```

**Output:**
```
True
```

---

### `or`

```python
print(5 > 10 or 8 < 12)
```

**Output:**
```
True
```

---

### `not`

```python
print(not True)
```

**Output:**
```
False
```

---

# 5. Identity Operators

Identity operators check whether two variables refer to the same object.

| Operator | Description |
|----------|-------------|
| `is` | Returns `True` if both objects are the same |
| `is not` | Returns `True` if objects are different |

---

## Example

```python
x = [1, 2]
y = x

print(x is y)
```

**Output:**
```
True
```

---

# 6. Membership Operators

Membership operators check whether a value exists in a sequence.

| Operator | Description |
|----------|-------------|
| `in` | Returns `True` if value exists |
| `not in` | Returns `True` if value does not exist |

---

## Example

```python
text = "Python"

print("P" in text)
print("z" in text)
```

**Output:**
```
True
False
```

---

# 7. Bitwise Operators

Bitwise operators perform operations on binary numbers.

| Operator | Description |
|----------|-------------|
| `&` | AND |
| `|` | OR |
| `^` | XOR |
| `~` | NOT |
| `<<` | Left Shift |
| `>>` | Right Shift |

---

## Example

```python
print(5 & 3)
```

**Output:**
```
1
```

---

# Operator Precedence

Python follows the order of operations.

| Priority | Operators |
|----------|-----------|
| Highest | `()` |
| | `**` |
| | `*`, `/`, `//`, `%` |
| | `+`, `-` |
| | Comparison Operators |
| | `not` |
| | `and` |
| Lowest | `or` |

Example:

```python
print(5 + 2 * 3)
```

**Output:**
```
11
```

---

# Key Points

- Operators perform operations on values and variables.
- Arithmetic operators are used for calculations.
- Assignment operators update variable values.
- Comparison operators return `True` or `False`.
- Logical operators combine conditions.
- Identity operators compare object identity.
- Membership operators check whether a value exists.
- Bitwise operators work with binary values.

---

# Practice

### 1. Add two numbers.

```python
a = 12
b = 8

print(a + b)
```

**Output:**
```
20
```

---

### 2. Find the remainder.

```python
print(17 % 5)
```

**Output:**
```
2
```

---

### 3. Compare two numbers.

```python
print(15 >= 10)
```

**Output:**
```
True
```

---

### 4. Check membership.

```python
text = "Python"

print("o" in text)
```

**Output:**
```
True
```

---

### 5. Use a logical operator.

```python
print(8 > 5 and 12 > 10)
```

**Output:**
```
True
```