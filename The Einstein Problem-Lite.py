COLORS = ['blue', 'green', 'red', 'white', 'yellow']
PETS = ['cat', 'bird', 'dog', 'fish', 'horse']
BEVERAGES = ['beer', 'coffee', 'milk', 'tea', 'water']
CIGARETTES = ['Rothmans', 'Dunhill', 'Pall Mall', 'Winfield', 'Marlboro']
NATIONALITY = ['Brit', 'Dane', 'German', 'Norwegian', 'Swede']
NUMBERS = ['1', '2', '3', '4', '5']
QUESTIONS = {"number":NUMBERS, "color":COLORS, "nationality":NATIONALITY, "beverage":BEVERAGES, "cigarettes":CIGARETTES, "pet":PETS}


def answer(relations, question):
    number_c = NUMBERS[:]
    color_c = COLORS[:]
    nationality_c = NATIONALITY[:]
    beverage_c = BEVERAGES[:]
    cigarettes_c = CIGARETTES[:]
    pet_c = PETS[:]
        
    question = question.split('-')
    re_ship = dict()
    re_ship_list = list()
    if question[0] in COLORS:
        for c in COLORS:
            re_ship[c] = {c}
    elif question[0] in PETS:
        for c in PETS:
            re_ship[c] = {c}
    elif question[0] in BEVERAGES:
        for c in BEVERAGES:
            re_ship[c] = {c}
    elif question[0] in CIGARETTES:
        for c in CIGARETTES:
            re_ship[c] = {c}
    elif question[0] in NATIONALITY:
        for c in NATIONALITY:
            re_ship[c] = {c}
    elif question[0] in NUMBERS:
        for c in NUMBERS:
            re_ship[c] = {c}
    for r in relations:
        rr = r.split('-')
        #print 'rr',rr
        flag1 = False
        flag2 = False
        global i1
        for i,d in enumerate(re_ship_list):
            if rr[0] in d:
                for i1,d1 in enumerate(re_ship_list):
                    if rr[1] in d1 and i != i1:
                        flag1 = True
                        re_ship_list[i].update(re_ship_list[i1])
                        #popi = il
                        break
                flag2 = True
                re_ship_list[i].add(rr[1])
                break
            elif rr[1] in d:
                for i1,d1 in enumerate(re_ship_list):
                    if rr[0] in d1 and i != i1:
                        re_ship_list[i].update(re_ship_list[i1])
                        flag1 = True
                        #popi = i1
                        break
                flag2 = True
                re_ship_list[i].add(rr[0])
                break
        if flag1 != False:re_ship_list.pop(i1)
        if flag2 == False:re_ship_list.append(set(rr))   
    re_ship_list_copy = re_ship_list[:] 
    for s in re_ship_list_copy:
        for w in s:
            if w in NUMBERS:
                number_c.remove(w)
            if w in COLORS:
                color_c.remove(w)
            if w in NATIONALITY:
                nationality_c.remove(w)
            if w in BEVERAGES:
                beverage_c.remove(w)
            if w in CIGARETTES:
                cigarettes_c.remove(w)
            if w in PETS:
                pet_c.remove(w)
        for w in s:
            if w in re_ship:
                re_ship[w].update(s)
                re_ship_list.remove(s)
                break
    if len(number_c) == 1:re_ship_list.append(set(number_c))
    if len(color_c) == 1:re_ship_list.append(set(color_c))
    if len(nationality_c) == 1:re_ship_list.append(set(nationality_c))
    if len(beverage_c) == 1:re_ship_list.append(set(beverage_c))
    if len(pet_c) == 1:re_ship_list.append(set(pet_c))
    if len(cigarettes_c) == 1:re_ship_list.append(set(cigarettes_c))
    while True:
        #print 'QUESTIONS[question[1]]',QUESTIONS[question[1]]
        #print 're_ship',re_ship
        #print 're_ship_list',re_ship_list   
        for c in QUESTIONS[question[1]]:
            if c in re_ship[question[0]]:
                return c
        re_ship_list_c = re_ship_list[:]
        for r in re_ship_list_c:
            global flag_count
            flag_count = 0
            global flag_key
            for k in re_ship:
                flag_f = False
                if len(re_ship[k]) == 6:continue
                for rc in r:
                    for kc in re_ship[k]:
                        if rc in NUMBERS and kc in NUMBERS:
                            flag_f = True
                            break
                        if rc in COLORS and kc in COLORS:
                            flag_f = True
                            break
                        if rc in NATIONALITY and kc in NATIONALITY:
                            flag_f = True
                            break
                        if rc in BEVERAGES and kc in BEVERAGES:
                            flag_f = True
                            break
                        if rc in CIGARETTES and kc in CIGARETTES:
                            flag_f = True
                            break
                        if rc in PETS and kc in PETS:
                            flag_f = True
                            break
                    if flag_f == True:
                        break
                if flag_f != True:
                    flag_count += 1
                    flag_key = k
            if flag_count == 1:
                re_ship[flag_key].update(r)
                re_ship_list.remove(r)
    #print 're_ship',re_ship
    #print 're_ship_list',re_ship_list       
            
    #return "Answer"


if __name__ == '__main__':
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'fish-color') == 'green'  # What is the color of the house where the Fish lives?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'tea-number') == '2'  # What is the number of the house where tea is favorite beverage?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'Norwegian-beverage') == 'water'  # What is the favorite beverage of the Norwegian man?

