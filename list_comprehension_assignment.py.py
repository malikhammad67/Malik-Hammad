
# python Practical Assignment: 
#List Comprehension


## Part A: Basic Questions

### Q1. Create a list of numbers from *1 to 10* using list comprehension.

numbers = []
for x in range(1, 11):
    numbers.append(x)
print(numbers)


### Q2. Create a list of *squares* of numbers from *1 to 10*.

squares = [x**2 for x in range(1, 11)]

print(squares)


### Q3. Create a list of *cubes* of numbers from *1 to 10*.

cubes = [i**3 for i in range(1, 11)]
print(cubes)

### Q4. Create a list of *even numbers* from *1 to 20*.
even_numbers = [i for i in range(1, 21) if i % 2 == 0]

print(even_numbers)


### Q5. Create a list of *odd numbers* from *1 to 20*.

odd_numbers = [i for i in range(1, 21) if i % 2 != 0]

print(odd_numbers)

## Part B: Conditional List Comprehension

### Q6. From the list below, create a new list containing only numbers greater than *20*.

# python
# numbers = [5, 12, 25, 30, 18, 45, 10, 60]

numbers = [5, 12, 25, 30, 18, 45, 10, 60]

new_list = [i for i in numbers if i > 20]

print(new_list)

### Q7. Create a list containing only the *positive numbers*.

# python
# nums = [-5, 10, -8, 15, 20, -3, 7]
#

nums = [-5, 10, -8, 15, 20, -3, 7]

positive_numbers = [i for i in nums if i > 0]

print(positive_numbers)


### Q8. Convert the following words into *uppercase*.
#
# python
# words = ["python", "java", "c++", "javascript"]



words = ["python", "java", "c++", "javascript"]

uppercase_words = [word.upper() for word in words]

print(uppercase_words)




### Q9. Find the *length* of each word.

# python
# words = ["apple", "banana", "grapes", "kiwi"]


words = ["apple", "banana", "grapes", "kiwi"]

lengths = [len(word) for word in words]

print(lengths)


### Q10. Create a list of numbers from *1 to 20* that are divisible by *3*.

numbers = [i for i in range(1, 21) if i % 3 == 0]

print(numbers)

## Part C: String Practice

### Q11. Create a list containing each character of the word:

# python
# word = "PYTHON"


word = "PYTHON"

letters = [char for char in word]

print(letters)


### Q12. Remove all vowels from the following word using list comprehension.

# python
# word = "Programming"

word = "Programming"

result = [char for char in word if char.lower() not in "aeiou"]

print(result)


## Part D: Mixed Practice

### Q13. Create a list of squares of only the *even numbers* from *1 to 20*.

squares = [i * i for i in range(1, 21) if i % 2 == 0]

print(squares)

### Q14. From the following list, create a new list containing words with more than *5 letters*.

# python
# fruits = ["apple", "banana", "kiwi", "watermelon", "orange", "pear"]


fruits = ["apple", "banana", "kiwi", "watermelon", "orange", "pear"]

new_list = [fruit for fruit in fruits if len(fruit) > 5]

print(new_list)

## Q15. Replace negative numbers with *0*.


# numbers = [-5, 10, -3, 8, -1, 15]


numbers = [-5, 10, -3, 8, -1, 15]

new_list = [0 if i < 0 else i for i in numbers]

print(new_list)

## Bonus Challenge

### Q16. Create the following multiplication table using list comprehension.



table = [5 * i for i in range(1, 11)]

print(table)

### Q17. Create a list of all numbers between *1 and 50* that are divisible by *5 and 7*.

numbers = [i for i in range(1, 51) if i % 5 == 0 and i % 7 == 0]

print(numbers)


### Q18. Create a list of the first letter of each word.



names = ["Ali", "Ahmed", "Sara", "Fatima", "Usman"]

first_letters = [name[0] for name in names]

print(first_letters)