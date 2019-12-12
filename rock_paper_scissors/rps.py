#!/usr/bin/python

import sys

def rock_paper_scissors(roundRemaining):
      
      moves=["rock","paper","scissors"]
      listsOfPossibleOutcomes=[]
      def helperfunc(roundRemaining, result=[]):
            #base case
            if roundRemaining==0:
                  print("result", result)
                  return listsOfPossibleOutcomes.append(result)
            for move in moves:
                print("move",result,move)             
                helperfunc(roundRemaining-1,result+[move])
      helperfunc(roundRemaining)
      return listsOfPossibleOutcomes

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')