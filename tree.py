from setup_es import *

cats = {
    'Basic Info':['chr', 'pos', 'ref', 'alt', 'rs_dbSNP151'],
    'IMAGE Enhancer Linked Functional Annotations':[],
    'ANNOVAR':[], 
    'AnnoQ Functional Annotations':[],
    'VEP':[],
    'SnpEff':[], 
    "allele frequencies":{
        "1000Gp3":[],
        "ESP6500":[],
        "ExAC":[],
        "UK10K":[],
        "gnomAD":[]
    },
    "disease related databases":{
        "clinvar":[],
        "COSMIC":[],
        "GWAS_catalog":[], #GWAS
        "GRASP2":[]        #GRAP
        
    },
    "others":[]
    
}

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
    def __repr__(self):
        return str(self.id) + ":" + self.name + ' parent_' + str(self.parent_id)

def start_with(pre, s):
    l = len(pre)
    return s[:l] == pre


def make_mapping_dic_tree(fields):
    for i in fields:
        added = False
        if i in cats['Basic Info']:
            continue
        if start_with('enhancer', i):
            cats['IMAGE Enhancer Linked Functional Annotations'].append(i)
            continue
        if start_with('flank', i):    
            cats['AnnoQ Functional Annotations'].append(i)
            continue
        for pre in ['ANNOVAR', 'VEP', 'SnpEff']:
            if start_with(pre, i):
                cats[pre].append(i)
                added = True
                break
        if added:continue
        for pre in ["1000Gp3", "ESP6500", "ExAC", "UK10K", "gnomAD"]:
            if start_with(pre, i):
                cats["allele frequencies"][pre].append(i)
                added = True
                break
        if added:continue
        for pre in ["clinvar", "COSMIC"]:
            if start_with(pre, i):
                cats["disease related databases"][pre].append(i)
                added = True
                break
        if added:continue
        if start_with('GWAS', i):
            cats["disease related databases"]['GWAS_catalog'].append(i)
            continue
        if start_with('GRASP', i):
            cats["disease related databases"]['GRASP2'].append(i)
            continue
        cats["others"].append(i)
    return cats

def dic_to_tree(dic, parent_id, node_li, info):
    uid = parent_id + 1
    for k in dic:
        node = Annotation_tree_node(nid=uid, name=k, info='', parent_id=parent_id)
        node_li .append(node)
        ouid = uid
        uid = uid + 1
        if type(dic[k]) == list:
            for name in dic[k]:
                node = Annotation_tree_node(nid=uid, name=name, info=info.get(name, ''), parent_id=ouid, leaf=True)
                #if info.get(name): print("#",name, info.get(name))
                node_li .append(node)
                uid = uid + 1
            
            #make a node and insert
            #make node for all in list and insert
        else:
            #make a node and insert
            #print(k)
            uid = dic_to_tree(dic[k], ouid, node_li, info)
    return uid

def init_tree_list():
    f = open('data/others/annotated.description.reformat.txt')
    info = {}
    for i in f:
        l = i.rstrip().split("\t")
        info[l[0]] = '\n'.join(l[1:])
    parent_id = 0
    root = Annotation_tree_node(parent_id=None)
    node_li = [root]
    all_mapping = es.indices.get_mapping()
    mapping = all_mapping['vs-index']['mappings']['properties']
    fields = [i for i in mapping]
    dic_fields = make_mapping_dic_tree(fields)
    dic_to_tree(dic_fields, parent_id, node_li, info)
    return list(i.get_dic() for i in node_li)
