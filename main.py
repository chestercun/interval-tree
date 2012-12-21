import sys
from itree import IntervalTree

def debug(obj):
  print obj.value

def drop(obj):
  print "%d %s %s" % (obj.value, obj.left, obj.right)

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
  i.insert(5)
  i.insert(3)
  i.insert(4)
  i.insert(1)
  i.insert(8)
  i.insert(6)
  i.insert(10)
  i.inorder(debug)
  i.inorder(drop)


if __name__ == "__main__":
  main()


