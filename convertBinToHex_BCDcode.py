def convertBinToHex(bin):
        # "1010 1011 1100 0001 0010 0011" => "ABC123"
    container = []
    refer = {
        "0000":"0","0001":"1",
        "0010":"2","0011":"3",
        "0100":"4","0101":"5",
        "0110":"6","0111":"7",
        "1000":"8","1001":"9",
        "1010":"A","1011":"B",
        "1100":"C","1101":"D",
        "1110":"E","1111":"F"
    }
    
    i = 0
    while i < len(bin):
        container.append(refer["0"*(4-len(bin[i:i+4])) + bin[i:i+4]])
        i += 4
    
    return ''.join(container)
    
print(convertBinToHex("10101")) # A1
