def query_to_file(es, body, output, error_output, index='vs-index'):

    col_names = body.get('_source',None)
    if not col_names:
        col_names = es.indices.get_mapping()[index]['mappings']['properties'].keys()
    output('\t'.join(col_names) + '\n')
    resp = es.search(
      index = index,
      scroll = '2m',
      size = 2000,
      body = body
    )
    old_scroll_id = resp['_scroll_id']

    while len(resp['hits']['hits']):
                for doc in resp['hits']['hits']:
                    li = [str(doc['_source'].get(k, '.')) for k in col_names]
                    output('\t'.join(li) + "\n")
                resp = es.scroll(
                    scroll_id = old_scroll_id,
                    scroll = '2s' # length of time to keep search context
                )
                # check if there's a new scroll ID
                if old_scroll_id != resp['_scroll_id']:
                    error_output("download error on:", resp['_scroll_id'])

                old_scroll_id = resp['_scroll_id']
