import sys
from itree import IntervalTree

def debug(node):
  print "%.01f" % node.value

def debug2(node):
  #print "%d %s %s" % (node.value, node.left, node.right)
  print "%.01f %s %s" % (node.value, node.left, node.right)

def debug3(node):
  print "%.01f %r" % (node.value, node.objects)

def main():
  if (len(sys.argv)>1):
    filename = sys.argv[1]
  else:
    filename = "test_data.txt"

  infile = open(filename,'r')

  for line in infile:
    (name,start,end) = line.strip().split(' ')
    print "%s, %s, %s" % (name,start,end)

  i = IntervalTree()

# 1,3,4,5,6,8,10
# use a mix of insert and load
# to test the total functionality
  """
           5
        3     8
      1  4   6  10
  """
  i.insert(6)
  i.insert(3)
  i.insert(3)
  i.insert(4)
  i.load(1)
  i.load(5)
  i.load(8)
  i.load(10)

  i.unload()
  print ""

  i.inorder( debug2 )

  # time to test insertions
  i.add(3,8,"yohann")
  print ""
  i.inorder( debug2 )
  i.inorder( debug3 )

  # collect objects list
  #objList = i.query( 1.5, 20.2)

if __name__ == "__main__":
  main()


