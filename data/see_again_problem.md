## 몫 구하기

-   링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120805
-   python

```py
def solution(num1, num2):
    return num1 // num2
```

## 배열의 평균값

-   링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120817
-   python

```py
def solution(numbers):
    return sum(numbers)/len(numbers)

# 다차원 배열의 합도 구할 수 있음
import numpy as np

def solution(numbers):
    return np.sum(numbers)/len(numbers)
```

## 문자열안에 문자열

-   링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120908
-   python

```py
def solution(str1, str2):
    return 2 if str1.find(str2) == -1 else 1

def solution(str1, str2):
    return 1 if str2 in str1 else 2
```

## 숨어있는 숫자의 덧셈 (1)

-   링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120851
-   python

```py
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isnumeric():
            answer += int(i)
    return answer

def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())

import re

def solution(my_string):
    return sum(int(n) for n in re.sub('[^1-9]', '', my_string))
```

## 진료순서 정하기

-   링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120835
-   python

```py
arr = [3, 76, 24]
#응급순서 = [76, 24, 3]
응급순서 = sorted(arr, reverse=True)
list(map(lambda x: 응급순서.index(x) + 1, arr))

def solution(arr):
    응급순서 = sorted(arr, reverse=True)
    return list(map(lambda x: 응급순서.index(x) + 1, arr))

def solution(emergency):
    응급순서 = sorted(emergency, reverse=True)
    return [응급순서.index(i) + 1 for i in emergency]
```

## 문자열 밀기

-   링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120921
-   python

```py
import collections

def solution(A, B):
    if A == B:
        return 0
    비교 = collections.deque(A)
    for i in range(len(A)):
        비교.rotate(1)
        if ''.join(비교) == B:
            return i+1
    return -1


solution=lambda a,b:(b*2).find(a)


def solution(A, B):
    #if A == "":
    #    return 0

    AA = A+A
    answer = AA.find(B)

    if answer >0:
        answer = len(A) - answer

    return answer
```

## 특이한 정렬

-   링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120880
-   python

```py
def solution(numlist, n):
    d = [[i, abs(i-n)] for i in numlist]
    return list(map(lambda x:x[0], sorted(d, key=lambda x:(x[1], -x[0]))))

def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer

# {i:i-n for i in numlist}
# [[i, i-n] for i in numlist]
# sorted(d, key=lambda x:x[1])
# sorted(d, key=lambda x:(x[1], -x[0])) # 다중조건
```

## 다항식 더하기

-   링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120863
-   python

```py
def solution(polynomial):
    # 양수만 고려했어도 됨.
    x = polynomial.split(' ')
    x항 = 0
    일반항 = 0
    for i, value in enumerate(x):
        if 'x' in value:
            if len(value) == 1:
                if x[i-1] == '+' or i == 0:
                    x항 += 1
            else:
                if x[i-1] == '+' or i == 0:
                    x항 += int(value[:-1])
        elif value != '+':
            일반항 += int(value)

    if 일반항 == 0 and x항 == 0:
        return f'0'
    elif 일반항 == 0 and x항 != 0:
        if x항 == 1:
            return 'x'
        return f'{x항}x'
    elif 일반항 != 0 and x항 == 0:
        return f'{일반항}'
    elif 일반항 < 0 and x항 > 0:
        if x항 == 1:
            return f'x - {일반항}'
        return f'{x항}x - {일반항}'
    elif 일반항 > 0 and x항 > 0:
        if x항 == 1:
            return f'x + {일반항}'
        return f'{x항}x + {일반항}'
    elif 일반항 > 0 and x항 < 0:
        if x항 == -1:
            return f'-x + {일반항}'
        return f'-{x항}x + {일반항}'
    elif 일반항 < 0 and x항 < 0:
        if x항 == -1:
            return f'-x + {일반항}'
        return f'-{x항}x + {일반항}'
```

## OX퀴즈

-   링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120907
-   python

