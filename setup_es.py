from elasticsearch import Elasticsearch
from requests.auth import HTTPBasicAuth

es_host = 'f58e3387dfa2495289b5b5edec2d6e3c.us-west-1.aws.found.io'
es_host = '8b9c0d0c1d8d421e8a98f56bc8cc7578.us-west-1.aws.found.io'
es_host = '7fcc129ce17b4396b0a53c1e80dad9cf.us-west-1.aws.found.io'
user = 'elastic'
passwd = 'l9r7WY8yUGHOWd7Mz0LeW5o6'
passwd = '7cKIJ33GofvFxJHCMViBz2Oc'
passwd = 'skQu1NTHlkCmvEkLvcbCV1eI'
port = '9243'

es = Elasticsearch(
    [es_host],
    http_auth=(user, passwd),
    scheme="https",
    port=int(port),
    timeout=40
)
SITE_NAME = 'https://' + es_host + ':' + port + '/'
es_auth = HTTPBasicAuth(user, passwd)
