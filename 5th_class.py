val = input("Please enter your name : ")
val1 = input("Please enter your password : ")
print(f"Hi {val}! Your {len(val1)*'*'} is  {len(val1)} character long")

my_cart = ["Apple", 1, 2, 3, 'Milk', 'Orange']
print(my_cart[::-1])
my_cart[0] = 'Berry'
print(my_cart)
print(len(my_cart))
new_cart = my_cart.copy()
print(new_cart)
my_cart.append(100)
print(my_cart)
print(my_cart + [3])
my_cart.extend([100, 200, 300])
print(my_cart)
my_cart.insert(3, 'Grape')
print(my_cart)
print(my_cart.index('Milk'))
my_cart.pop(5)
print(my_cart)
my_cart.remove('Orange')
print(my_cart)
my_cart.clear()
print(my_cart)

my_list = [1, 2, 3]
bonus = [5] + my_list
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)

basket = ['Bananas', 'Apples', 'Orange', 'Blubarries']
basket.remove('Bananas')
print(basket)
basket.append('Kiwi')
print(basket)
basket[0] = 'Apples'
print(basket)
basket.clear()
print(basket)
print(basket.count('Apples'))

my_list = [1, 4, 5, 6, 2, 7, 3]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
my_list.reverse()
print(my_list)
print(4 in my_list)
print(min(my_list))
print(max(my_list))
print(sum(my_list))
