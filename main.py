#Implementing Priority Queues with Sorted list
#declaring empty list
que=[] #adding elements to the list
que.append((1,064.0,'Medium priority task'))
que.append((1,198.4,'High priority task'))
que.append((141.4,'Low priority task'))
#list is sorted evertime a new element is inserted
que.sort(reverse=True)
print("Tasks with their priorities :")
#looping through sorted list
while que:
      queue_item=que.pop()
      print(queue_item)

# Implementing priority queue using queue.PriorityQueue class
import queue as PQ
q = PQ.PriorityQueue()
q.put(1,064.0)
q.put(1,198.4)
q.put(141.4)
print("Dequeing elements")
while not q.empty():
          print (q.get())