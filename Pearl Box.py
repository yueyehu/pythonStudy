
def probability(marbles, step):
    bc = marbles.count('b')*1.0/len(marbles)
    wc = marbles.count('w')*1.0/len(marbles)
    for i in range(step-1):
        bc_t = bc*(bc - 1.0/len(marbles)) + wc*(bc + 1.0/len(marbles))
        wc_t = wc*(wc - 1.0/len(marbles)) + bc*(wc + 1.0/len(marbles))
        bc,wc = bc_t,wc_t
    return wc


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(probability('bbw', 3), 0.48), "1st example"
    assert almost_equal(probability('wwb', 3), 0.52), "2nd example"
    assert almost_equal(probability('www', 3), 0.56), "3rd example"
    assert almost_equal(probability('bbbb', 1), 0), "4th example"
    assert almost_equal(probability('wwbb', 4), 0.5), "5th example"
    assert almost_equal(probability('bwbwbwb', 5), 0.48), "6th example"

    print("All done? Earn rewards by using the 'Check' button!")
