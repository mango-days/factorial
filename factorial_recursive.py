def factorial(number):
  if number!=1:
    return number*factorial(number-1)
  return 1

number = int(input())
print(factorial(number))