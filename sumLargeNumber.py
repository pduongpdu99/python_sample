def sumLargeNum(a, b):
    # a is the string variable
    # b is the string variable
    a = str(a)
    b = str(b)
    
    while len(a) > len(b): b = "0" + b
    while len(a) < len(b): a = "0" + a
    
    l = len(a)
    result = ""
    
    a = a[::-1]
    b = b[::-1]
    
    carry= 0    
    for i in range(l): 
        s = ((ord(a[i]) - 48) + (ord(b[i]) - 48) + carry)
        result += chr(s%10 + 48)
        carry = s // 10
    
    if carry != 0:
        result += str(carry)
    return result[::-1]

print(sumLargeNum(input(), input()))

