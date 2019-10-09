from graph import *

x=graph()

x.addVertex(1)
x.addVertex(1)
x.addVertex(1)
x.addVertex(1)
x.addVertex(1)
x.addVertex(1)
x.addVertex(1)
x.addVertex(1)
#x.printEdges()
x.addEdge(0,1,False,1)
x.addEdge(0,2,False,1)
x.addEdge(0,3,False,1)
x.addEdge(1,2,False,2)
x.addEdge(1,4,False,2)
x.addEdge(2,3,True,3)
x.addEdge(3,4,True,4)
#x.addEdge(4,5,True,5)

x.addEdge(5,6,True,1)
x.addEdge(5,7,True,1)


#x.printEdges()
print "Depth from None"
print x.traverse(None,False)

print "Depth from 0"
print x.traverse(0,False)

print "Breadth from 0"
print x.traverse(0,True)
print "Breadth; start=None"
print x.traverse(None,True)

print "connect from 3,4"
print x.connectivity(3,4)

print "pathway from 0,4"
print x.pathway(0,4)

print "pathway from 5,6"
print x.pathway(5,6)

print "breadth from 5"
print x.traverse(5,True)