```py
def solution(quiz):
    answer = []
    for i in quiz:
        c = i.split('=')
        for j in range (len(c)):
            if eval(c[0]) == eval(c[1]):
                answer.append('O')
                break
            else:
                answer.append('X')
                break
    return answer



def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]
```

## 겹치는 선분의 길이

-   링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120876
-   python

```py
# 오답
def solution(lines):
    하나, 둘, 셋 = lines
    길이 = []
    if 하나[1] <= 둘[0]:
        pass
    else:
        길이.append([min(둘[1], 하나[1]), max(둘[0], 하나[0])])
    if 하나[1] <= 셋[0]:
        pass
    else:
        길이.append([min(하나[1], 셋[1]), max(하나[0], 셋[0])])
    if 둘[1] <= 셋[0]:
        pass
    else:
        길이.append([min(셋[1], 둘[1]), max(셋[0], 둘[0])])

    # [길이[0][0], 길이[1][0], 길이[2][0]]
    # [길이[0][1], 길이[1][1], 길이[2][1]]
    if 길이 == []:
        return 0
    # 중간에 끊어진 경우가 있을 수 있음, test case 1번과 9번 통과 못함
    # 반례 : [[0, 5], [3, 9], [8, 9]]
    시작 = [i[0] for i in 길이]
    끝 = [i[1] for i in 길이]
    print(길이)
    # return max(시작) - min(끝)

solution([[0, 5], [3, 9], [8, 9]])
solution([[0, 5], [3, 9], [1, 10]])
solution([[0, 1], [2, 5], [3, 9]])

# 정답
def solution(lines):
    lines.sort(key=lambda x:x[1])
    하나, 둘, 셋 = lines
    길이 = []
    if 하나[1] <= 둘[0]:
        pass
    else:
        길이.append([max(둘[0], 하나[0]), min(둘[1], 하나[1])])
    if 하나[1] <= 셋[0]:
        pass
    else:
        길이.append([max(하나[0], 셋[0]), min(하나[1], 셋[1])])
    if 둘[1] <= 셋[0]:
        pass
    else:
        길이.append([max(셋[0], 둘[0]), min(셋[1], 둘[1])])

    if 길이 == []:
        return 0
    print(길이)
    l = 길이
    # 중간에 끊어진 경우가 있을 수 있음, test case 1번과 9번 통과 못함
    # 반례 : [[0, 5], [3, 9], [8, 9]]
    if len(l) == 1:
        return l[0][1] - l[0][0]
    elif len(l) == 2:
        if l[0][1] <= l[1][0]:
            return (l[0][1] - l[0][0]) + (l[1][1] - l[1][0])
        else:
            return max(l[1]) - min(l[0])
    elif len(l) == 3:
        # 겹치지 않고 and 겹치지 않는다
        if l[0][1] <= l[1][0] and l[1][1] <= l[2][0]:
            return (l[0][1] - l[0][0]) + (l[1][1] - l[1][0]) + (l[2][1] - l[2][0])
        # 모두 겹친다
        elif l[0][1] > l[1][0] and l[1][1] > l[2][0]:
            시작 = [i[0] for i in l]
            끝 = [i[1] for i in l]
            return max(끝) - min(시작)
        # 부분적으로 겹친다
        else:
            # 겹치지 않고 and 겹친다
            if l[0][1] <= l[1][0] and l[1][1] > l[2][0]:
                return (l[0][1] - l[0][0]) + (max(l[2]) - min(l[1]))
            # 겹치고 and 겹치지 않는다
            if l[0][1] > l[1][0] and l[1][1] <= l[2][0]:
                return (max(l[1]) - min(l[0])) + (l[2][1] - l[2][0])
            return max(l[2][1]) - min(l[0][1])


solution([[0, 1], [2, 5], [3, 9]])
solution([[0, 5], [3, 9], [8, 9]])
solution([[0, 5], [3, 9], [1, 10]])

# 정답 코드 2
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
```

