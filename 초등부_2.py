#회문 0, 유사회문(한문자만 삭제하면 되는 회문) 1, 둘다아니면 2

#ispalindrome

'''
abba        0
summuus     1
xabba       1
xabbay      2
comcom      2
comwwmoc    0
comwwtmoc   1
'''

'''
앞글자 <> 뒷글자 하나씩비교

if 다르면
    그다음글자와 비교, 그래도 다르면 break 다음글자 ..

    그 다음글자부터 다시 시작..?
'''

pString = input('입력 >> ')
reversePString = pString[::-1]

#print("reversePString :: ", reversePString)

#lenPString = round(len(pString)/2)
lenPString = int(len(pString)/2)
#lenPString = len(pString)
#print("lenPString :: ", lenPString)

def isPlindrome() :
    differCnt = 0
    revCnt = 0
    returnNum = 0
    for i in range(lenPString) :
        if returnNum != 2 :
            if(pString[i] == reversePString[revCnt]) :
                revCnt += 1
            else :
                differCnt += 1
                if differCnt >= 2 :
                    returnNum = 2
                else :
                    returnNum = 1
        
    return returnNum


if __name__ == '__main__': 
    print(isPlindrome())