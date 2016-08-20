def find_max(data,s):
    if len(data) > 0:
        if min(data) > s:
            return 0
        else:
            if data[0] > s:
                return find_max(data[1:],s)
            else:
                return max(find_max(data[1:],s),find_max(data[1:],s-data[0]) + data[0])
    return 0
def checkio(data):
    data_sum  = sum(data)*1.0/2
    return int(2*(data_sum-find_max(data,data_sum)))
  


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
