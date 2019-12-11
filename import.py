from elasticsearch import Elasticsearch
from elasticsearch import helpers
import fileinput
import pickle
from utils import id_gen


def parse_line(l, data_parser, header):
    line = l.rstrip().split("\t")
    d = {}
    for idx in range(len(header)):
        if line[idx] == ".":
            continue
        k = header[idx]
        d[k] = data_parser.get(k, str)(line[idx])
    return d



data = open('doc_type.pkl', 'rb')
dtype = pickle.load(data)
data_parser = {}
for k in dtype:
    data_parser[k] = eval(dtype[k])
data_parser['chr'] = str
data_parser['GWAS_catalog_pubmedid'] = str
data_parser['GRASP_PMID'] = str

es = Elasticsearch(hosts=["127.0.0.1:9200"], timeout=5000)

error = open("error.log", "w")
header = ''
count = 0
da_list = []
for i in fileinput.input():
    count += 1
    if not header:
        header = i.rstrip().split("\t")
        continue
    data = {
        "_index": "vs-index",
        "_id": id_gen(i),
        "_source": parse_line(i, data_parser, header) }
    try:
        data = {
        "_index": "vs-index",
        "_id": id_gen(i),
        "_source": parse_line(i, data_parser, header)
    }
        da_list.append(data)
    except:
        print("error on:",data)
    if count % 10000 == 0:
        helpers.bulk(es, da_list, chunk_size=5000, raise_on_error=True)
        da_list = []
        print("import {}".format(count))
helpers.bulk(es, da_list, chunk_size=5000, raise_on_error=True)
