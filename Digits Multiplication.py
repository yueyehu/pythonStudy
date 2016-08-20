#golf=lambda n:reduce(lambda x,y:x*(y if y else 1),map(int,str(n)))
def golf(n,j=1):
 for i in map(int,str(n)):
  if i:j=j*i
 return j
#
# if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert golf(123405) == 120
#    assert golf(999) == 729
#    assert golf(1000) == 1
#    assert golf(1111) == 1
#    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
