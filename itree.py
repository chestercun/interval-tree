__all__ = ["IntervalTree"]

# binary tree node
class Node:
  """
  Helper class for IntervalTree implementation
  """
  def __init__(self,value):
    """
    Start a node with a numeric value
    """
    # elemental endpoint
    self.value = value
    # spanning
    self.objects = {}
    # greater-than & less-than
    self.right_objects = {}
    self.left_objects = {}
    # node references
    self.parent = None
    self.left = None
    self.right = None

  def push(self,obj):
    """
    Add an object reference to the "objects" list
    """
    hashref = self.objects
    if not hashref.has_key(obj):
      hashref[obj] = True

  def push_left(self,obj):
    """
    Add an object reference to the "objects" list
    """
    hashref = self.left_objects
    if not hashref.has_key(obj):
      hashref[obj] = True

  def push_right(self,obj):
    """
    Add an object reference to the "objects" list
    """
    hashref = self.right_objects
    if not hashref.has_key(obj):
      hashref[obj] = True

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
    # NOTE: add the object reference
    # to the proper location
    # self.__match__( self.head, obj )

  def __match__(self,node,obj):
    """
    Helper function for add
    This traverses the interval tree
    and adds the obj-ref to the appropriate nodes
    """
    if (node==None):
      return
    # NOTE: unfinished

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
    if value < node.value:
      if node.left==None:
        node.left = Node(value)
        node.left.parent = node
      else:
        self.__insert__(node.left,value)
    elif value > node.value:
      if node.right==None:
        node.right = Node(value)
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
    if (node==None):
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

  def __span__(self,start,end,node):
    return start <= node.value <= end

  def __current_endpoints__(self,node,array):
    """
    Takes a node reference and array
    Performs an in-order traversal, appending node
    values to the array
    """
    if (node==None):
      return
    self.__current_endpoints__(node.left,array)
    array.append( node.value )
    self.__current_endpoints__(node.right,array)

  def query_endpoint(self,endpoint):
    """
    Return a list of objects containing an endpoint
    """
    # NOTE: incomplete
    val = []
    return val

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

