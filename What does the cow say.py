COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

def cowsay(text):
    textt = text[:]
    text = text.split()
    if textt[0] == ' ':text[0] = ' ' + text[0]
    if textt[-1] == ' ':text[-1] =  text[-1] + ' '
    count = 0
    tex = []
    while count < len(text):
        if len(text[count]) > 39:
            if text[count][0] == ' ':
                tex.append(' ')
                i = 1
            else:
                i = 0
            while 1:
                if len(text[count][i:]) > 39:
                    tex.append(text[count][i:i+39])
                    i+=39
                else:
                    tex.append(text[count][i:])
                    break
        else:
            tex.append(text[count])
        count += 1
    text = tex[:]
    #if textt[0] == ' ':text[0] = ' ' + text[0]
    #if textt[-1] == ' ':text[-1] =  text[-1] + ' '
    line = ['']
    line_count = 0
    for i,w in enumerate(text):
        if len(line[line_count]) != 0:
            line[line_count] += ' '
        line[line_count] += w
        if i+1 < len(text) and len(line[line_count])+len(text[i+1]) >= 39:
            line.append('')
            line_count += 1
    if len(line) == 1:
        ps = ' '+'_'*(len(line[0])+2)+'\n'+'<'+' '+line[0]+' '+'>'+'\n'+ ' '+'-'*(len(line[0])+2)
    else:
        L = max([len(i) for i in line])
        p_s = ' '+'_'*(L+2)+'\n'
        p_e = ' '+'-'*(L+2)
        p_s1= r'/'+' '+'%s'%line[0]+' '*(L-len(line[0])+1)+'\\'+'\n'
        p_e1= '\\'+' '+'%s'%line[-1]+' '*(L-len(line[-1])+1)+r'/'+'\n'
        p_s += p_s1
        for i in range(1,len(line)-1):
            p_s = p_s +'|'+' '+'%s'%line[i]+' '*(L-len(line[i])+1)+r'|'+'\n'
        ps = p_s+p_e1+p_e
    return '\n'+ps+COW
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                                'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
