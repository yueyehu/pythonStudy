class checkio:

    def __init__(self, anything):
        pass

    def __lt__(self, otherthing):
        return True

    def __gt__(self, otherthing):
        return True

    def __ge__(self, otherthing):
        return True

    def __le__(self, otherthing):
        return True

    def __eq__(self, otherthing):
        return True

    def __ne__(self, otherthing):
        return True

    
if __name__ == '__main__':
    import re, math
    assert checkio({}) != [] ,         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'
    print('NO WAY :(')
