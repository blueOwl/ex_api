from elasticsearch import Elasticsearch
from flask import Flask,request,redirect,Response,jsonify, send_from_directory, abort
from flask_cors import CORS
from tree import *
from gene_pos import *
from download import *
import uuid
import requests
import config
from setup_es import *
from utils import *

#SITE_NAME = 'http://localhost:9200/'
#es = Elasticsearch(hosts=["127.0.0.1:9200"], timeout=5000)
app = Flask(__name__)
CORS(app)

def get_mapping(idx='vs-index'):
    all_mapping = es.indices.get_mapping()
    mapping = all_mapping[idx]['mappings']['properties']
    fields = [i for i in mapping]
    return fields
'''
'''
@app.route('/<idx>/anno_tree')
def get_anno_tree(idx):
    #stct = structure_mapping(get_mapping(idx=idx))
    #tree_dic = dict_to_tree(stct)
    return jsonify({"header_tree_array": init_tree_list()}) #[tree_dic[i].get_dic() for i in sorted(tree_dic.keys())]})


@app.route('/<idx>/structure')
def show_idx_str(idx):
    stct = get_mapping(idx=idx)
    return jsonify(stct)

'''
@app.route('/<idx>/vcf', methods=['POST'])
def vcf_intersect(idx):
    req_json = request.get_json()
    ids = [vcf_to_id(i.encode('utf8')) for i in req_json['params']['uploadList']['ids'].split('\n') if i.encode("utf-8")[:1] != '#']
'''

@app.route('/gene')
def search_gene_pos():
    gene_name = request.args.get('gene')
    gene_id = map_gene(gene_name)
    gene_pos = get_pos_from_gene_id(gene_id, chromosomal_location_dic)
    gene_info = {'gene_id':gene_id, 'contig': '', 'start':0, 'end':0}
    if gene_pos:
        gene_info['contig'] = gene_pos[0]
        gene_info['start'] = gene_pos[1]
        gene_info['end'] = gene_pos[2]
    return jsonify({'gene_info':gene_info})

@app.route('/download/<folder>/<name>', methods=['GET'])
def download_file(folder, name):
    if not folder in config.DOWNLOAD_DIR: 
        abort(400)
    return send_from_directory(folder, name, as_attachment=True)

@app.route('/total_res', methods=['GET','POST'])
def get_download_url():
    body = request.json
    query = {"query": body.get('query')}
    if body.get('_source'):
        query['_source'] = body['_source']
    filename = str(uuid.uuid4()) + '.txt'
    f = open(config.DOWNLOAD_DIR + '/' + filename, 'w')
    query_to_file(es, query, f.write, f.write)
    return jsonify({"url": "/download/" + 'tmp/' + filename})

@app.route('/<idx>/ids', methods=['POST'])
def mget(idx):
    body = request.json
    ids = body.get('ids')
    source = body.get('_source')
    filename = str(uuid.uuid4()) + '.txt'
    f = open(config.DOWNLOAD_DIR + '/' + filename, 'w')
    if (not ids) or (not source):
        abort(404)
    hits = {"hits":query_vcf(es, {"ids":ids, "_source":source}, f.write)}
    #query to file and return first page
    return jsonify({"hits":hits, "url": "/download/" + 'tmp/' + filename})

@app.route('/<path:path>',methods=['GET','POST'])
def proxy(path):
    global SITE_NAME
    #print(request.get_json())
    if request.method=='GET':
        resp = requests.get(f'{SITE_NAME}{path}', auth=es_auth)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method=='POST':
        resp = requests.post(f'{SITE_NAME}{path}',json=request.get_json(), auth=es_auth)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug = True,port=3404)

