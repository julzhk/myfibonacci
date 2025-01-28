A basic library that calculates Fibonacci numbers

worked example from the book : https://learning.oreilly.com/library/view/speed-up-your/9781801811446/

install with 

```
pip install git+https://github.com/julzhk/myfibonacci@master
```


usage: 
```python
from myfibonacci_py.fib_calcs.fib_numbers import recurring_fibonacci_number
from myfibonacci_py.fib_calcs.fib_numbers import calculate_numbers

print(recurring_fibonacci_number(15))
# 610

print( calculate_numbers([1, 2, 3, 4, 5, 6, 7]))

# [1, 1, 2, 3, 5, 8, 13]

```

from command line:
    
    ```bash
fib-number --number 11
# 89
```