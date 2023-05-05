import re  # re module <- regex
from collections import Counter  # 사용 빈도 라이브러리


# 내부 함수 데이터 > 추후 txt 혹은 Crawling 개선
value = """
# 무한수
import math

math.factorial
math.gcd #최대공약수
math.pi
math.inf
-math.inf
math.nan
# 조합(import itertools로는 쌍을 구할 수 있음)
math.perm(n, r) n개 중 r개, 순열
math.comb(n, r) n개 중 r개, 조합

float("inf")
-float("inf")
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]

def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]

def solution(numbers):
    v = list(reversed(sorted(numbers)))
    return v[0] * v[1]
    
def solution(my_string):
    return sorted(int(i) for i in my_string if i.isdigit())
"""


# Built-in function list
func = ['abs', 'all', 'any', 'bin', 'bool', 'chr', 'dict',
        'dir', 'enumerate', 'eval', 'filter', 'float', 'globals',
        'help', 'hex', 'id', 'input', 'int', 'isinstance', 
        'issubclass', 'iter', 'len', 'list', 'locals', 'map',
        'max', 'min', 'next', 'object', 'oct', 'open', 'ord',
        'pow', 'print', 'property', 'range', 'repr', 'reversed',
        'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod'
        'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']


# frequency of use of built-in function
frequency_use = {}


for i in func:
    frequency_use[i] = len(re.findall(i, value))

# cnt = Counter(value)

# print(list(cnt.elements()))
print(frequency_use)