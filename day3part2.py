INPUT_S ='''/
110011110101

101010101101
111001111000
001011111101
101111010110
111110100011
111011111010
010101001111
000011001110
111010011011
110111111010
100011101110
000110111001
111010110101
010001011001
011011111111
111101001011
001111110001
110100001110
101000100001
101011001111
100110101010
100011101011
001000110100
'''

#For o2 generator : 
#Take for the position of the bit the most common bit from the input
#If there is the same number of 0 and 1, take 1
#Then keep only the numbers with this bit in this position


binary = [str(line) for line in INPUT_S.splitlines()]


def delNoLen(subList) :
    for i in subList :
        if len(i) == 0 or len(i) == 1 :
            subList.remove(i)
    return subList

def countMoreForIndex(index, listBin) :
    zero = 0
    one = 0
    for j in listBin :
        if( j[index] == '0') :
            zero += 1
        else :
            one += 1
    if zero > one :
        return '0'
    else :
        return '1'


def selectWithParam(param, index, listBin) :
    nbDel = 0
    subList = listBin.copy()
    for j in range(len(listBin)) :
        if listBin[j][index] != param :
            del subList[j - nbDel]
            nbDel += 1
    return subList

def findO2(listBin) :
    subList = delNoLen(listBin)
    for index in range(len(subList[0])) :
        if(len(subList) == 1) :
            return subList[0]
        countmore = countMoreForIndex(index,subList)
        subList = selectWithParam(countmore,index,subList)
    return subList[0]

def countLessForIndex(index, listBin) :
    zero = 0
    one = 0
    for j in listBin :
        if( j[index] == '0') :
            zero += 1
        else :
            one += 1
    if zero > one :
        return '1'
    else :
        return '0'

def findCO2(listBin) :
    subList = delNoLen(listBin)
    for index in range(len(subList[0])) :
        if(len(subList) == 1) :
            return subList[0]
        countless = countLessForIndex(index,subList)
        subList = selectWithParam(countless,index,subList)
    return subList[0]

def bintodec(num) :
    value = 0
    for i in range(len(num)-1,-1,-1) :
        if num[i] == '0' :
            continue
        else :
            if i == len(num)-1 :
                value += 1
            else :
                value += 2**(len(num)-i-1)
    return value

o2 = bintodec(findO2(binary))
co2 = bintodec(findCO2(binary))
res = o2 * co2
print(res)
