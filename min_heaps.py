class min_heap():
  def __init__(self):
    self.data=[]
  def _sift_up(self, index):
    while (index-1)//2 >= 0:
      current, parent=self.data[index], self.data[(index-1)//2]
      if current<parent:
        self.data[index], self.data[(index-1)//2]=parent, current
        index=(index-1)//2
      else:
        break
  def _sift_down(self):
    if len(self.data)==0:
      return 
    self.data[0], self.data[-1]=self.data[-1], self.data[0]
    self.data.pop()
    index=0
    while (2*index+1)<len(self.data):
      if (2*index+2)<len(self.data):
        if self.data[2*index+1]>=self.data[2*index+2]:
          target=2*index+2
        else:
          target=2*index+1
        parent, current = self.data[index], self.data[target]
        if parent > current:
          self.data[index], self.data[target] = current, parent
          index=target
          continue
      else:
        if self.data[2*index+1]<self.data[index]:
          target=2*index+1
          parent, current = self.data[index], self.data[target]
          if parent > current:
            self.data[index], self.data[target] = current, parent
            index=target
            continue
      break
      
  def push_value(self, value):
    self.data.append(value)
    self._sift_up(len(self.data)-1)
  def pop_min(self):
    self._sift_down()
  def _is_valid(self):
    if len(self.data)<=1:
      return True
    for i in range(len(self.data)):
      if (2*i+1)<len(self.data):
        if (2*i+2)<len(self.data):
          if ((self.data[i]<=self.data[2*i +2]) and (self.data[i]<=self.data[2*i+1])):
            continue
          else:
            return False
        else:
          if self.data[i]<=self.data[2*i +1]:
            continue
          else:
            return False
    return True

    




