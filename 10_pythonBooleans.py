# Python Booleans

## What is a Boolean?

A Boolean is a data type that has only **two values**:

- `True`
- `False`

Booleans are commonly used in conditions and comparisons.

---

## Creating Boolean Values

```python
x = True
y = False

print(x)
print(y)
```

**Output:**
```
True
False
```

---

## Boolean with Comparison Operators

Comparison operators return either `True` or `False`.

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal to | `5 == 5` |
| `!=` | Not equal to | `5 != 3` |
| `>` | Greater than | `10 > 5` |
| `<` | Less than | `5 < 10` |
| `>=` | Greater than or equal to | `10 >= 10` |
| `<=` | Less than or equal to | `5 <= 8` |

---

## Examples

### Equal To

```python
print(10 == 10)
```

**Output:**
```
True
```

---

### Not Equal To

```python
print(10 != 5)
```

**Output:**
```
True
```

---

### Greater Than

```python
print(20 > 15)
```

**Output:**
```
True
```

---

### Less Than

```python
print(8 < 3)
```

**Output:**
```
False
```

---

## The `bool()` Function

The `bool()` function converts a value into a Boolean.

```python
print(bool(1))
print(bool(0))
```

**Output:**
```
True
False
```

---

## Truthy and Falsy Values

Some values automatically become `True` or `False` when using `bool()`.

### Falsy Values

These values return `False`:

- `0`
- `0.0`
- `""` (Empty String)
- `[]` (Empty List)
- `()` (Empty Tuple)
- `{}` (Empty Dictionary)
- `set()` (Empty Set)
- `None`
- `False`

Example:

```python
print(bool(""))
print(bool([]))
print(bool(0))
```

**Output:**
```
False
False
False
```

---

### Truthy Values

Almost everything else returns `True`.

Example:

```python
print(bool("Python"))
print(bool(100))
print(bool([1, 2, 3]))
```

**Output:**
```
True
True
True
```

---

## Boolean in `if` Statements

Booleans are mostly used in decision-making.

```python
age = 18

if age >= 18:
    print("You can vote.")
```

**Output:**
```
You can vote.
```

---

## Using Boolean Operators

| Operator | Description |
|----------|-------------|
| `and` | Returns `True` if both conditions are true |
| `or` | Returns `True` if at least one condition is true |
| `not` | Reverses the Boolean value |

---

### `and` Example

```python
print(10 > 5 and 8 > 3)
```

**Output:**
```
True
```

---

### `or` Example

```python
print(10 > 20 or 5 < 8)
```

**Output:**
```
True
```

---

### `not` Example

```python
print(not True)
print(not False)
```

**Output:**
```
False
True
```

---

## Key Points

- A Boolean has only two values: `True` and `False`.
- Comparison operators always return a Boolean value.
- The `bool()` function converts values into `True` or `False`.
- Empty values are usually `False`.
- Non-empty values are usually `True`.
- Booleans are commonly used with `if` statements and logical operators.

---

# Practice

### 1. Check if two numbers are equal.

```python
print(15 == 15)
```

**Output:**
```
True
```

---

### 2. Convert a number to Boolean.

```python
print(bool(25))
```

**Output:**
```
True
```

---

### 3. Check an empty string.

```python
print(bool(""))
```

**Output:**
```
False
```

---

### 4. Use the `and` operator.

```python
print(5 < 10 and 8 > 2)
```

**Output:**
```
True
```

---

### 5. Use the `not` operator.

```python
print(not False)
```

**Output:**
```
True
```