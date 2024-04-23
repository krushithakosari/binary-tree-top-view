class Node:
    def __init__(self,data):
        self.lc=None
        self.rc=None
        self.data=data
        self.hd=0
def topview(root):
    m={}
    q=[root]
    while q:
        node=q.pop(0)
        if node.hd not in m:
            m[node.hd]=node.data
        if node.lc:
            node.lc.hd=node.hd-1
            q.append(node.lc)
        if node.rc:
            node.rc.hd=node.hd+1
            q.append(node.rc)
    print("topview")
    for hd in sorted(m):
        print(m[hd],end=",")
root=Node(1)
root.lc=Node(2)
root.rc=Node(3)
root.lc.lc=Node(4)
root.lc.rc=Node(5)
root.rc.lc=Node(6)
root.rc.rc=Node(7)
root.lc.rc.lc=Node(8)
root.rc.lc.rc=Node(9)
topview(root)

