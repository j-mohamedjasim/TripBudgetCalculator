print('Warning!!!')
print()
print('This calculator is to calculate and help divide the cost to equal')
print()
print('Please answer the following questions and it will give you how much person should contribute and it will give you the expected budget for each person')
print()

num = int(input('How many adult are travelling? '))

hotel = int(input('What is the total cost of the hotel together? '))

tollfee = int(input('What is the toll fee? '))

carpark = int(input('How much would you consider to pay for the car park? '))

grocery = int(input('How much would you pay for grocery if needed? '))

petrol = int(input('How much would you spend or spent for petrol? '))

vplaces = int(input('How much you paying for visiting places? '))

meal = int(input('How much have/would you pay for meal? '))

clothes = int(input('How much would you pay for clothes/fashion? '))

taxi = int(input('How much you pay for taxi? (if applicable) '))

ptransport = int(input('How much would you pay for public transport? (if applicable) '))

things = int(input('How much would you concider to pay for other things such as toys? '))


total = hotel + tollfee + carpark + grocery + petrol + vplaces + meal + clothes + taxi + ptransport +things

divide = total / num

print()
print(f"The total amount is £{total}")
print()

print(f'Each person in the trip will have to contribute £{divide}')
print()
