def check():
	one = float(input("enter a side "))
	two = float(input("Enter another side "))
	three = float(input("Enter a last side "))
	a= 0
	b= 0
	c= 0
	if one > two and one > three:
		c += one
		a += two
		b += three
	elif two > three:
		c += two
		a+= one
		b += three
	else:
		c+= three
		a += one
		b += two

	jj = a **2
	kk = b **2
	ll = c **2
	if jj + kk == ll:
		print ("Pythagorean Triple")
		
	else:
		print ("NOT A TRIPLE")

check()