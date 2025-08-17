def fibonacci_series(terms):
  first,second = 0, 1
  for i in range(terms):
    print(first, end=" ")
    first, second = second, first + second
    fibonacci_series(10)
