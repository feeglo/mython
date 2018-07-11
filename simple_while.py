name=''
while not name:
	name=raw_input('plase enter your name:')
	print 'hello', name
	panduan=raw_input('Dose it need to continued (y/n):')
	if panduan=='y':
		name=''
	else:
		print ('your are very clever\nsee you')
		break


