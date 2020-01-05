import random,math
import time
n=int(input('How many numbers you want:'))
s=input('Enter Operator:')
class phone:
	caller_id={}
	for i in range(n):
		y=random.randint(100000,999999)
		z=[' '+str(y)]
	
		
	def ideafirst(phone):
		caller_id={}
		k=n//4
		for i in range(k):
			y=random.randint(100000,999999)
			z=['9826' + str(y)]
			for caller_id in z:
				print(caller_id)
	def ideasecond(phone):
		caller_id={}
		b=n//3
		for i in range(b):
			y=random.randint(100000,999999)	
			z=['9926'+str(y)]
			for caller_id in z:
				print(caller_id)
	def ideathird(phone):
		caller_id={}
		c=n//2
		for i in range(c):
			y=random.randint(100000,999999)
			z=['9977'+str(y)]
			for caller_id in z:
				print(caller_id)
	def airtel1(phone):
		caller_id={}
		q=n//2
		for i in range(q):
			y=random.randint(100000,999999)
			z=['9893'+str(y)]
			for caller_id in z:
				print(caller_id)
			
	def airtel2(phone):
		caller_id ={}
		a=n//3
		
		for i in range(a):
			y=random.randint(100000,999999)
			z=['9981'+str(y)]
			for caller_id in z:
				print(caller_id)
	def airtel3(phone):
		caller_id={}
		b=n//2
		for i in range(b):
			y=random.randint(100000,999999)
			z=['9735'+str(y)]
			for caller_id in z:
				print(caller_id)
	def jio1(phone):
		caller_id={}
		r=n//6
		for i in range(r):
			y=random.randint(100000,999999)
			z=['8839'+str(y)]
			for caller_id in z:
				print(caller_id)
	def jio2(phone):
		caller_id={}
		t=n//5
		for i in range(t):
			y=random.randint(100000,999999)
			z=['7000'+str(y)]
			for caller_id in z:
				print(caller_id)
	def jio3(phone):
		caller_id={}
		o=n//4
		for i in range(o):
			
			y=random.randint(100000,999999)
			z=['6263'+str(y)]
			for caller_id in z:
				print(caller_id)
	def jio4(phone):
		caller_id={}
		p=n//2
		for i in range(p):
			y=random.randint(100000,999999)
			z=['8770'+str(y)]
			for caller_id in z:
				print(caller_id)
	
main=phone
if s== 'idea':
	print('These all are Madhya pradesh idea sim mobile numbers ')
	time.sleep(3)
	main.ideafirst(phone)
	main.ideasecond(phone)
	main.ideathird(phone)
elif s == 'airtel':
	print('These all are Madhya pradesh airtel sim mobile numbers ')
	time.sleep(3)
	main.airtel1(phone)
	main.airtel2(phone)
	main.airtel3(phone)
elif s == 'jio':
	print('These all are Madhya pradesh jio sim mobile numbers ')
	time.sleep(3)
	print('wait for few seconds.....')
	time.sleep(2)
	main.jio1(phone)
	main.jio2(phone)
	main.jio3(phone)
	main.jio4(phone)
else:
	print('invaild operator')
	print('please give vaild operator.....')
