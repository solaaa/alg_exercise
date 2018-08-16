# leetcode 49
# input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# output: 
#[
  #["ate","eat","tea"],
  #["nat","tan"],
  #["bat"]
#]
def my_hash(string):
    string = list(string)
    string = sorted(string)
    return tuple(string)

def groupAnagrams(strs):
    table = {}
    for string in strs:
        key = my_hash(string)
        if key in table:
            table[key].append(string)
        else:
            table[key] = []
            table[key].append(string)
    res = []
    for key in table:
        res.append(table[key])
    return res

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))