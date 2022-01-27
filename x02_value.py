#!python3
from x01_deck import *


def value():
  x = createDeck()
  boom = []
  for a in x:
    boom.append(a)
    cool = sum(boom)
    
    print(boom)

  '''
  input:
  list hand: hand is a list of strings that contains the cards in the hand
  eg: ['AH','3D','4S']
  
  return:
  int the total value of the hand
  may return a list if the hand contains an Ace
  eg:
  '''
  value()
  print(value)
  return None


def main():
  assert value(['AH','3D','4S']) ==[8,18]
  assert value(['KH','TD']) == 20
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 26

if __name__ == "__name__":
  main()
