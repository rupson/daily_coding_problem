from typing import List

def next_index (arr, current_index):
  if (current_index == (len(arr)-1)):
    return 0
  return current_index + 1

def apply_offset_by_maximum (max, offset, n):
  return (n+offset) % max


def find_index(array, x, boundaries):
  offset = boundaries["min"]
  arrayLength = len(array)
  def apply_offset (n: int):
    return apply_offset_by_maximum(arrayLength, offset, n)
  min_index = boundaries["min"]
  max_index = boundaries["max"]

  search_index = apply_offset((apply_offset(max_index) + apply_offset(min_index)) // 2)
  while (array[search_index] != x):
    print(f"search_index: {search_index}\nmax_index: {max_index}\nmin_index: {min_index}\n")
    if (array[search_index] < x):
      min_index = search_index
    elif (array[search_index] > x):
      max_index = search_index
    search_index = apply_offset((apply_offset(max_index) + apply_offset(min_index)) // 2)
  return search_index

def find_boundary_indexes(array: List[int]):
  max_index = len(array) - 1
  search_index = (max_index) // 2
  min_index = 0
  
  while (min_index < search_index and max_index > search_index):
    if (array[search_index] < array[max_index]):
      max_index = search_index
    if (array[search_index] > array[max_index]):
      min_index = search_index
    search_index = (max_index + min_index) // 2
  return {"min": next_index(array, search_index), "max": search_index }

if __name__ == "__main__":
  rotated = [13,18,25,2,8,10]
  # rotated = [13,14,15,16,17,18,19,20,25,2,8,10,11,12]
  # not_rotated = [2,8,10,13,18,25]
  print(apply_offset_by_maximum(6, 3, 3))
  boundaries = find_boundary_indexes(rotated)
  print(f"boundaries>>>{boundaries}")
  print(find_index(rotated, 8, boundaries))