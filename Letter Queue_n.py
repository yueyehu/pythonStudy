def letter_queue(commands):
    s = ''
    for c in commands:
        if c[1] == 'U':
            s+=c[-1]
        else:
            if len(s)>=2:
                s = s[1:]
            else:
                s = ''
    return s


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(("PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T")) == "DOT", "dot example"
    assert letter_queue(("POP", "POP")) == "", "Pop, Pop, empty"
    assert letter_queue(("PUSH H", "PUSH I")) == "HI", "Hi!"
    assert letter_queue(()) == "", "Nothing"

    print("All done? Earn rewards by using the 'Check' button!")
