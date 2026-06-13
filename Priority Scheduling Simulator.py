def sift_up(heap, index):
    while (index-1)//2>=0:
        if heap[index][1:3] < heap[(index-1)//2][1:3]:
            heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]
            index = (index-1)//2
        else:
            break
    return None

def heap_push(heap, value):
    heap.append(value)
    return sift_up(heap, len(heap)-1)
def sift_down(heap, index):
    while (2*index+1)<len(heap):
        #It has both children
        if (2*index+2)<len(heap):
            #left smaller than right,
            if heap[2*index+1][1:3]<heap[2*index+2][1:3]:
                 #We compare to the current,
                if heap[index][1:3]<=heap[2*index+1][1:3]:
                    break
                #If it's not smaller,
                heap[index], heap[2*index+1] = heap[2*index+1], heap[index]
                index = 2*index + 1
                continue
            #right smaller than left,
            else:
                if heap[index][1:3]<=heap[2*index+2][1:3]:
                     break
                    #If it's not smaller,
                heap[index], heap[2*index+2] = heap[2*index+2], heap[index]
                index = 2*index + 2
                continue
        #It has only the left
        else:
            if heap[index][1:3]<=heap[2*index+1][1:3]:
                break
            #If it's not smaller,
            heap[index], heap[2*index+1] = heap[2*index+1], heap[index]
            index = 2*index + 1
    return None
def heap_pop(heap):
    if not heap:
        raise IndexError()
    root=heap[0]
    heap[0]=heap[-1]
    heap.pop()
    if heap:
        sift_down(heap, 0)
    return root
class PriorityQueue:
    def __init__(self):
        self.data=[]
        self.counter=0
    def push(self, item, priority):
        heap_push(self.data, (item, priority, self.counter))
        self.counter +=1
    def pop(self):
        return heap_pop(self.data)[0]
    def is_empty(self):
        return len(self.data)==0   
def schedule_tasks(tasks):
    my_priority_queue=PriorityQueue()
    output=[]
    for i in tasks:
        my_priority_queue.push(i[0], i[1])
    while not my_priority_queue.is_empty():
        output.append(my_priority_queue.pop())
    return output
