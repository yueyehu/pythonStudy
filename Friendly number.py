def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    base_count = 0
    while abs(number) > base:
        if len(powers) == base_count+1:
            break
        number = number*1.0/base
        base_count += 1
    #print number
    if decimals == 0:
        number = int(number)
    else:
        number = round(number,decimals)
        l = len(str(number).split('.')[1])
        number = number if l==decimals else str(number) + '0'*(decimals-l)
    #print number
    return str(number)+powers[base_count]+suffix

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'

