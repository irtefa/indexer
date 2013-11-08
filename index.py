import requests
import time
import json
from parse_rest.connection import register
from parse_rest.datatypes import Object

#all the API keys
parse_app_id = '#'
parse_master_key = '#'
rest_api_key = '#'

#required host names
elasticsearch_host = 'http://ec2-54-237-2-191.compute-1.amazonaws.com:9200/metadata/'
headers = {'content-type': 'application/json'}

#before we index, we flush the current index
r = requests.delete(elasticsearch_host)
print r.text

class Meta(Object):
    pass

register(parse_app_id, rest_api_key)

#get all parse metadata
all_metadata = Meta.Query.all()

for metadata in all_metadata:
    elastic_object = {
    'name': metadata.name.lower(),
    'artist': metadata.artist,
    'album': metadata.album.lower(),
    'genre': metadata.genre,
    'objectId': metadata.objectId,
    'time': metadata.time,
    'artwork': metadata.cover
    }
    r = requests.post(elasticsearch_host + 'meta/', data=json.dumps(elastic_object), headers=headers)
    print r.text
    time.sleep(2)

print "All parse metadata has been indexed"
