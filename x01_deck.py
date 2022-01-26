#!python3

"""
Create a list of cards
the cards should be denoted with a number or A, J, Q, K, T (for ace, jack, queen, king or ten)
as well as a suit
"""

def createDeck():
  ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
  suits = ['C','D','H','S']
  d = []
  for i in ranks:
    for u in suits:     
      deck = [i + u]
      d = d + deck
  return d

  

#createDeck()




def main():
  deck = createDeck()
  print(deck)
  assert "JH" in deck 
  assert "AC" in deck 
  assert "TD" in deck 
  assert len(deck) == 52
  
if __name__ == "__main__":
  main()