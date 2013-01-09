import sys
from itree import IntervalTree

def debug2(node):
  print "%.01f %r %r" % (node.value, node.left, node.right)

def debug3(node):
  print "%.01f obj: %r left: %r right: %r" % (node.value, node.objects, node.left.objects, node.right.objects)

class StringWrapper:
  def __init__(self,name):
    self.name = name

def main():
  if (len(sys.argv)>1):
    filename = sys.argv[1]
  else:
    filename = "composers.txt"

  infile = open(filename,'r')
  data = []


  for line in infile:
    (name,start,end) = line.strip().split(' ')
    print "%s, %s, %s" % (name,start,end)
    data.append((int(start),int(end),name))

  i = IntervalTree()

  # load pts
  for tup in data:
    i.load(tup[0])
    i.load(tup[1])
  # don't forget to "unload"
  i.unload()

  """
  i.insert(1874)
  i.insert(1779)
  i.insert(1672)
  i.insert(1585)
  i.insert(1756)
  i.insert(1828)
  i.insert(1791)
  i.insert(1843)
  i.insert(1951)
  i.insert(1907)
  i.insert(1888)
  i.insert(1971)
  """

  for tup in data:
    s = StringWrapper(tup[2])
    #i.add(tup[0],tup[1],s)
    i.add(tup[0],tup[1],tup[2])

  i.inorder( debug2 )
  i.inorder( debug3 )

  # test endpoint
  for ep in [1400,1828,1830,1907,1908,1780]:
    #print "date: %d" % ep, ["%s" % obj for obj.name in i.query_endpoint( ep )]
    print "date: %d" % ep, ["%s" % obj for obj in i.query_endpoint( ep )]

  # collect objects list
  #objList = i.query( 1.5, 20.2)

if __name__ == "__main__":
  main()


