import heapq
def djikstra(graph, start, targets):
  distance={start:0}
  pq=[(0, start)]
  parents={start:None}
  while pq:
    current_distance, node=heapq.heappop(pq)
    if current_distance != distance[node]:
      continue
    for neighbor, weight in graph[node]:
      new_distance=current_distance + weight
      if new_distance < distance.get(neighbor, float("inf")):
        parents[neighbor]=node
        distance[neighbor]=new_distance
        heapq.heappush(pq, (new_distance, neighbor))
  paths=[]
  for nodes in targets:
    if nodes in distance:
      temp=[]
      current=nodes
      while current!=start:
        temp.append(current)
        current=parents[current]
      temp.append(start)
      paths.append(temp.copy()[::-1])
    else:
      paths.append("None")
  return paths, [distance.get(i, float("inf")) for i in targets]
