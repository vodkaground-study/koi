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

# 정보올림피아드 답임. dfs 스터디
def main():
	L = set()
	
	N = int(input())
	a = list(map(int, input().split()))
	t = sum(a)
	
	def dfs(x, s):
		if x == N:
			if 0 < s <= t:
				L.add(s)
		else:
			dfs(x+1, s-a[x])
			dfs(x+1, s)
			dfs(x+1, s+a[x])
	
	dfs(0, 0)
	
	print(t - len(L))

main()