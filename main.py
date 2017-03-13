import os
pyt = "python3" #Here is the command that you use to run python. Possible values - python,python3,python27 etc
while(1==1):
	print('\nMain Menu:\n')
	print('1. You vs your friends')
	print('2. View a problem')
	print('3. Submit a solution')
	print('4. Exit\n')
	c = int(input('Enter your choice: '))
	if(c==1):
		try:
			os.system(pyt+" spoj-friends.py")
		except:
			print('Error: File missing or permission denied')
	elif(c==2):
		problem = input('\nEnter the problem code: ')
		try:
			os.system(pyt+" spoj-viewer.py "+problem)
		except:
			print('Error: File missing or permission denied')
	elif(c==3):
		problem = input('\nEnter the problem code: ')
		file = input('\nEnter the filename to submit: ')
		try:
			os.system(pyt+" spoj-submitter.py "+problem+" "+file)
		except:
			print('Error: File missing or permission denied')
	elif(c==4):
		break
	else:
		print('Try again..')
