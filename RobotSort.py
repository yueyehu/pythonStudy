'''
Created on 2015/11/23

@author: HKJ
'''
def swap_sort(array):
    swap = list()
    array_list = [i for i in array]
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array_list[j] > array_list[j+1]:
                array_list[j],array_list[j+1] = array_list[j+1],array_list[j]
                swap.append(str(j)+str(j+1))
    return ','.join(swap)
        


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check_solution(f, indata):
        result = f(indata)
        array = list(indata[:])
        la = len(array)
        if not isinstance(result, str):
            print("The result should be a string")
            return False
        actions = result.split(",") if result else []
        for act in actions:
            if len(act) != 2 or not act.isdigit():
                print("The wrong action: {}".format(act))
                return False
            i, j = int(act[0]), int(act[1])
            if i >= la or j >= la:
                print("Index error: {}".format(act))
                return False
            if abs(i - j) != 1:
                print("The wrong action: {}".format(act))
                return False
            array[i], array[j] = array[j], array[i]
        if len(actions) > (la * (la - 1)) // 2:
            print("Too many actions. BOOM!")
            return False
        if array != sorted(indata):
            print("The array is not sorted. BOOM!")
            return False
        return True

    assert check_solution(swap_sort, (6, 4, 2)), "Reverse simple"
    assert check_solution(swap_sort, (1, 2, 3, 4, 5)), "All right!"
    assert check_solution(swap_sort, (1, 2, 3, 5, 3)), "One move"

    print("Earn cool rewards by using the 'Check' button!")