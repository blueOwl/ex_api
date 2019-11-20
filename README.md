# Flask wrap for es based annotation search API

## bash scripts demo:

* show.sh : show first 10 docs
* region.sh : region query
* region_fields.sh : region query with specific fields
* region_size.sh : region query with size and from for pagination
* structure.sh : show fields tree structure

## response 

```
{
  "took": 6,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 264,
      "relation": "eq"
    },
    "max_score": 0,
    "hits": [
      {...},
      {...}
    ]
  }
}
```

* response.hits.total.value is total result number
* response.hits.hits is data
