import re
def count_words(text, words):
    text = text.lower()
    text = re.findall("[a-z]+",text)
    print text
    count = 0
    for w in text:
        for c in words:
            if c in w:
                count += 1
                break
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"

    print("All set? Click 'Check' to review your code and earn rewards!")
