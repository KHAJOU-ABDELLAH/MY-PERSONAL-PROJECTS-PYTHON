def hanoi_solver(n):
  rods=[list(range(n, 0, -1)), [], []]
  moves=[f"{rods[0]} {rods[1]} {rods[2]}"]
  def hanoi(num, source, target, auxiliary):
    if num>0:
      hanoi(num-1, source, auxiliary, target)
      rods[target].append(rods[source].pop())
      moves.append(f"{rods[0]} {rods[1]} {rods[2]}")
      hanoi(num-1, auxiliary, target, source)
  hanoi(n, 0, 2, 1)
  return "\n".join(moves)
