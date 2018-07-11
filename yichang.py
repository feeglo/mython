While True:
	try:
		x=input('Enter the first number:')
		y=input('Enter rhe second number:')
		value=x/y
		print'x/y is',value
	except:
		print 'Invalid input. please try again'
	else:
		break
