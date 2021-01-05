
"""CREATED ON *DATE=5 JAN,2021 *TIME=23:00-23.38 """
####################################################
#                                                  #
#    DEVELOPER'S NAME  :- ARIJ ARMAN MANDAL        #
#      PROJECT   :-  MATH-HELPER-PYTHON            #
#                                                  #  
#                                                  #
#       KEEP SUPORTING ME..... THANK YOU           #
#                                                  #
#                                                  #
####################################################
# A Simple python code using only IF-ELIF-ELSE conditios .
import time
i = 1
time.sleep(2.2)
print('<<<<<====================================>>>>>')
print("----------[Welcome to my Math Class]----------")
print('<<<<<====================================>>>>>')
print('')
time.sleep(1.3)
arij_constant = 1
while True:
	time.sleep(0.5)
	print('  (((======================================================)))')
	print('                What solution do you want ?')
	print('(((============================================================)))')
	time.sleep(1.2)
	print('  [1] Add or Plus(a+b)                  [6] Simple Interset')
	time.sleep(0.4)
	print('  [2] Substract or Minus(a-b)           [7] Compound Interset')
	time.sleep(0.4)
	print('  [3] Multiply or into(a x b)           [8] Square, Cubes and others')
	time.sleep(0.4)
	print('  [4] Division or x/y                   [9] Nothing')
	time.sleep(0.4)
	print('  [5] Roots                             [10] Math on Workers and Time')
	time.sleep(0.4)
	print('')
	print('           [99] Exit(press 99 and enter)')
	
	print('')
	user = int(input('(@)_Choose a number[1-10/99]: '))
	print("")
	# Plus,minus,multiply and division zone
	if user == 1 :
		time.sleep(0.5)
		num1 = float(input('[*] Enter the 1st number: '))
		print('')
		num2 = float(input('[*] Enter the 2nd number: '))
		time.sleep(0.5)
		print('>>>>Answer is= ',num1+num2)
		time.sleep(0.3)
		print("")
		time.sleep(0.5)
		i += 1
	elif user == 2 :
		time.sleep(0.5)
		num1 = float(input('[*] Enter the 1st number: '))
		print('')
		num2 = float(input('[*] Enter the 2nd number: '))
		time.sleep(0.5)	
		print('')
		print('>>>>Answer is= ',num1-num2)
		print('')
	elif user == 3 :
		time.sleep(0.5)
		num1 = float(input('[*] Enter the 1st number: '))
		print('')
		num2 = float(input('[*] Enter the 2nd number: '))	
		time.sleep(0.5)
		print('>>>>Answer is= ',num1*num2)
	elif user == 4 :
		num1 = float(input('[*] Enter the 1st number: '))
		num2 = float(input('[*] Enter the 2nd number: '))	
		print('>>>>Answer is= ',num1/num2)
	# For root in mathematical	
	elif user == 5 :
		aaa = 1
		while True:
			print('[1] Square roots')
			print('[2] Cube roots')
			print('[3] Choose custom                 [99] Exit Main menu')
			choice = int(input('Enter choice: '))
			if choice == 1:
				print()
				a = float(input('Enter the number: '))
				time.sleep(0.3)
				b= a**0.5
				
				print('The square root of',a, "is", b)
				
			elif choice == 2 :
				a = float(input('Enter the number: '))
				time.sleep(0.3)
				b= a**0.33333333333333333333333333333333333
				c = round(b)
				print('The cube root of',a, "is", c)
			elif choice == 3:
				root = int(input('Enter the Root power or Exponent: '))
				chroot = 1/root
				a = float(input('Enter the number: '))
				b = a**chroot
				c = round(b)
				x = int(a)
				print('The', root,"th power of", x, 'is =', b)
			elif choice == 99 :
				print()
				break
			else: 
				print('Error! Invalid Input.')
			aaa += 1
	elif user == 6 :
		aaa = 1
		time.sleep(0.5)
		while True :
			print('************(Simple Interset)************')
			print('')
			print('Which answe do you want? ')
			print('')
			print('[1] Principle                          [99] Exit Main-menu')
			print('[2] Time')
			print('[3] % of Interest')
			print('[4] Interest')
			print('')
			time.sleep(0.4)
			inp = int(input('Enter your chice: '))
			if inp == 1 :
				t = float(input('Enter the time span: '))
				r = float(input('Enter the % of Interest: '))
				i = float(input('Enter the amount of Interset: '))
				p = (i*100)/(t*r)
				time.sleep(0.6)
				print ('The principle amout is =', p)
				time.sleep(0.4)
			elif inp == 2 :
				p = float(input('Enter the Principle amount: '))
				r = float(input('Enter the % of interst : '))
				i = float(input('Enter the Interest amount: '))
				time.sleep(0.6)
				t = (i*100)/(p*r)
				print('The time span is=', t)
				time.sleep(0.6)
			elif inp == 3 :
				p = float(input('Enter the Principle amount: '))
				t = float(input('Enter the Time span: '))
				i = float(input('Enter the Principle amount: '))
				time.sleep(0.5)
				r = (i*100)/(p*t)
				print('The percentage % of Interest is =', r)
				time.sleep(0.5)
			elif inp == 4 :
				p = float(input('Enter the Principle amount: '))
				r = float(input('Enter the % of interst : '))
				t = float(input('Enter the time span: '))
				time.sleep(0.4)
				i = (p*t*r)/100
				print('The amount of Interest is =', i)
			elif inp == 99 :
				print('Exiting to Main-menu...')
				time.sleep(0.5)
				break
			else :
				print('Error! Invalid Input.')
			aaa += 1
	elif user == 7 :
		aaa = 1
		print('')
		while True:
			print('*****************(COMPOUND INTEREST)*****************')
			time.sleep(0.4)
			print("")
			print('[1] Start Compound Interest      [2] Exit Main-menu')
			time.sleep(0.4)
			print('')
			uss = int(input('Enter your choice: '))
			print('')
			if uss == 1 :
				time.sleep(0.5)
				p = float(input('Enter the Principle amount: '))
				print('')
				t = int(input('Enter the Time span: '))
				print('')
				r = float(input('Enter the % of interst : '))
				print('')
				ci = p*(1 + r/100)**t
				time.sleep(0.5)
				print('Compound Interest is =', ci)
				print('')
			elif uss == 2 :
				print('')
				print('Exiting...')
				time.sleep(0.4)
				break
			else: 
				print('')
				print('Error! Invalid Input...')
			aaa += 1
		
	elif user == 10 :
		arij_constant = 1
		while True:
			
			print('(((===========================)))')
			print('   What solution do you want ?')
			print('(((===========================)))')
			time.sleep(1.2)
			print('[1] Workers                    [99] Exit')
			time.sleep(0.8)
			print('[2] Time ')
			time.sleep(0.8)
			print('[3] Worked_Place')
			time.sleep(0.8)
			print('')
			time.sleep(1.0)
			choice_first = int(input("👨‍💻️==> Enter the Choice[1 to 4 or 99]: "))
			print('')
			time.sleep(1.3)
			if choice_first == 1:
				print('==> Enter the given examples of Workers,Time & Worked_Place:')
				a = int(input('==> Enter Workers: '))
				print('')
				b = int(input('==> Enter Time: '))
				print('')
				c = int(input('==> Enter Worked_Place: '))
				print('')
				k = (b*a)/c
				time.sleep(0.8)
				print('==> Enter the value of 2nd_Time & 2nd_Worked_Place:')
				print('')
				b2 = int(input('==> Enter 2nd_Time: '))
				print('')
				c2 = int(input('==> Enter 2nd_Worked_Place: '))
				print('')
				print('The amount of Workers is:')
				time.sleep(0.8)
				a2 = (k*c2)/b2
				print(a2)
				print('')
			elif choice_first == 2 :
				print('==> Enter the given examples of Workers,Time & Worked_Place:')
				print('')
				a = int(input('==> Enter Workers: '))
				print('')
				b = int(input('==> Enter Time: '))
				print('')
				c = int(input('==> Enter Worked_Place: '))
				print('')
				k = (b*a)/c
				time.sleep(0.8)
				print('==> Enter the value of 2nd_Workers & 2nd_Worked_Place:')
				print('')
				a2 = int(input('==> Enter 2nd_Workers: '))
				print('')
				c2 = int(input('==> Enter 2nd_Worked_Place: '))
				print('')
				b2 = (k*c2)/a2
				print('The amount of Time is:')
				time.sleep(0.8)
				print(b2)
				print('')
			elif choice_first == 3 :
				print('==> Enter the given examples of Workers,Time & Worked_Place:\n')
				print('')
				a = int(input('==> Enter Workers: '))
				print('')
				b = int(input('==> Enter Time: '))
				print('')
				c = int(input('==> Enter Worked_Place: '))
				print('')
				k = (b*a)/c
				time.sleep(0.8)
				print('==> Enter the value of 2nd_Workers & 2nd_Time:\n')
				print('')
				a2 = int(input('==> Enter 2nd_Workers: '))
				print('')
				b2 = int(input('==> Enter 2nd_Time: '))
				print('')
				c2 = (a2*b2)/k
				print('The amount of 2nd_Worked_Place is :')
				time.sleep(0.8)
				print(c2)
				print('')
				
			elif choice_first == 99:
				print('Exiting....')
				time.sleep(2.0)
				break
				
			else :
				print('Error! Invalid Input. Try again...')

		arij_constant += 1
	elif user == 99 :
		print('>>>> Exiting claculator. Have a nice day...')
		time.sleep(2.2)
		exit()
	else  :
		print('>>>> Error! Invalid input. Try again...')
	
i += 1
