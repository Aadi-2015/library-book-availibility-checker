items = ['maths','science']
count = [12,0]
book = {item: count for item,count in zip(items,count)}
print(f'books: {book}')
stock=[item for item in items if book[item]>0]
print(stock)
item1 = input('enter your choice: ')
if item1 not in book or book[item1]==0:
    print('out of stock')
    exit()
price = [662,778]
tax=int(input("Enter the amount of markup: "))