days = int(input('How many day\'s temperature '))

temp = []
i = 1
while i <= days:
  inpTemp = int(input(f'Day {i}\'s high temperature '))
  temp.append(inpTemp)
  i += 1

averageTemp = sum(temp)/len(temp)  
print(f'Average = {averageTemp}')

j=0
for t in temp:
  if t > averageTemp:
    j+= 1
print(f'{j}day(s) above average')    
