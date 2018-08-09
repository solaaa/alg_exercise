import bintree as bt
def build_bintree(series, mode='bfs'):
    '''
    params:
        series: list of int, like: [1, 2, 3, None, 4, 5]
                                           1
                                        2     3
                                      #  4   5  #
                                      
        mode: 'pre', 'mid', 'post' or 'bfs'
    '''
    if series == []:
        return None
    if mode == 'bfs':
        root = bt.TreeNode(val=series[0])
        queue = [root]     
        pt = 1
        while pt < len(series):
            cur = queue.pop()
            if pt < len(series) and series[pt] != None:
                left = bt.TreeNode(series[pt])
                cur.left = left
                queue.insert(0, left)
            pt += 1
            if pt < len(series) and series[pt] != None:
                right = bt.TreeNode(series[pt])
                cur.right = right
                queue.insert(0, right)
            pt += 1
        return root

        
        
        
        
# test   
#s = [1,2,3,None,4,5,6,7,8,9,None,10]
#tree = build_bintree(s)
#queue = [tree]
#while queue != []:
    #val = [node.val for node in queue]
    #print(val)
    #queue = [kid for node in queue for kid in (node.left, node.right) if kid]

