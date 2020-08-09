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

with open('products.txt', 'w', encoding = 'utf-8') as f:
	f.write('product, price\n')#加入欄位
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')#write in file