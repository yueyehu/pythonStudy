def checkio(words_set):
    words = words_set.copy()
    for w in words_set:
        words.remove(w) 
        for wd in words:
            print w,wd
            if len(w) > len(wd):
                if wd == w[-len(wd):] :return True
            else:
                if w == wd[-len(w):] :return True
    return False
#These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    assert checkio({u"hello", u"lo", u"he"}) == True, "helLO"
    assert checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
    assert checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
    assert checkio({u"one"}) == False, "Only One"
    assert checkio({u"helicopter", u"li", u"he"}) == False, "Only end"


