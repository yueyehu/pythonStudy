import re
def create_key_table(key):
    kt = list("abcdefghijklmnopqrstuvwxyz0123456789")
    key_t = list()

    for i,c in enumerate(key):
        try:
            kt.remove(c)
            key_t.append(c)
        except:
            pass
        
    kt = ''.join(key_t + kt)
    #print kt
    return{kt[j*6+i]:(j,i) for i in range(6) for j in range(6)},[[kt[j*6+i] for i in range(6)] for j in range(6)]

def encode(message, key):
    message = ''.join(re.findall('[0-9a-z]+',message.lower()))
    #
    m_c = message
    while True:
        for i in range(len(message)-1):
            if m_c[i] == m_c[i+1] and i%2 == 0:
                if m_c[i] != 'x':
                    m_c = m_c[0:i+1] + 'x' + m_c[i+1:]
                else:
                    m_c = m_c[0:i+1] + 'z' + m_c[i+1:]
                break
        if message != m_c:
            message = m_c
        else:
            break
        #print message
    #print message
    if len(message)%2 != 0:
        if message[-1] == 'z':
            message += 'x'
        else:
            message += 'z'
    message = [message[i:i+2] for i in range(len(message))if i%2 == 0]
    #print message
    m_encode = list()
    key_table,kt_list = create_key_table(key)
    i = 0
    while len(message) != i:
        #print message[i]
        a0 = key_table[message[i][0]][0]
        a1 = key_table[message[i][0]][1]
        b0 = key_table[message[i][1]][0]
        b1 = key_table[message[i][1]][1]
        #print a0,a1,b0,b1
        if a0 == b0:
            m_encode.append(kt_list[a0][(a1+1)%6] + kt_list[b0][(b1+1)%6])
        elif a1 == b1:
            m_encode.append(kt_list[(a0+1)%6][a1] + kt_list[(b0+1)%6][b1])
        else:
            m_encode.append(kt_list[a0][b1] + kt_list[b0][a1])
        i += 1
    return ''.join(m_encode)


def decode(secret_message, key):
    secret_message = [secret_message[i:i+2] for i in range(len(secret_message))if i%2 == 0]
    key_table,kt_list = create_key_table(key)
    m_decode = list()
    i = 0
    while len(secret_message) != i:
        #print message[i]
        a0 = key_table[secret_message[i][0]][0]
        a1 = key_table[secret_message[i][0]][1]
        b0 = key_table[secret_message[i][1]][0]
        b1 = key_table[secret_message[i][1]][1]
        #print a0,a1,b0,b1
        if a0 == b0:
            m_decode.append(kt_list[a0][(a1-1)%6] + kt_list[b0][(b1-1)%6])
        elif a1 == b1:
            m_decode.append(kt_list[(a0-1)%6][a1] + kt_list[(b0-1)%6][b1])
        else:
            m_decode.append(kt_list[a0][b1] + kt_list[b0][a1])
        i += 1
    '''   
    m_c = secret_message = ''.join(m_decode)

    while True:
        for i in range(len(secret_message)-2):
            if m_c[i] == m_c[i+2] and i%2 == 0:
                if m_c[i] != 'x' and m_c[i+1] == 'x':
                    m_c = m_c[0:i+1] + m_c[i+2:]
                elif m_c[i] == 'x' and m_c[i+1] == 'z':
                    m_c = m_c[0:i+1] + m_c[i+2:]
                break
        if secret_message != m_c:
            secret_message = m_c
        else:
            break
        #print messag
    '''
    return ''.join(m_decode)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert encode("Fizz Buzz is x89 XX.", "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
    assert decode("do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
    assert encode("How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
    assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
    assert encode("My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
    assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
    assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
    assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
    assert encode("ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
    assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"

