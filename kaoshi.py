def create_dict():
    fin = open('words.txt')#open a dictionary
    word_dict = set()
    try:
        for word in fin:
            word = word.strip()
            word = word.lower()
            word_dict.add(word)
    finally:
        fin.close()
    return word_dict
word_dict = create_dict()

def create_con(string,word_dict):
    if len(string) == 0:
        return ''
    word_len = 1
    while 1:
        
        if word_len > len(string):break
        if string[0:word_len] in word_dict:
            s = string[0:word_len] +' '+ create_con(string[word_len:],word_dict)
            if len(''.join(s.split())) == len(string):
                return s
        word_len += 1
    return ''

string="abrownfoxjumpoveralazydog"
print create_con(string,word_dict)
