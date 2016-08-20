def count_words(text, words):
    count = 0
    text = text.lower()
    print text
    for c in words:
        c = c.lower()
        print c
        if text.find(c) > -1:
            count += 1
    return count
count_words(u"How aresjfhdskfhskd you?", {u"how", u"are", u"you", u"hello"})
