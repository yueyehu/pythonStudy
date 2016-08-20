d2 = {'0':'..','1':'.-','2':'-.'}
d3 = {'0':'...','1':'..-','2':'.-.','3':'.--','4':'-..','5':'-.-'}
d4 = {'0':'....','1':'...-','2':'..-.','3':'..--','4':'.-..','5':'.-.-','6':'.--.','7':'.---','8':'-...','9':'-..-'}
def morse_time(time_string):
    time = time_string.split(':')
    morse_string = ''
    if len(time[0]) == 1:
        morse_string += d2['0'] + ' ' + d4[time[0]]
    else:
        morse_string += d2[time[0][0]] + ' ' + d4[time[0][1]]
    morse_string += ' : '
    if len(time[1]) == 1:
        morse_string += d3['0'] + ' ' + d4[time[1]]
    else:
        morse_string += d3[time[1][0]] + ' ' + d4[time[1][1]]
    morse_string += ' : '
    if len(time[2]) == 1:
        morse_string += d3['0'] + ' ' + d4[time[2]]
    else:
        morse_string += d3[time[2][0]] + ' ' + d4[time[2][1]]
    return morse_string


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_time("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert morse_time("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert morse_time("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert morse_time("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
