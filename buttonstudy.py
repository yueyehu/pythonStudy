import simplegui

stor = 12
operand = 3

def output():
	print "Store = ",store
	print "Operand = ",operand
	print ""
	
def swap():
	global store,operand
	store,operand = operand,store
	
frame = simplegui.create_frame("Caculator",200,200)

frame.add_button("Print",output,100)
frame.add_button("Swap",swap,100)

frame.start()