# Elasticsearch based API

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

Send with query body.

endpoint `/total_res`

###response

`{"url":url}`

## vcf file search

### response

endpoint `/<idx>/ids`

No pages. Only return first 50 hits. Contains url for download.

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

## All other queries

Same as elasticsearch. 