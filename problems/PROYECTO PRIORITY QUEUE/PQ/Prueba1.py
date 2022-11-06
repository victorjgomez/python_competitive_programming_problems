from PQ import PriorityQueue

pq = PriorityQueue()

'''
print(f"peek {pq.peek()}")

pq.insert_or_update(152,"A")

print(f"peek {pq.peek()}")

print(pq.extract())

print(f"peek {pq.peek()}")

print(pq.extract())

print(f"peek {pq.peek()}")
'''

pq.insert_or_update(152,"A")
pq.insert_or_update(152,"B")
pq.insert_or_update(96,"T")
pq.insert_or_update(0,"Q")
pq.insert_or_update(2,"W")
pq.insert_or_update(8,"T")
pq.insert_or_update(20,"B")

pq.print_tree()

print(f"extract {pq.extract()}")

pq.print_tree()

print(f"extract {pq.extract()}")

pq.print_tree()

print(f"extract {pq.extract()}")

pq.print_tree()

print(f"extract {pq.extract()}")

pq.print_tree()

print(f"extract {pq.extract()}")

pq.print_tree()

print(f"extract {pq.extract()}")

pq.print_tree()