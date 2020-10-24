import math
'''
inputCnt = input('추 갯수 >> ')

inputArr = []
for i in range(int(inputCnt)) :
    inputArr.append(input(str(i) + '번째 추 무게 >> '))
'''

'''
왼쪽, 오른쪽 나눠서 두개를  -왼쪽 +오른쪽 해서 나오는 숫자 전부다..

왼 :: 오
아무것도 없을때 오른쪽 갯수들 숫자 저장
왼에 추 하나씩 올라갔을때 더했을때 숫자 저장
왼에 추 두개씩 ...
loop...

ex 1,2,6

0 : 1
0 : 2
0 : 6
0 : 1+2
0 : 1+6
0 : 2+6
0 : 1+2+6
1 : 2
1 : 6
1 : 2+6

'''

'''
1,2,3,4

1
2
3
4
12
13
14
23
24
34
123
124
134
234
1234

'''
print(math.factorial(4) +1)

def solution() :
    left = 0
    right = 0


def loopFunc(left, arr) :
    while(len(arr)) :
        pass
        
