class Annotation_tree_node:
	def __init__(self, nid=0, parent_id=0, info='', name="root", leaf=False):
		self.id = nid
		self.parent_id = parent_id
		self.info = info
		self.name = name
		self.leaf = leaf
	def get_dic(self):
		return {'id' : self.id,
			'name' : self.name,
			'detail' : self.info,
			'parent_id' : self.parent_id,
                        'leaf':self.leaf} 

def dict_to_tree(dic):
    uid = 1
    root = Annotation_tree_node(parent_id=None)
    tree_dic = {'root':root}
    for k in dic:
        node = Annotation_tree_node(nid=uid, name=k, info='', parent_id=root.id)
        tree_dic[k] = node
        uid += 1
        for anno_name in dic[k]:
            node = Annotation_tree_node(nid=uid, name=anno_name, info=anno_name, parent_id=tree_dic[k].id, leaf=True)
            tree_dic[anno_name] = node
            uid += 1
    print(set([tree_dic[k].parent_id for k in tree_dic]))
    return tree_dic


