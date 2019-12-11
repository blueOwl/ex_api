from elasticsearch import Elasticsearch
from elasticsearch import helpers
import fileinput
import pickle
from utils import id_gen
import json

es = Elasticsearch(
    ['f58e3387dfa2495289b5b5edec2d6e3c.us-west-1.aws.found.io'],
    http_auth=('elastic', 'l9r7WY8yUGHOWd7Mz0LeW5o6'),
    scheme="https",
    port=9243,
    timeout=20
)
es = Elasticsearch(hosts=["127.0.0.1:9200"], timeout=5000)
#delete old one
es.indices.delete(index='vs-index', ignore=[404])
#create and load mapping
es.indices.create(index='vs-index')
mapping = json.load(open("./es_scripts/vs_index_mapping.json"))
es.indices.put_mapping(index = 'vs-index', body=mapping )
