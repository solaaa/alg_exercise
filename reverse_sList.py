class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def init_list(arr):
    head = None
    q = None
    if arr == []:
        return head
    for i in range(len(arr)):
        p = Node(arr[i])
        if i == 0:
            head = p
            q = head
        else:
            q.next = p
            q = q.next
    return head

def dfs(head):
    p = head
    while p:
        print(p.val)
        p = p.next
def reverse(h):
    p = h.next
    q = None
    while p:
        h.next = q
        q = h
        h = p
        p = p.next
    h.next = q
    return h


h = init_list([1,2,3,5,6])
dfs(h)
h = reverse(h)
dfs(h)
        