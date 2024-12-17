Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Create a loop with For and Range to go from 1 to 100.
... for number in range(1, 101):
...   # First check if the number is divisible by both 3 and 5.
...   if number % 3 == 0 and number % 5 == 0:
...     print("FizzBuzz")
...  
...   # Then check if the number is only divisible by 3
...   elif number % 3 == 0:
...     print("Fizz")
...  
...   # Finally check if the number is only divisible by 5
...   elif number % 5 == 0:
...     print("Buzz")
...  
...   # If it's not divisible by either of those numbers, just print the number
...   else:
...     print(number)
... 
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
