__all__ = ["IntervalTree"]

# regular leaf node
class Node:
  """
  Helper class for TreeNode implementation
  """
  def __init__(self):
    """
    Empty node with only a parent ptr and objects hash
    """
    # spanning
    self.objects = {}
    # node references
    self.parent = None

  def push(self,obj):
    """
    Add an object reference to the "objects" list
    """
    hashref = self.objects
    if not hashref.has_key(obj):
      hashref[obj] = True

  def is_leaf(self):
    """
    Check if instance is "base" class only
    """
    return self.__class__ == Node

# binary tree node
class TreeNode(Node):
  """
  Helper class for IntervalTree implementation
  Inherits from a regular node
  """
  def __init__(self,value):
    # base constructor
    Node.__init__(self)
    # elemental endpoint
    self.value = value
    # node references
    self.left = Node()
    self.right = Node()

# interval tree implementation
class IntervalTree:
  def __init__(self):
    """
    Initialize a tree with zero nodes
    """
    self.__reset__()

  def __reset__(self):
    """
    Resets the tree and the cached endpoints
    saved from load method calls
    """
    self.head = None
    self.endpoints = {}

  def add(self,start,end,obj):
    """
    This adds an entire interval to BST
    Takes two numerics for start and end.
    Third parameter is the object reference
    """
    # first make sure the interval is there
    self.insert( start )
    self.insert( end )
    # then add the reference
    #_min = self.getMin(self.head)
    #_max = self.getMax(self.head)

    # hack infinities
    _min = -1000000 #self.getMin(self.head)
    _max =  1000000 #self.getMax(self.head)
    #print "min %.01f max %.01f" % (_min,_max)
    self.__match__( self.head, start, end, _min, _max, obj )

  def getMin(self, node):
    # store ref
    n = node
    while (not n.left.is_leaf()):
      n = n.left
    return n.value

  def getMax(self, node):
    # store ref
    n = node
    while (not n.right.is_leaf()):
      n = n.right
    return n.value

  def __match__(self, node, start, end, _min, _max, obj):
    """
    Helper function for add
    This traverses the interval tree
    and adds the obj-ref to the appropriate nodes
    """
    if ( node.is_leaf() ):
      node.push(obj)
      return

    if start <= _min and _max <= end:
      node.push(obj)
    else:
      if start < node.value:
        self.__match__(node.left, start, end, _min, node.value, obj)
      if node.value < end:
        self.__match__(node.right, start, end, node.value, _max, obj)


  def insert(self,value):
    """
    Inserts a new interval endpoint into BST
    """
    if (self.head==None):
      self.head = TreeNode(value)
    else:
      self.__insert__(self.head,value)

  def __insert__(self,node,value):
    """
    Helper function for insert
    """
    if value < node.value:
      #if node.left==None:
      if node.left.__class__ == Node:
        node.left = TreeNode(value)
        node.left.parent = node
      else:
        self.__insert__(node.left,value)
    elif value > node.value:
      #if node.right==None:
      if node.right.__class__ == Node:
        node.right = TreeNode(value)
        node.right.parent = node
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
    #if (node==None):
    if ( node.is_leaf() ):
      return
    self.__inorder__(node.left,fn)
    fn(node)
    self.__inorder__(node.right,fn)

  def load(self,value):
    """
    Let the user load all of their points
    at once, then let them call unload
    to build their tree. Lastly, they can insert
    their objects into the tree
    """
    ep = self.endpoints
    if not ep.has_key(value):
      ep[value] = True
    #print ep

  def unload(self):
    """
    This generates a list of all endpoints
    both "loaded" and "current" and performs
    a balanced insert to create a balanced tree
    """
    # get currents
    currentEndpoints = []
    self.__current_endpoints__( self.head, currentEndpoints )
    #print "current: ", currentEndpoints
    # get loaded
    allPoints = self.endpoints.keys()
    #print "loaded: ", allPoints
    allPoints.extend( currentEndpoints )
    allPoints.sort()
    #print "all: ", allPoints

    # reset the tree
    self.__reset__()
    self.__balanced_inserts__( allPoints )

  def __balanced_inserts__(self,numeric_array):
    """
    Takes a numeric array and inserts
    """
    size = len(numeric_array)
    if size==0:
      return
    else:
      mid = size / 2
      # split array
      left = numeric_array[0:mid]
      right = numeric_array[mid+1:]
      #print left
      #print right

      self.insert( numeric_array[mid] )
      self.__balanced_inserts__(left)
      self.__balanced_inserts__(right)


  def __current_endpoints__(self,node,array):
    """
    Takes a node reference and array
    Performs an in-order traversal, appending node
    values to the array
    """
    if ( node==None or node.is_leaf() ):
      return
    self.__current_endpoints__(node.left,array)
    array.append( node.value )
    self.__current_endpoints__(node.right,array)

  def query_endpoint(self,endpoint):
    """
    Return a list of objects containing an endpoint
    """
    val = {}
    self.__accumulate__(self.head,endpoint,val)
    return val.keys()

  def __accumulate__(self,node,endpoint,accumulator):
    """
    Traverse the tree collecting references
    NOTE: this is still buggy
    """
    # base case
    if (node.is_leaf()):
      for obj in node.objects:
        accumulator[obj] = True
      return
    # accumulate
    if endpoint==node.value:
      for obj in node.objects:
        accumulator[obj] = True
    # recurse
    if endpoint <= node.value:
      self.__accumulate__(node.left,endpoint,accumulator)
    if endpoint >= node.value:
      self.__accumulate__(node.right,endpoint,accumulator)

  def __span__(self,start,end,node):
    """
    Check if a node is inside the interval
    """
    return start <= node.value <= end

  def query_interval(self,start,end):
    """
    Return a list of objects in an interval
    """
    # NOTE: incomplete
    val = []
    return val

def testsuite():
  print "testing interval tree"

if __name__ == "__main__":
  testsuite()

