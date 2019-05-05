import time

# Haha, "friends" that's cute
# shit, how I'm going to start ...

start = time.time()
def sumDivSlow(number): 
  sum=0
  for i in range(1,int(number/2)+1):
    if(number % i == 0):
      sum += i
  return sum

for i in range(0,1000): # okay, til now I'm okay
  for j in range(0,1000):
    if(sumDivSlow(i) == j and sumDivSlow(j) == i):
      print("{} and {} are friends".format(i, j))
end = time.time()
print("Ended in {} seconds".format(end-start))
# 42 seconds... This is very slow!

# I'm gonna try making a faster algorithm :p
def sumDiv(number):
  sum=0
  j = 2
  while(j *j < number):
    if(number % j == 0):
      if(number / j == j):
        sum+= j
      else:
        sum+= j+ number/j
    j+=1
  return int(sum)+1

print(sumDiv(220))

start = time.time()
for i in range(1,1000): # okay, til now I'm okay
  for j in range(1,1000):
    if(sumDiv(i) == j and sumDiv(j) == i):
      print("{} and {} are friends".format(i, j))
end = time.time()

print("Ended in {} seconds".format(end-start))
# 9 seconds... much better x)