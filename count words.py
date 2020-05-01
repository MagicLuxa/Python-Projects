def countWords(text):
    word = ""
    words = 0
    table = {}

    for i in range(len(text)):
        letter = text[i]
        if ord(letter) > 64 and ord(letter) < 91:
            letter = ord(letter)
            letter += 32
            letter = chr(letter)
        
        if ord(letter) > 96 and ord(letter) < 123:
            word += letter

        else:
            if word != "":
                if word in table.keys():
                    table[word] += 1
                    words += 1
                else:
                    table[word] = 1
                    words += 1
            word = ""

    return table, words


file = open("text2.txt")

text = file.read().replace("\n", " ")
file.close()

table, words = countWords(text)


while True:
    word = input("Which word?      ")
    if type(word) != str:
        break
    else:
        if word in table.keys():
            percentage = ((table[word] / words) * 100)
            print("{}%".format(percentage))
        else:
            print("This word doesn't appear in the text")
