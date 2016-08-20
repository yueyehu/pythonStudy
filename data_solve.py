def data2bin():
    file_out = open("data_bin.txt",'w')
    file_object=open("data.txt")
    for line in file_object:
        words=line.strip().split();
        try:
            words[0],words[1] = words[1],words[0]
        except:
            break
        wordbin = ''
        for i,word in enumerate(words):
            wordbin += str2bin(word,i)
        file_out.write(wordbin+'\n')
    file_out.close()
    file_object.close()

def str2bin(word,flag):
    w = word.split('.')
    s = ''
    if flag == 0:
        s+=word2bin(w[0],7)+' '
    elif flag == 1:
        s+=word2bin(w[0][2:],4)
    elif flag == 2:
        if len(w)==1:
            s+=word2bin(w[0],7)+word2bin('0',4)
        else:
            s+=word2bin(w[0],7)+word2bin(w[1][:1],4)
    elif flag == 3:
        if len(w)==1:
            s+=word2bin(w[0],4)+word2bin('0',4)
        else:
            s+=word2bin(w[0],4)+word2bin(w[1][:1],4)
    elif flag == 4:
        if len(w)==1:
            s+=word2bin(w[0],6)+word2bin('0',7)
        else:
            s+=word2bin(w[0],6)+word2bin(w[1][:2],7)
    return s

def word2bin(word,length):
    sw=bin(int(word))
    length += 2
    s = ''
    if len(sw) < length:
        s+= '0'*(length-len(sw))+sw[2:]
    else:
        s+= sw[2:]
    return s
