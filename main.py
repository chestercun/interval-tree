import sys
from itree import IntervalTree

def debug(obj):
  print "%.01f" % obj.value

def debug2(obj):
  #print "%d %s %s" % (obj.value, obj.left, obj.right)
  print "%.01f %s %s" % (obj.value, obj.left, obj.right)

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

  # collect objects list
  #objList = i.query( 1.5, 20.2)

if __name__ == "__main__":
  main()


