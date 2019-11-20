. host.sh

curl -XPOST "$host/vs-index/_search?pretty" \
-H 'Content-Type: application/json' \
-d '{
"query": { 
    "bool": {
	"filter": [
		{"term": {"chr":"2"}},
		{"range" : { "pos" : { "gte" : 10, "lte" : 20000 } }}]
    }
  },
"from" : 0, "size" : 20
}'
