import re
def flat_list(array):
    return [int(i) for i in re.findall('-*\d',str(array))]
