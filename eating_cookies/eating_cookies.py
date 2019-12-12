#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache={}): 
  
  if n in cache:
    print("n",n)
    print("cache[n]",cache[n])
    print("cache",cache)
    return cache[n]    

  if n==0:
        value= 1
  elif n<0:
        value= 0
  elif n>0:
      value= eating_cookies(n-1)+eating_cookies(n-2)+eating_cookies(n-3)

  cache[n] = value
  return value        
print(eating_cookies(50))
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')