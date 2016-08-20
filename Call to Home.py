def total_cost(calls):
    count = 0
    call_map = {}
    for c in calls:
        i = -1
        while 1:
            if c[i] == ' ':break
            i -= 1
        if c[0:10] in call_map:
            call_map[c[0:10]] += int(c[i+1:])/60+ (1 if int(c[i+1:])%60 !=0 else 0)
        else:
            call_map[c[0:10]] = int(c[i+1:])/60+ (1 if int(c[i+1:])%60 !=0 else 0)
    for d in call_map:
        if call_map[d] <=100:
            count += call_map[d]
        else:
            count += 100+2*(call_map[d]-100)
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost((u"2014-01-01 01:12:13 181",
                       u"2014-01-02 20:11:10 600",
                       u"2014-01-03 01:12:13 6009",
                       u"2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost((u"2014-02-05 01:00:00 1",
                       u"2014-02-05 02:00:00 1",
                       u"2014-02-05 03:00:00 1",
                       u"2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost((u"2014-02-05 01:00:00 60",
                       u"2014-02-05 02:00:00 60",
                       u"2014-02-05 03:00:00 60",
                       u"2014-02-05 04:00:00 6000")) == 106, "Precise calls"
