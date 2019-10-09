import tree
import binary_tree

x=tree.tree(1000)
y=tree.tree(2000)
z=tree.tree(3000)
x.AddSuccessor(y)
x.AddSuccessor(z)
w=tree.tree(5)
z.AddSuccessor(w)
ans=x.Get_LevelOrder()
print "Level order Tree"+str(ans)
bin=x.ConvertToBinaryTree()
bin1=bin.Get_LevelOrder()
print bin1


a=binary_tree.binary_tree(1)
a.AddLeft(2)
a.AddRight(3)
a.AddLeft(4)
a.AddRight(5)

ans2 = a.Get_LevelOrder()
print ans2

ans3=a.ConvertToTree()
final=ans3[1].Get_LevelOrder()
print final
