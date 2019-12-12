#!/usr/bin/python

import argparse

def find_max_profit(prices):
      sumOfSmallBig=0
      for firstRound in prices:
            for secondRound in prices[:prices.index(firstRound)]:
                  if secondRound<firstRound:                                            
                        if firstRound-secondRound>sumOfSmallBig:
                              sumOfSmallBig=firstRound-secondRound             
                  elif secondRound==prices[len(prices)-2] and sumOfSmallBig==0:
                        sumOfSmallBig=firstRound-secondRound
      return sumOfSmallBig

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} will be made of the prices: {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))