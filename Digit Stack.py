def golf(c):
 s,l=0,[]
 for i in c:
  if i[1]=='U':l.append(int(i[-1]))
  elif i[1]=='O':
   if len(l):s+=l.pop()
  else:
   if len(l):s+=l[-1]
 return s
# if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert golf(("PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK")) == 8, "Example"
#    assert golf(("POP", "POP")) == 0, "PopPop"
#    assert golf(("PUSH 9", "PUSH 9", "POP")) == 9, "Push 9"
#    assert golf(()) == 0, "Empty"
#    print("All done? Earn rewards by using the 'Check' button!")
