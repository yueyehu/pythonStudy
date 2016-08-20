VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
import re

def checkio(text):
    text = text.upper()
    text = text = re.findall('[0-9A-Z]{2,}',text)
    print text
    count = 0
    for w in text:
        for i,c in enumerate(w):
            if i + 1 == len(w):
                count += 1
            else:
                if (c in VOWELS and w[i+1] in CONSONANTS) or (c in CONSONANTS and w[i+1] in VOWELS):continue
                else:break
                
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
