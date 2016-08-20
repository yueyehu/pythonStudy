def convert(code):
    bin_code = bin(code)[2:].zfill(6)[::-1]
    return [[int(bin_code[j + i * 3]) for i in range(2)] for j in range(3)]


LETTERS_NUMBERS = list(map(convert,
                           [1, 3, 9, 25, 17, 11, 27, 19, 10, 26,
                            5, 7, 13, 29, 21, 15, 31, 23, 14, 30,
                            37, 39, 62, 45, 61, 53, 47, 63, 55, 46, 26]))
CAPITAL_FORMAT = convert(32)
NUMBER_FORMAT = convert(60)
PUNCTUATION = {",": convert(2), "-": convert(18), "?": convert(38),
               "!": convert(22), ".": convert(50), "_": convert(36)}
WHITESPACE = convert(0)
def braille_append(result,count):
    if count % 10 == 0:
        for i in range(3):
            result.append([0]*29)
        if len(result) != 3:
            result.append([0]*29)
def braille_page(text):
    result = list()
    count = 0
    for c in text:
        braille_append(result,count)
        if c.islower() == True:
            for i in range(3):
                result[count/10*4+i][(count%10*3):(count%10*3+2)] = LETTERS_NUMBERS[ord(c) - ord('a')][i]
                #print result
        elif c.isdigit() == True:
            for i in range(3):
                result[count/10*4+i][(count%10*3):(count%10*3+2)] = NUMBER_FORMAT[i]
            count += 1
            braille_append(result,count)
            for i in range(3):
                result[count/10*4+i][(count%10*3):(count%10*3+2)] = LETTERS_NUMBERS[(ord(c) - ord('1')+10)%10][i]
        elif c.isspace() == True:
            for i in range(3):
                result[count/10*4+i][(count%10*3):(count%10*3+2)] = WHITESPACE[i]
        elif c.isupper() == True:
            for i in range(3):
                result[count/10*4+i][(count%10*3):(count%10*3+2)] = CAPITAL_FORMAT[i]
            count += 1
            braille_append(result,count)
            for i in range(3):
                result[count/10*4+i][(count%10*3):(count%10*3+2)] = LETTERS_NUMBERS[ord(c) - ord('A')][i]
        elif c in PUNCTUATION:
            for i in range(3):
                result[count/10*4+i][(count%10*3):(count%10*3+2)] = PUNCTUATION[c][i]
        count += 1
    if count < 10:
        result = [result[i][0:count*3-1] for i in range(3)]
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(func, text, answer):
        result = func(text)
        return answer == tuple(tuple(row) for row in result)

    assert checker(braille_page, u"hello 1st World!", (
        (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1),
        (1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1),
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0))
    ), "Example"
    assert checker(braille_page, u"42", (
        (0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0),
        (0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0),
        (1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0))), "42"
    assert checker(braille_page, u"CODE", (
        (0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1),
        (0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0))
    ), "CODE"

