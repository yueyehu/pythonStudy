'''
Created on 2015/12/3

@author: HKJ
'''
def find_repeats(decimal_string):
    print (len(decimal_string)) / 3
    for i in range(0, (len(decimal_string)) / 3):
        first, second, third = (decimal_string[-i * 3 - 3: -i * 2 - 2],
                                decimal_string[-i * 2 - 2: -1 - i],
                                decimal_string[-1 - i:])
        # logging.debug('1st: %s, 2nd: %s, 3rd: %s' % (first, second, third))
        if first and first == second == third:
            return len(decimal_string) - 1 - i * 3 - 2, len(decimal_string) - 1 - i * 2 - 1
    return None, None


def get_next_decimal(numerator, denominator):
    while 1:
        decimals = str(numerator * 10 / denominator)
        numerator = numerator * 10 % denominator
        yield decimals


def convert(numerator, denominator):
    # logger.debug('numerator:%d, denominator:%d' % (numerator % denominator, denominator))
    decimal_generator = get_next_decimal(numerator % denominator, denominator)
    decimal_string = ''
    for i in range(10000):
        decimal_string += decimal_generator.next()
        # logger.debug(decimal_string)
        if decimal_string[-3:] == '000':
            return '%d.%s' % (numerator / denominator, decimal_string[:-3])
        if len(decimal_string) < 3:
            continue
        print decimal_string
        start_pos, end_pos = find_repeats(decimal_string)
        if start_pos is not None:
            # logger.debug('start pos:%d, end_pos:%d' % (start_pos, end_pos))
            # logger.debug('%d.%s(%s)' % (numerator / denominator,
            #                             decimal_string[:start_pos],
            #                             decimal_string[start_pos:end_pos]))
            return '%d.%s(%s)' % (numerator / denominator,
                                  decimal_string[:start_pos],
                                  decimal_string[start_pos:end_pos])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"