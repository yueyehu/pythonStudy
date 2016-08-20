def super_root(number):
    if number == 1:return 1
    n_s = 0
    n_b = 20
    n_m = 10
    s = n_m**n_m - number
    while abs(s)>0.001:
        if s > 0:
            n_b = n_m
            n_m = (n_s+n_m)/2.0
        else:
            n_s = n_m
            n_m = (n_m+n_b)/2.0
        s = n_m**n_m - number
    return n_m

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False

    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
