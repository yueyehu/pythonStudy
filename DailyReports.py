'''
Created on 2015/11/22/

@author: HKJ
'''
def count_reports(full_report, from_date, to_date):
    full_report = full_report.split('\n')
    countdate = 0
    for f in full_report:
        f = f.split()
        if check_between(f[0],from_date,to_date):
            fc = f[1].split(',')
            for c in fc:
                countdate += (ord(c[0]) - ord('A'))*9 + ord(c[1]) -ord('0')
    return countdate    

def check_between(date_bet,from_date,to_date):
    if compare_date(from_date,date_bet) and compare_date(date_bet,to_date):
        return True
    else:
        return False
    
def compare_date(min_date,max_date): 
    min_date = min_date.split('-')
    max_date = max_date.split('-')
    if int(min_date[0]) > int(max_date[0]):
        return False
    elif int(min_date[0]) < int(max_date[0]):
        return True
    elif int(min_date[1]) > int(max_date[1]):
        return False
    elif int(min_date[1]) < int(max_date[1]):
        return True
    elif int(min_date[2]) > int(max_date[2]):
        return False
    else:
        return True
        
    
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_reports("2015-01-01 A1,B2\n"
                         "2015-01-05 C3,C2,C1\n"
                         "2015-02-01 B4\n"
                         "2015-01-03 Z9,Z9",
                         "2015-01-01", "2015-01-31") == 540, "Normal"
    assert count_reports("2000-02-02 Z2,Z1\n"
                         "2000-02-01 Z2,Z1\n"
                         "2000-02-03 Z2,Z1",
                         "2000-02-04", "2000-02-28") == 0, "Zero"
    assert count_reports("2999-12-31 Z9,A1", "2000-01-01", "2999-12-31") == 235, "Millenium"

    print("Earn cool rewards by using the 'Check' button!")