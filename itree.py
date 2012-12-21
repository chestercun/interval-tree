# binary tree node
class Node:
  """
  Helper class for IntervalTree implementation
  """
  def __init__(self,value):
    """
    Start a node with a numeric value
    """
    self.value = value
    self.objects = []
    self.left = None
    self.right = None

  def add_reference(obj):
    """
    Add an object reference to the "objects" list
    """
    self.objects.append(obj)

# interval tree implementation
class IntervalTree:
  def __init__(self):
    """
    Initialize a tree with zero nodes
    """
    self.head = None

  def add(self,start,end,obj):
    """
    This adds an entire interval to BST
    Takes two numerics for start and end.
    Third parameter is the object reference
    """
    print ""

  def insert(self,value):
    """
    Inserts a new interval endpoint into BST
    """
    if (self.head==None):
      self.head = Node(value)
    else:
      self.__insert__(self.head,value)

  def __insert__(self,node,value):
    """
    Helper function for insert
    """
    if value<node.value:
      if node.left==None:
        node.left = Node(value)
      else:
        self.__insert__(node.left,value)
    else:
      if node.right==None:
        node.right = Node(value)
      else:
        self.__insert__(node.right,value)


  def inorder(self,fn):
    """
    Traverse the binary search tree
    Takes a function as the only parameter
    """
    self.__inorder__(self.head,fn)

  def __inorder__(self,node,fn):
    """
    Helper function for in-order BST traversal
    """
    if (node==None):
      return
    self.__inorder__(node.left,fn)
    fn(node)
    self.__inorder__(node.right,fn)




