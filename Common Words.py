def common_words(first, second):
    first = set(first.split(','))
    second = set(second.split(','))
    s = first & second
    s = list(s)
    s.sort()
    return ','.join(s)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert common_words("hello,world", "hello,earth") == "hello", "Hello"
    assert common_words("one,two,three", "four,five,six") == "", "Too different"
    assert common_words("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
