from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.pop())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)
print(type(q))

