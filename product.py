import os # operating system
# 讀取檔案
products = []  #大清單
if os.path.isfile('products.csv'):
	print('yeah!找到檔案!')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:  #注意:逗號後不能空格
				continue
			s = line.strip().split(',')
			name = s[0]
			price = s[1]
			products.append([name, price])
	print(products)

else:
	print('找不到檔案!')

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)
s = products[0][1]
print(s)

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #f代表是創建這個檔案
	f.write('商品,價格\n')
	for p in products:               #列出product內的商品
		f.write(p[0] + ',' + str(p[1]) + '\n' ) #把列出資料寫入創建檔案內

		