products = []  #大清單
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)
s = products[0][1]
print(s)

for p in products:
	print(p[0], '的價格是', p[1])

	