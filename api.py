from elasticsearch import Elasticsearch
from flask import Flask,request,redirect,Response,jsonify
import requests

es = Elasticsearch(hosts=["127.0.0.1:9200"], timeout=5000)
app = Flask(__name__)
SITE_NAME = 'http://localhost:9200/'

def get_mapping(idx='vs-index', tp='variant'):
    all_mapping = es.indices.get_mapping()
    mapping = all_mapping[idx]['mappings'][tp]['properties']
    fields = [i for i in mapping]
    return fields

def structure_mapping(field_list):
    res = {"ANNOVAR":[], 'VEP':[], 'SnpEff':[], 'others':[]}
    for i in field_list:
        for k in res:
            if k in i: 
                res[k].append(i)
                continue
            res['others'].append(i)
    return res

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
    app.run(debug = False,port=9888)

