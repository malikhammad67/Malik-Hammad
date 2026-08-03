# Python Variables

## What is a Variable?
A **variable** is a name used to store data in memory. We can access or update its value whenever needed.

### Syntax
```python
variable_name = value
```

### Example
```python
name = "Ali"
age = 20

print(name)
print(age)
```

---

## Variable Naming Rules

✅ Can:
- Start with a letter or `_`
- Contain letters, numbers, and underscores

❌ Cannot:
- Start with a number
- Contain spaces or special characters
- Use Python keywords (`if`, `for`, `class`, etc.)

**Example**
```python
student_name = "Ali"   # ✔ Valid
_age = 20              # ✔ Valid
# 1name = "Ali"        # ✘ Invalid
```

---

## Updating a Variable

```python
name = "Ali"
name = "Ahmed"

print(name)
```

**Output**
```
Ahmed
```

---

## Multiple Assignment

```python
x, y, z = 10, 20, 30
```

Or assign the same value:

```python
a = b = c = 100
```

---

## Check Data Type

```python
age = 20
print(type(age))
```

---

## Best Practices

- Use meaningful names.
- Follow **snake_case** (`student_name`).
- Avoid single-letter variable names.
- Keep names simple and readable.

---

## Key Points

- Variables store data.
- Use `=` to assign values.
- Values can be changed anytime.
- Python is **case-sensitive** (`name` ≠ `Name`).