import math
import time

#Using for loop
#Start
start = time.time()
number = int(input("Type a number: "))
fact = 1
for i in range(1,number+1):
  fact *= i
end = time. time()
#End
print(
  "Using for loop: fact of {} is {}\nTime spent: {}"
  .format(number, fact, end-start)
)

#Another method
#Start
start = time.time()
fact = math.factorial(number)
end = time. time()
#End
print(
  "Using math: fact of {} is {}\nTime spent: {}"
  .format(number, fact,end-start)
)