class Annotation_tree_node:
	def __init__(self, nid=0, parent_id=0, info='', name="root"):
		self.id = nid
		self.parent_id = parent_id
		self.info = info
		self.name = name
	def get_dic(self):
		return {'id' : self.id,
			'name' : self.name,
			'detail' : self.info,
			'parent_id' : self.parent_id} 

def dict_to_tree(dic):
    root = Annotation_tree_node(parent_id=None)
    tree_dic = {'root':root}
    for k in dic:
        node = Annotation_tree_node(nid=k, name=k, info='', parent_id=root.id)
        tree_dic[k] = node
        for anno_name in dic[k]:
            node = Annotation_tree_node(nid=anno_name, name=anno_name, info=anno_name, parent_id=k)
            tree_dic[anno_name] = node
    return tree_dic


