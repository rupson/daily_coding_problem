## 716 22/11/2020

from typing import List

def no_of_bytes(as_bytes: List[int]):
  if len(as_bytes) % 8 == 0:
    return len(as_bytes) // 8
  raise Exception('value is not in bytes')

def has_leading_10_on_tail_bytes(as_bytes_tail: List[int]):
  if len(as_bytes_tail) == 0:
    return True
  if as_bytes_tail[0:2] != [1,0]:
    return False
  return has_leading_10_on_tail_bytes(as_bytes_tail[8::])

def is_utf_encoded(as_bytes: List[int]):
  try:
    num_of_bytes = no_of_bytes(as_bytes)
    if num_of_bytes > 3:
      return False
    if num_of_bytes == 1:
      return as_bytes[0] == 0
    return all(as_bytes[0:num_of_bytes]) and as_bytes[num_of_bytes] == 0 and has_leading_10_on_tail_bytes(as_bytes[8::])
  except Exception:
    return False

if __name__ == "__main__":
  test = [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0]
  print(is_utf_encoded(test))

