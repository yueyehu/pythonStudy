import re
def find_word(message):
    mes = re.findall('\w+',message)
    mes = mes[::-1]
    #print mes
    mes_score = [[0]*len(mes) for i in range(len(mes))]
    for i,c1 in enumerate(mes):
        for j,c2 in enumerate(mes):
            if i == j:continue
            c1 = c1.lower()
            c2 = c2.lower()
            if c1 == c2:
                mes_score[i][j] = 100
                continue
            if c1[0] == c2[0]:mes_score[i][j] += 10
            if c1[-1] == c2[-1]:mes_score[i][j] += 10
            mes_score[i][j] += (min(len(c1),len(c2))*1.0/max(len(c1),len(c2)))*30
            mes_score[i][j] += (len(set(c1)&set(c2))*1.0/len(set(c1)|set(c2)))*50
    mes_score = [sum(r) for r in mes_score]
    return mes[mes_score.index(max(mes_score))].lower()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word(u"Speak friend and enter.") == "friend", "Friend"
    assert find_word(u"Beard and Bread") == "bread", "Bread is Beard"
    assert find_word(u"The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     u"I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     u" According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(u"One, two, two, three, three, three.") == "three", "Repeating"
