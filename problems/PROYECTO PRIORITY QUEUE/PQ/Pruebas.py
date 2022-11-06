# importing "heapq" to implement heap queue
import heapq
data = "A"
priority = 1
heap = []
data_dict = {}

heapq.heappush(heap, (9,"A"))
heapq.heappush(heap, (9,"B"))
heapq.heappush(heap, (4,"C"))
heapq.heappush(heap, (7,"C"))
heapq.heappush(heap, (3,"Q"))
heapq.heappush(heap, (3,"C"))

#data_dict[data] = priority


print(heap)


