. host.sh

curl -XPOST "$host/vs-index/_search?pretty" \
-H 'Content-Type: application/json' \
-d '{
"_source": ["ANNOVAR_ensembl_GO_biological_process_complete_list_id","pos"],
"query": { 
    "bool": {
	"filter": [
		{"term": {"chr":"2"}},
		{"range" : { "pos" : { "gte" : 10, "lte" : 20000 } }}]
}}}'
