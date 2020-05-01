def caesar_crypto_encode(text, shift):
    
    if text == None:
        return ""
        
    if text == None:
        return ""
        
    num = 0
    for i in range(len(text)):
        if text[i] == " ":
            num += 1
    if num == len(text):
        return ""
            
    output = []
    for i in range(len(text)):
        temp = ord(text[i])
        if temp > 64 and temp < 97:
            temp -= 64
            temp += shift - 1
            temp %= 26
            temp += 65
            temp = chr(temp)
            output.append(temp)
        elif temp > 96 and temp < 123:
            temp -= 96
            temp += shift - 1
            temp %= 26
            temp += 97
            temp = chr(temp)
            output.append(temp)
        else:
            temp = chr(temp)
            output.append(temp)
    output = listToString(output)
    print(output)
    return output

def listToString(s):   
    str1 = ""    
    for ele in s:  
        str1 += ele   
    return str1


for i in range(0, 27):
    caesar_crypto_encode("abcdefghijklmnopqrstuvwxyz", i)