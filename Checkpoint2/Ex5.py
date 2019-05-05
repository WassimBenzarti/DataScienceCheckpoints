import time

#Naive approach
def fib(n):
  if n <= 1: return 1
  return fib(n-1)+fib(n-2)



def fibFast(n, cache):
  if n <= 1: return 1
  if(not n-1 in cache): cache[n-1] = fibFast(n-1,cache)
  if(not n-2 in cache): cache[n-2] = fibFast(n-2,cache)
  return cache[n-1] + cache[n-2]

n = 30

start = time.time()
print("fib of {} is {}".format(n, fib(n)))
end = time.time()
print("Ended in {} seconds \n".format(end-start))


start = time.time()
cache={}
print("fibFast of {} is {}".format(n, fibFast(n, cache)))
end = time.time()
print("Ended in {0:.10f} seconds".format(end-start))
# Much better