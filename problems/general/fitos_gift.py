import math
from typing import List


def get_list_card_number_and_position_x(card_numbers_input: str):
 list_card_number = []
 index = 0
 position_x = -1

 for number in card_numbers_input:
  if number == 'x':
   position_x = index
   list_card_number.append(0)
  else:
   list_card_number.append(int(number))

  index += 1

 return {"list_card_number": list_card_number, "position_x": position_x}


def get_double_every_other(list_card_number: List[int]):
 double_every_other = []
 index = 2

 for i in range(len(list_card_number)-1, -1, -1):
  if index % 2 == 0:
   double_every_other.append(list_card_number[i]*2)
  else:
   double_every_other.append(list_card_number[i])

  index += 1

 double_every_other.reverse()

 return double_every_other

def get_value_to_sum(number):
 if (number < 10):
  return number
 else:
  return math.floor(number / 10) + number - (math.floor(number / 10) * 10)

def get_sum(double_every_other: List[int]):
 sum = 0
 for number in double_every_other:
  sum += get_value_to_sum(number)

 return sum

def get_required_one_digit_number(sum: int, last: int):
 modulo = 10
 remainder = sum*9 % modulo

 if remainder == last:
  return 0
 elif remainder < last:
  return last - remainder
 else:
  return modulo - (remainder-last)

def get_required_one_digit_number_when_x_is_last(sum: int):
 modulo = 10
 remainder = sum*9 % modulo

 return remainder


if __name__ == "__main__":
 n = int(input())
 card_numbers_input = str(input())

 dict_list_card_number_and_position_x = get_list_card_number_and_position_x(card_numbers_input)

 list_card_number = dict_list_card_number_and_position_x["list_card_number"]
 position_x = dict_list_card_number_and_position_x["position_x"]
 last = list_card_number[len(list_card_number)-1]

 double_every_other = get_double_every_other(list_card_number[:n-1])

 sum = get_sum(double_every_other)

 #print(sum)

 required_one_digit_number = -1

 if position_x == n-1:
  required_one_digit_number = get_required_one_digit_number_when_x_is_last(sum)
 else:
  for i in range(10):
   list_card_number[position_x] = i
   double_every_other = get_double_every_other(list_card_number[:n - 1])
   sum = get_sum(double_every_other)

   if sum*9 %10 == last:
    required_one_digit_number = i
    break

 print(required_one_digit_number)

