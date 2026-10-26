# https://matcomgrader.com/problem/9695/bus/
"""
Reference linked-list
https://realpython.com/linked-lists-python/#introducing-collectionsdeque
"""
import math
from collections import deque

# import Counter from collections
from collections import Counter, defaultdict

def get_stops(ps_list):
    stops = set(ps_list)
    sorted_stops = list(stops)
    sorted_stops.sort()
    return sorted_stops

def get_dict_passenger_index(passengers):
    dict_passenger_index = defaultdict(lambda: list())

    index = 1
    for passenger in passengers:
        dict_passenger_index[passenger].append(index)
        index += 1

    return dict_passenger_index


def get_updated_dict_passenger_exit(passenger,
                                    right_or_left,
                                    dict_passenger_index,
                                    dict_passenger_exit):
    dict_passenger_exit_copy = dict_passenger_exit.copy()
    dict_passenger_exit_copy[dict_passenger_index[passenger][0]] = right_or_left

    return dict_passenger_exit_copy

def get_updated_dict_passenger_index(passenger,
                                     dict_passenger_index):
    dict_passenger_index_copy = dict_passenger_index.copy()
    dict_passenger_index_copy[passenger] = dict_passenger_index[passenger][1:]

    return dict_passenger_index_copy


def get_direction(cont, n):
    half = math.ceil(n / 2)
    if (n - cont) < half:
        return "R"
    else:
        return "L"



if __name__ == "__main__":
    input1 = list(map(int, input().rstrip().split()))
    n = input1[0]
    k = input1[1]
    passengers_list = list(map(int, input().rstrip().split()))

    stops = get_stops(passengers_list)
    dict_passenger_exit = {}
    dict_passenger_index = get_dict_passenger_index(passengers_list)
    counter = Counter(passengers_list)
    passengers_deque = deque(passengers_list)

    for stop in stops:
        for _ in range(counter[stop] + 1):
            cont = 0
            for passenger in passengers_deque:
                cont += 1
                if passenger == stop:
                    right_or_left = get_direction(cont-1, len(passengers_deque))
                    dict_passenger_exit = get_updated_dict_passenger_exit(passenger, right_or_left, dict_passenger_index, dict_passenger_exit)
                    dict_passenger_index = get_updated_dict_passenger_index(passenger, dict_passenger_index)

                    passengers_deque.remove(stop)
                    break


    # print(dict_passenger_exit)

    result = ""
    for i in range(1, n+1):
        result += dict_passenger_exit[i]

    print(result)