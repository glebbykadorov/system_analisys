import json

json_tree_file = open('tree.json')
tree_json = json.load(json_tree_file)
    
def dict_to_tree_req(tree_json, tree ,prev ,current): 
    for node in tree_json:
        print(node)
        tree[0].append(node)
        tree[1].append(prev)
        current[0] += 1
        if tree_json[node] != - 1:
            dict_to_tree_req(tree_json[node],tree,current[0] - 1,current)

class tree:
    def __init__(self,labels,parents):
        self.labels = labels
        self.parents = parents
    def __str__(self):
        return str(self.labels) + '\n' + str(self.parents)

def dict_to_tree(tree_json):
    data = ([],[])
    prev = -1
    current = [0]
    dict_to_tree_req(tree_json, data ,prev, current)
    return tree(data[0],data[1])

print(dict_to_tree(tree_json))

