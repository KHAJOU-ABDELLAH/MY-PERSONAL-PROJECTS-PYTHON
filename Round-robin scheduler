from collections import deque
n, q = map(int, input().split())
to_process=deque()
processed=[]
for _ in range(n):
  task, time = input().split()
  to_process.append((task, int(time)))
while len(to_process)>0:
  task, time = to_process[0][0], to_process[0][1]
  if time<=q:
    processed.append(task)
    to_process.popleft()
  else:
    time -=q
    to_process.append((task, time))
    to_process.popleft()
print(" ".join(processed))
  
