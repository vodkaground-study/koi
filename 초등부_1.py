'''
n개의 막대기에대한 높이정보가 주어질때, 오른쪽에서 보면 몇개가 보이나?
'''

# 2 <= n <= 100,000
stick_cnt = int(input('막대기 개수 >> '))

# 각각의 막대기 높이 입력 :: 1 <= h <= 100,000
stick_height = []

for i in range(stick_cnt) :
    stick_height.append(int(input(str(i) + "번째 막대기 높이 >> ")))

def solution() :
    viewHeight = 0
    viewCnt = 0
    stick_height.reverse()
    for item in stick_height :
        if viewCnt == 0 :
            viewHeight = item
            viewCnt += 1
        else :
            if item > viewHeight :
                viewHeight = item
                viewCnt += 1
    
    print('총 보이는 갯수 : ', viewCnt)

if __name__ == '__main__': 
    solution()

