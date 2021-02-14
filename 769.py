"""
Daily Programming Challenge #769
Author: rupson
"""

import random
import math

def roll_dice() -> int:
  return random.randint(1,6)

def until_5_6():
  results = []
  while True:
    if (len(results) < 2):
      results.append(roll_dice())
    elif ((results[::-1][0]==6) and (results[::-1][1]==5)):
      return len(results)
    else: 
      results.append(roll_dice())

def until_6_6():
  results = []
  while True:
    if (len(results) < 2):
      results.append(roll_dice())
    elif ((results[::-1][0]==6) and (results[::-1][1]==6)):
      return len(results)
    else: 
      results.append(roll_dice())

if __name__ == "__main__":
  list_length = 1000000
  no_of_tries = {
    "five_to_six": [],
    "six_to_six": []
  }
  while (len(no_of_tries["five_to_six"]) < list_length):
    if (len(no_of_tries["five_to_six"]) % (list_length / 100)) == 0:
      percent_complete = math.floor((len(no_of_tries["five_to_six"]) / list_length) * 50)
      print(f"rolling {percent_complete}% complete")
    no_of_tries["five_to_six"].append(until_5_6())
  while (len(no_of_tries["six_to_six"]) < list_length):
    if (len(no_of_tries["six_to_six"]) % (list_length / 100)) == 0:
      percent_complete = math.floor((len(no_of_tries["six_to_six"]) / list_length) * 50) + 50
      print(f"rolling {percent_complete}% complete")
    no_of_tries["six_to_six"].append(until_6_6())
  
  average_5_6 = sum(no_of_tries["five_to_six"]) / len(no_of_tries["five_to_six"])
  average_6_6 = sum(no_of_tries["six_to_six"]) / len(no_of_tries["six_to_six"])

  print(f"average tries, 5 then 6: {average_5_6}")
  print(f"average tries, 6 then 6: {average_6_6}")