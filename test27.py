class Friends:
    def __init__(self, connections):
        self.con = list(connections)
        
    def add(self, connection):
        for c in self.con:
            if c == connection: return False
        self.con.append(connection)
        return True

    def remove(self, connection):
        for i,d in enumerate(self.con):
            if connection == d:
                self.con.pop(i)
                return True
        return False
    def names(self):
        con = set()
        for d in self.con:
            con.update(d)
        return con

    def connected(self, name):
        con = set()
        for d in self.con:
            if name in d: con.update(d)
        if name in con:
            con.remove(name)
            return con 
        return set()



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
