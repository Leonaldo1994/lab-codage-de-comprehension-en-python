# -*- coding: utf-8 -*-
"""

@author: Leonaldo1994
"""

def exo_03(liste):
  pairs = [l for l in liste if l % 2 == 0 ] 
  return sorted(pairs)

def main():
  print( exo_03( [ 3, 5, 7, 9, 98, 13, 24, 56, 17, 9, 8 ] ) )

if __name__== "__main__":
  main()
