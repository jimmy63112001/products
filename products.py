products = []
while True:
	name = input('enter name: ')
	if name == 'q':
		break
	price = input('enter price: ')
	#p = []
	#p.append(name)
	#p.append(price)
	#products.append(p)
	products.append([name, price])
print(products) 

for p in products:
	print(p[0], '的價格是', p[1])