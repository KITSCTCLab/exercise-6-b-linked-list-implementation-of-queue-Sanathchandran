class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    temp = Node(data)
    if self.head == None:
      self.head = temp
      temp.next = None
    else:
      temp.next = self.head
      self.head = temp

  def pop(self) -> None:
    if self.head == None:
      pass
    else:
      self.head = self.head.next

  def status(self):
    """
    It prints all the elements of stack.
    """
    temp = self.head
    while temp != None:
      print(temp.data, "=>", sep = "", end = "")
      temp = temp.next
    print("None")


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
