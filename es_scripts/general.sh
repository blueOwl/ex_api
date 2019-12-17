. host.sh

curl -XPOST "$host/vs-index/_search?pretty" \
-H 'Content-Type: application/json' \
-d '
{
"_source":["chr","pos","ref","alt","rs_dbSNP151","ANNOVAR_ensembl_Effect"],
"query":
	{"multi_match":
		{
		"query":"upstream",
		"fields": ["chr","pos","ref","alt","rs_dbSNP151","ANNOVAR_ensembl_Effect"]
		}
	},
"from":0,
"size":50}
'
