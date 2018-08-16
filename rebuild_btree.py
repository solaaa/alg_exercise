class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_bt(pre, mid):
    # 1. build root
    root = TreeNode(pre[0])
    
    # 2. find the root.val in mid
    idx = 0
    for i in range(len(mid)):
        if root.val == mid[i]:
            idx = i
            break
    L_len = idx
    R_len = len(mid) - idx - 1
    
    # 3. recursion
    if L_len:
        root.left = build_bt(pre[1:L_len+1], mid[:L_len])
    if R_len:
        root.right = build_bt(pre[L_len+1:], mid[L_len+1:])
    return root

def pre(r):
    if r:
        print(r.val)
    else:
        return
    pre(r.left)
    pre(r.right)
    
tree = build_bt([1,2,3,4,5,6,7,8,9],[4,3,2,5,6,1,8,7,9])
pre(tree)