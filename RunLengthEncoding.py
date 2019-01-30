def Encode(inputString):
    occurances = 1
    prevString = ''
    codeList = []
    encodedString = ''

    for character in inputString:
        if character == prevString:
            occurances += 1
        else:
            if prevString:
                entry = (prevString,occurances)
                codeList.append(entry)
                occurances = 1
            prevString = character

    entry = (character,occurances)
    codeList.append(entry)

    for code in codeList:
        if code[1] < 2:
            encodedString += code[0]
        else:
            encodedString += str(code[1]) + code[0]

    return encodedString



def main():  # define main function
    print(Encode("CCCGGRRRRRRY"))



if __name__ == '__main__':
    main()  # call main() function


