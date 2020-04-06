class SortedList(list):
  def __init__(self, values):
    super().__init__(values)
    self.sort()    
    
  def append(self, value):
    super().append(value)
    self.sort()
    
class SuperDict(dict):
  fallback_value = "There is no such a key"
  def __init__(self, dic):
    super().__init__(dic)
    
  def __getitem__(self, key):
    try:
      return super().__getitem__(key)
    except KeyError:
      return self.fallback_value
	# Alternatively
	# def __missing__(self, key):
		# return self.fallback_value


d = SuperDict({"k": 10, "b": 5})
print(d["k"])
print(d["c"])
    
lst1 = SortedList([2,1,5,3])
print(lst1)

lst1.append(0.5)
print(lst1)