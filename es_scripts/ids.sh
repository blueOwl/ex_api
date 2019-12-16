. host.sh

curl -XPOST "$host/vs-index/ids" \
-H 'Content-Type: application/json' \
-d '{
  "_source":["pos", "ref"],
  "ids":["18:10636A>C", "18:10644C>G", "18:10667C>T", "18:10719C>G"]
}'

curl -XPOST "$host/vs-index/ids" \
-H 'Content-Type: application/json' \
-d '{
  "_source":["pos", "ref"],
  "ids":["18:10636A>C", "18:10644C>G", "18:10667C>T", "18:10719C>G"]
}'|jq -r '.url'|xargs -I{} wget -q -O- $host{}
