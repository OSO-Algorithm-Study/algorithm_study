# gcd(0, n) = n

from math import gcd

def solution(arrayA, arrayB):
    answer = 0
    
    arrayA.sort()
    arrayB.sort()
    
    dict_A = findGCD(arrayA)
    dict_B = findGCD(arrayB)
    
    if dict_A == 0:
        key_A = 0
    else:
        key_A = findKEY(dict_A, arrayB)    
    
    if dict_B == 0:
        key_B = 0
    else:
        key_B = findKEY(dict_B, arrayA)
        
    key = max(key_A, key_B)
    
    if (key == 0):
        answer = 0
    else:
        answer = key
    
    return answer


def findKEY(dict_X, array_X):
    for x in array_X:
        if (x % dict_X) == 0:
            key_A = 0
            return key_A
        
    if dict_X == 0:
        return
        
    return dict_X


def findGCD(arrayX):
    dict_X = {}
    arrayX_len = len(arrayX)
    
    gcd_X = 0
    
    for i in range(arrayX_len):
        gcd_X = gcd(gcd_X, arrayX[i])
    
    return gcd_X