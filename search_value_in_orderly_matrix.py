def search(mat, k):
    i = 0
    j = len(mat[i]) - 1
    while i < len(mat) and j>=0:
        if mat[i][j] > k:
            j -= 1
        elif mat[i][j] < k:
            i += 1
        else:
            return True
    return False
print(search(
[[1,2,3],
 [4,5,6],
 [7,8,9]],
0
))
