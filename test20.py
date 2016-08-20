def check_connection(network, first, second):
    rel = []
    for c in network:
        drone = c.split('-')
        con = None
        for i,d in enumerate(rel):
            if drone[0] in d or drone[1] in d:
                if con == None:
                    if drone[0] in d:rel[i].add(drone[1])
                    else:rel[i].add(drone[0])
                    con = i
                else:
                    rel[con].update(rel[i])
                    rel.pop(i)
                    break
        if con == None:rel.append(set(drone))
        for d in rel:
            if first in d and second in d:return True
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."

