def fizz_buzz(n):
    return [ ('FizzBuzz' if not x % 15 else ('Fizz' if not x % 3 else ('Buzz' if not x % 5 else x) )) for x in range(1,n + 1) ]
