import pyinputplus as pyip

# initialize price dictionary
price_dict = {
    'wheat': 2.99,
    'white': 1.99,
    'sourdough': 3.99,
    'chicken': 4.99,
    'turkey': 3.99,
    'ham': 2.99,
    'tofu': 5.99,
    'cheddar' : 1.99,
    'swiss' : 1.99,
    'mozzarella' : 1.99,
    'No Cheese' : 0.00,
}

#
# Bread
#
bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='Select a bread type: ')
print('You selected', bread_type)

#
# Protein
#
protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt='Select a protein type: ')
print('You selected', protein_type)


#
# Cheese
#
cheese_yesNo = pyip.inputYesNo(prompt='Do You Want Cheese? ')

if cheese_yesNo == 'yes':
    cheese_type = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], prompt='Select a cheese type: ')
    print('You selected', cheese_type)
else:
    cheese_type = ('No Cheese')
    print('No Cheese')


#
# Toppings
#
toppingsList = ['mayo', 'mustard', 'lettuce', 'tomato']
toppingsChoices = {}

for topping in toppingsList:
    yesNo = pyip.inputYesNo(prompt=f'Do You Want {topping}? ')
    if yesNo == 'yes':
        toppingsChoices[topping] = yesNo
    else:
        continue
    
print('Your selected toppings:')
for topping, choice in toppingsChoices.items():
    if choice == 'yes':
        print(f'  {topping}')




#
# Sandwich Count
#
sandwiches_Count = pyip.inputInt(prompt='How Many Sandwiches Do You Want? ', min=1)



# Calculate the total price of the sandwich
bread_price = price_dict[bread_type]
protein_price = price_dict[protein_type]
cheese_price = price_dict[cheese_type]

total_price = ((bread_price + protein_price + cheese_price) * sandwiches_Count)


print(f'Your {sandwiches_Count} sandwich(es) will have:\n'
      f'  {bread_type} Bread \n'
      f'  {protein_type} Protein\n'
      f'  {cheese_type}')
for topping, choice in toppingsChoices.items():
    if choice == 'yes':
        print(f'  {topping}')

print(f'Your Total Cost = {total_price}')


