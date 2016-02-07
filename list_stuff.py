my_list = [[1, 2], [3, 4]]
# now my_list[0] is [1, 2]
# and so it follows that my_list[0][0] is 1
for pair in my_list:
  pair[0] += 1 # addressing the first element of each sub-list
print(my_list)
# should print [[2, 2], [4, 4]]

# Another option is to use a class to hold your data. For example, if it
# represents X and Y coordinates:
class Point(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __repr__(self):
    return "Point({0}, {1}".format(self.x, self.y)
    
my_list_two = [Point(1, 2), Point(3, 4)]
for point in my_list_two:
  point.x += 1
print(my_list_two)
# should print [Point(2, 2), Point(4, 4)]