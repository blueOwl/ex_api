# AnnoQ API based on Elasticsearch

Currently this API is under domain `http://annoq.org:3404/` and index name (\<idx\>) is `vs-index`.

## Annotation tree structure

* endpoint 
`/<idx>/anno_tree`

## Gene mapping
* endpoint `/gene`
* parameters `?gene=`

### response

```
{
  "gene_info": {
    "contig": "10", 
    "end": 254634, 
    "gene_id": "HUMAN|HGNC=16966|UniProtKB=Q15326", 
    "start": 135484
  }
}
```

## Download request

Send json request with query body. See documents for elasticsearch.

endpoint `/total_res`

### response

`{"url":url}`

## vcf file search

endpoint `/<idx>/ids`

No pages. Only return first 50 hits. Contains url for download.

Request body:

```
{
  "_source":["pos", "ref"],
  "ids":["18:10636A>C", "18:10644C>G", "18:10667C>T", "18:10719C>G"]
}
```

IDs should in format of `"contig":pos"Ref">"Alt"`

### response



```
{
  "hits": {
    "hits": [
      {
        "pos": 10636,
        "ref": "A"
      },
      {
        "pos": 10644,
        "ref": "C"
      },
      {
        "pos": 10667,
        "ref": "C"
      },
      {
        "pos": 10719,
        "ref": "C"
      }
    ]
  },
  "url": "/download/tmp/74ea9e11-7f47-4c61-a5e6-fe2c54425b71.txt"
}
```

## Other Queries
Data scheme `/<idx>/_mapping` .

Same as elasticsearch. 