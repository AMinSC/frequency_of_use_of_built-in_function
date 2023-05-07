## 구글 입사문제 중에서

-   링크 : https://codingdojang.com/scode/393
-   python

```py
str(list(range(10000))).count('8')
```

-   js

```js
Array(10000).fill(0).map((v, i) => i).toString().split('').filter(v => v === '8').length
```

## 다음 입사문제 중에서

-   링크 : https://codingdojang.com/scode/408
-   python

```py
s = [1, 3, 4, 8, 13, 17, 20]
index = 0
minim = float('inf') #float('-inf')
for i in range(1, len(s)):
    if (s[i] - s[i-1]) < minim:
        index = i
        minim = s[i] - s[i-1]

s[index-1], s[index]

s = [1, 3, 4, 8, 13, 17, 20]
ss = s[1:]
sorted(zip(s, ss), key=lambda x:x[1]-x[0])[0]
```

## 문자열 압축하기

-   링크 : https://codingdojang.com/scode/465
-   python

```py
s = 'aaabbcccccca'

result = s[0]
count = 0

for string in s:
    print(result)
    if string == result[-1]:
        count += 1
    else:
        result += str(count) + string
        count = 1

result += str(count)
result

###

import re

s = 'aaabbcccccca'
p = re.compile('(\w)(\\1*)') # \w는 문자 클래스 \1은 재참조 메타문자, *는 0번또는 여러번
p.findall(s)
```

## Special Sort

-   링크 : https://codingdojang.com/scode/414
-   python

```py
def solution(value):
    return [i for i in value if i < 0] + [i for i in value if i >= 0]

solution([-1, 1, 3, -2, 2])
```

## 숫자 출력하기

-   링크 : https://codingdojang.com/scode/471
-   python

```py
# 32진수가 맥시멈


int('aa', 16)
int('aa', 32)

chr(32)
chr(33)
ord(32)
ord(33)

bin(20150111), oct(20150111), hex(20150111)
format(20150111, 'b'), format(20150111, 'o'), format(20150111, 'x')
print(int('j6tqv', ord(' '))) # js로 진법 변환
# let number = 20150111;
# let test = number.toString(16);
# let test = number.toString(32);
# let test = number.toString(33);

ord('!')
print(int('gwnae', ord('!')))
```

## 아마존 면접문제 중에서

-   링크 : https://codingdojang.com/scode/416
-   python

```py
def solution(l):
    n = len(l) // 2
    return list(zip(l[:n], l[n:]))

l = ['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5']
sum(solution(l), ()) 
# sum(iterable, start)

def solution(l):
    n = len(l)//2
    l[::2], l[1::2] = l[:n], l[n:]

l = ['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5']
solution(l)
l


```

## 가성비 최대화

-   링크 : https://codingdojang.com/scode/490
-   python

```py
가격 = 10
성능 = 150
부품가격 = 3
부품성능 = [30, 70, 15, 40, 65]

부품성능.sort(reverse=True)

for i in 부품성능 :
    if  성능 / 가격 > ( 성능 + i ) / ( 가격 + 부품가격 )  :
        break
    else: 
        성능 += i
        가격 += 부품가격

print(int( 성능 / 가격 ))
```

## 그 시간 사무실에 몇 명이 있었나?

-   링크 : https://codingdojang.com/scode/418
-   python

```py
# 시간이라고 해서 꼭 시간으로 비교할 필요는 없음
t = ''.join(input().split(':'))
count = 0

log = '''09:12:23 11:14:35
10:34:01 13:23:40
10:34:31 11:20:10'''

logs = log.split('\n')
for log in logs:
    l = [''.join(time.split(':')) for time in log.split()]
    # print(l)
    if l[0] <= t <= l[1]:
        count += 1

count
#10:35:00
#11:21:00
#13:25:00
```

## 120번째 죄수

-   링크 : https://codingdojang.com/scode/525
-   python

```py
room = [-1] * 120

for i in range(1, 121):
    for n in range(1, 121):
        if n % i == 0:
            room[n-1] *= -1

room.count(1)
```

## 

-   링크 : 
-   python

```py
def OneEditApart(a, b):
    while a and b:
        if a[-1] == b[-1]:
            a = a[:-1]
            b = b[:-1]
            continue
        elif a[0] == b[0]:
            a = a[1:]
            b = b[1:]
            continue
        else:
            break
    return len(a) <= 1 and len(b) <= 1

print(OneEditApart("cat", "dog"))
print(OneEditApart("cat", "cats"))
print(OneEditApart("cat", "cut"))
print(OneEditApart("cat", "cast"))
print(OneEditApart("cat", "at"))
print(OneEditApart("cat", "acts")) 
```

## Subdate

-   링크 : https://codingdojang.com/scode/394
-   python

```py
def subdate(date):
    년 = int(date[:4])
    월 = int(date[4:6])
    일 = int(date[6:])
    월별일 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    일수 = 년 * 365 + 일
    for i in range(1, 월):
        일수 += 월별일[i]
    return 일수

def solution(a, b):
    return abs(subdate(a) - subdate(b))

solution('20070515', '20070501') #14
solution('20070301', '20070515') #75
```

## Happy Number

