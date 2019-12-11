import requests

host = 'http://panthertest3.med.usc.edu:8083'
gene_mapping_api = '/services/oai/pantherdb/geneinfo'
params = {"geneInputList":"ABCA1", "organism":9606}

def load_chromosomal_location(dfile='./data/others/Homo_sapiens.chromosomal_location_20180114'):
    dic = {}
    for i in open(dfile):
        line = i.rstrip().split('\t')
        dic[line[0]] = (line[1], int(line[2]), int(line[3]))
    return dic
    
def map_gene(k):
    params["geneInputList"] = k
    try:
        r = requests.get(url = host + gene_mapping_api, params = params, timeout=5)
        data = r.json()
        return data['search']['mapped_genes']['gene']["accession"]
    except:
        return ''

def get_pos_from_gene_id(gid, chromosomal_location_dic):
    return chromosomal_location_dic.get(gid ,None)

chromosomal_location_dic = load_chromosomal_location('./data/others/Homo_sapiens.chromosomal_location_20180114')

#print(get_pos_from_gene_id(map_gene("ABCA1"), chromosomal_location_dic))
