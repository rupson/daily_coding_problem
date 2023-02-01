from typing import TypeVar


T = TypeVar('T')

def get_last_elt(l: list[T]) -> T:
  if (len(l) == 0): 
    raise Exception("no")
  return l[len(l) - 1]

def get_first_elt(l: list[T]) -> T:
  if (len(l) == 0): 
    raise Exception("no")
  return l[0]

def get_available_nums(remaining_nums) -> list[int]:
  if remaining_nums == None:
    return list(range(len(bigger_or_smaller)))
  return remaining_nums


def unjumble(bigger_or_smaller: list[str], remaining_nums = None) -> list[int]:
  available_nums = get_available_nums(remaining_nums)
  if len(bigger_or_smaller) == 0:
    return []

  if (get_last_elt(bigger_or_smaller) == '+'):
    return unjumble(bigger_or_smaller[0:-1], available_nums[0:-1]) + [get_last_elt(available_nums)]

  if (get_last_elt(bigger_or_smaller) == '-'):
    return unjumble(bigger_or_smaller[0:-1], available_nums[1:]) + [get_first_elt(available_nums)]

  if (get_last_elt(bigger_or_smaller) == None):
    return [available_nums[0]]

  raise Exception("no")


if __name__ == "__main__":
  bigger_or_smaller = [None, '+', '+','-','+']
  print(unjumble(bigger_or_smaller))
  assert(unjumble(bigger_or_smaller) == [1,2,3,0,4])