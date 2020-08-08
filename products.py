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