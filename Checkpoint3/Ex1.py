from functools import reduce

list =[]
for i in range(6):
  list += int(input("Type {} element here\n".format(i)))

# Sorry, too lazy to do the for loop x)
print(
  reduce(lambda x,y: x+y, list)
)