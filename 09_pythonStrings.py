# Python Strings

## What is a String?

A string is a sequence of characters enclosed in single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` / `""" """`).

Strings are used to store text.

---

## Creating Strings

```python
name = "Ali"
city = 'Lahore'
message = """Welcome to Python"""
```

---

## String Indexing

Each character in a string has an index number.

```python
text = "Python"

print(text[0])
print(text[1])
print(text[-1])
```

**Output:**
```
P
y
n
```

---

## String Slicing

Slicing is used to get a part of a string.

**Syntax:**

```python
string[start:end]
```

Example:

```python
text = "Python"

print(text[0:3])
print(text[2:6])
print(text[:4])
print(text[3:])
```

**Output:**
```
Pyt
thon
Pyth
hon
```

---

## String Length

Use the `len()` function to find the length of a string.

```python
text = "Python"

print(len(text))
```

**Output:**
```
6
```

---

## Common String Methods

| Method | Description | Example |
|---------|-------------|---------|
| `upper()` | Converts to uppercase | `"python".upper()` |
| `lower()` | Converts to lowercase | `"PYTHON".lower()` |
| `title()` | First letter of each word uppercase | `"hello world".title()` |
| `capitalize()` | First letter uppercase | `"python".capitalize()` |
| `strip()` | Removes extra spaces | `" hello ".strip()` |
| `replace()` | Replaces text | `"Python".replace("P","J")` |
| `find()` | Finds the index of a character | `"Python".find("t")` |
| `count()` | Counts occurrences | `"banana".count("a")` |

---

## Examples

### Convert to Uppercase

```python
text = "python"

print(text.upper())
```

**Output:**
```
PYTHON
```

---

### Convert to Lowercase

```python
text = "PYTHON"

print(text.lower())
```

**Output:**
```
python
```

---

### Replace Text

```python
text = "Python"

print(text.replace("Python", "Java"))
```

**Output:**
```
Java
```

---

### Find a Character

```python
text = "Python"

print(text.find("t"))
```

**Output:**
```
2
```

---

### Count Characters

```python
text = "banana"

print(text.count("a"))
```

**Output:**
```
3
```

---

## String Concatenation

Concatenation means joining two or more strings using the `+` operator.

```python
first = "Hello"
second = "World"

print(first + " " + second)
```

**Output:**
```
Hello World
```

---

## String Repetition

Use the `*` operator to repeat a string.

```python
text = "Hi "

print(text * 3)
```

**Output:**
```
Hi Hi Hi
```

---

## Checking String Content

Use these methods to check the content of a string.

| Method | Description |
|---------|-------------|
| `isalpha()` | Checks if all characters are letters |
| `isdigit()` | Checks if all characters are digits |
| `isalnum()` | Checks if letters and numbers only |
| `isspace()` | Checks if string contains only spaces |

Example:

```python
text = "Python"

print(text.isalpha())
```

**Output:**
```
True
```

---

## Escape Characters

Escape characters are used to include special characters in a string.

| Escape Character | Description |
|------------------|-------------|
| `\n` | New line |
| `\t` | Tab space |
| `\"` | Double quote |
| `\'` | Single quote |
| `\\` | Backslash |

Example:

```python
print("Hello\nWorld")
```

**Output:**
```
Hello
World
```

---

## Key Points

- Strings store text data.
- Strings are enclosed in single, double, or triple quotes.
- Indexing starts from `0`.
- Negative indexing starts from `-1`.
- Slicing extracts a portion of a string.
- Strings are immutable (cannot be changed directly).
- Many built-in methods make string manipulation easy.

---

# Practice

### 1. Print the first character of a string.

```python
text = "Python"

print(text[0])
```

**Output:**
```
P
```

---

### 2. Convert a string to uppercase.

```python
text = "python"

print(text.upper())
```

**Output:**
```
PYTHON
```

---

### 3. Find the length of a string.

```python
text = "Programming"

print(len(text))
```

**Output:**
```
11
```

---

### 4. Replace one word with another.

```python
text = "I like Python"

print(text.replace("Python", "Java"))
```

**Output:**
```
I like Java
```

---

### 5. Join two strings.

```python
first = "Hello"
second = "Python"

print(first + " " + second)
```

**Output:**
```
Hello Python
```