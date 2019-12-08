from elasticsearch import Elasticsearch
from flask import Flask,request,redirect,Response,jsonify
from flask_cors import CORS
import requests
from tree import *

es = Elasticsearch(hosts=["127.0.0.1:9200"], timeout=5000)
app = Flask(__name__)
CORS(app)

SITE_NAME = 'http://localhost:9200/'

def get_mapping(idx='vs-index'):
    all_mapping = es.indices.get_mapping()
    mapping = all_mapping[idx]['mappings']['properties']
    fields = [i for i in mapping]
    return fields

def structure_mapping(field_list):
    res = {"ANNOVAR":[], 'VEP':[], 'SnpEff':[], 'others':[]}
    for i in field_list:
        check = False
        for k in res:
            if k in i: 
                res[k].append(i)
                check = True
                continue
        if not check:
            res['others'].append(i)
    return res

@app.route('/<idx>/anno_tree')
def get_anno_tree(idx):
    stct = structure_mapping(get_mapping(idx=idx))
    tree_dic = dict_to_tree(stct)
    return jsonify({"header_tree_array":[tree_dic[i].get_dic() for i in sorted(tree_dic.keys())]})


@app.route('/<idx>/structure')
def show_idx_str(idx):
    stct = structure_mapping(get_mapping(idx=idx))
    return jsonify(stct)

@app.route('/<path:path>',methods=['GET','POST',"DELETE"])
def proxy(path):
    global SITE_NAME
    if request.method=='GET':
        resp = requests.get(f'{SITE_NAME}{path}')
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method=='POST':
        resp = requests.post(f'{SITE_NAME}{path}',json=request.get_json())
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method=='DELETE':
        resp = requests.delete(f'{SITE_NAME}{path}').content
        response = Response(resp.content, resp.status_code, headers)
        return response
if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug = False,port=3404)

