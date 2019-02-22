# Lab 1 - Python Introduction

## Exercises

### 1. Write a program to solve the example (|(a^2/b^2+c^2*a^2)/(a+b+c*(k-a/b^3))+c+(k/b-k/a)*c|). Provide a division by zero check.

Create the function `func` which receives an integer a,b,c,k as arguments and returns the expression value or Zero Division Error.

```python
func(1,2,3,4) # => 2.3675...
func(0,1,2,3) # => Zero Division Error
```

### 2. An arbitrary list is given, containing both strings and numbers. Print all even elements line by line.