-   링크 : https://codingdojang.com/scode/496
-   python

```py
testcase = [3, 7, 4, 13]
def happyNumber(입력숫자):
    더할숫자 = []
    더한숫자 = 입력숫자
    제곱의합리스트 = []
    while(더한숫자 != "1"):
        for i in range(len(더한숫자)):
            a = int(더한숫자[i]) * int(더한숫자[i])
            더할숫자.append(a)
        더한숫자 = str(sum(더할숫자))
        print(더할숫자, 제곱의합리스트)
        더할숫자 = []
        if 더한숫자 == 입력숫자: 
            return False
        if 더한숫자 in 제곱의합리스트:
            return False
        제곱의합리스트.append(더한숫자)
    return True

for i, number in enumerate(testcase):
    if happyNumber(str(number)):
        print(f'Case #{(str(i+1))}: {number} is a Happy number.')
    else:
        print(f'Case #{(str(i+1))}: {number} is an Unhappy number.')
'''
[9] []
[81] ['9']
[64, 1] ['9', '81']
[36, 25] ['9', '81', '65']
[36, 1] ['9', '81', '65', '61']
[9, 49] ['9', '81', '65', '61', '37']
[25, 64] ['9', '81', '65', '61', '37', '58']
[64, 81] ['9', '81', '65', '61', '37', '58', '89']
[1, 16, 25] ['9', '81', '65', '61', '37', '58', '89', '145']
[16, 4] ['9', '81', '65', '61', '37', '58', '89', '145', '42']
[4, 0] ['9', '81', '65', '61', '37', '58', '89', '145', '42', '20']
[16] ['9', '81', '65', '61', '37', '58', '89', '145', '42', '20', '4']
[1, 36] ['9', '81', '65', '61', '37', '58', '89', '145', '42', '20', '4', '16']
Case #1: 3 is an Unhappy number.
[49] []
[16, 81] ['49']
[81, 49] ['49', '97']
[1, 9, 0] ['49', '97', '130']
[1, 0] ['49', '97', '130', '10']
Case #2: 7 is a Happy number.
[16] []
[1, 36] ['16']
[9, 49] ['16', '37']
[25, 64] ['16', '37', '58']
[64, 81] ['16', '37', '58', '89']
[1, 16, 25] ['16', '37', '58', '89', '145']
[16, 4] ['16', '37', '58', '89', '145', '42']
[4, 0] ['16', '37', '58', '89', '145', '42', '20']
Case #3: 4 is an Unhappy number.
[1, 9] []
[1, 0] ['10']
Case #4: 13 is a Happy number.
'''
```

## Ugly Numbers

-   링크 : https://codingdojang.com/scode/436
-   python

```py
def uglyNumber(n):
    ugly_number_list = [1]
    for i in range(n-1):
        last = ugly_number_list[-1]

        temp = []
        for i in ugly_number_list:
            for j in [i*2, i*3, i*5]:
                if j > last:
                    temp.append(j)

        ugly_number_list.append(min(temp))
    return ugly_number_list[-1]

uglyNumber(1500)
```

## Two Printers

-   링크 : https://codingdojang.com/scode/449
-   python

```py
def two_printers(x, y, page):
    time = 1
    while True:
        if time // x + time // y >= page:
            return time
        time+=1

two_printers(1, 1, 5) #3
two_printers(3, 5, 4) #9
two_printers(1, 100, 1) #1
two_printers(1, 100, 2) #2
```

## tic-tac-toe game

-   링크 : https://codingdojang.com/scode/464
-   python

```py
import numpy as np

board = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
marker = ['X', 'O']
player = 0

def printBoard():
    for i in board:
        print(f'| {" | ".join(i)} |')


def checkWinner():
    if board[0][0] == board[1][1] == board[2][2]:
        printBoard()
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        printBoard()
        return board[0][2]
    else:
        for i in range(3):
            if len(set([board[0][i], board[1][i], board[2][i]])) == 1:
                printBoard()
                return board[0][i]
            elif len(set([board[i][0], board[i][1], board[i][2]])) == 1:
                printBoard()
                return board[i][0]
    if len(np.unique(board)) == 2:
        printBoard()
        return 'Draw'
    return False


def solution():
    printBoard()
    position = input()
    pos = np.where(board == position)

    if list(pos[0]):
        board[pos[0][0]][pos[1][0]] = marker[player]

    ch = checkWinner()
    if ch:
        if ch == 'Draw':
            print('비김!')
        else:
            print(ch, '이김!')
        return False
    return True

while solution():
    player ^= 1


## 참고사항 ##
test = [1, 2, 3, 4]

def t():
    test[1] = 1000

t()
test


board = np.array([['1','2','3'],['4','5','6'],['7','8','9']])
# 있는 값
pos = np.where(board == '3')
pos
pos[0]
pos[0][0]

pos[1]
pos[1][0]

# 없는 값
pos = np.where(board == '33')
pos
pos[0]
list(pos[0])
```

## 

-   링크 : 
-   python

```py

```

-   js

```js

```

## 

-   링크 : 
-   python

```py

```

-   js

```js

```

## 

-   링크 : 
-   python

```py

```

-   js

```js

```