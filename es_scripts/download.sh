. host.sh

curl -XPOST "$host/total_res" \
-H 'Content-Type: application/json' \
-d '{
"query": { 
    "bool": {
	"filter": [
		{"term": {"chr":"2"}},
		{"range" : { "pos" : { "gte" : 10, "lte" : 20000 } }}]
}}}'|jq -r '.url'|xargs -I{} wget -q -O- $host{}
