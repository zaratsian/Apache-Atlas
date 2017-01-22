

import requests
import re
import json


def atlas_get_status(atlas_host, atlas_port, atlas_user, atlas_pw):
    url  = 'http://' + str(atlas_host) + ':' + str(atlas_port) + '/api/atlas/admin/status'
    auth = (atlas_user,atlas_pw)
    r = requests.get(url,auth=auth)
    if r.status_code == 200:
        return r.content
    else:
        return '[ ERROR ] Status Code: ' + str(r.status_code) + ' --- ' + r.content

get_atlas_status('localhost','21000','admin','admin')



def atlas_search(atlas_host, atlas_port, atlas_user, atlas_pw, query):
    url  = 'http://' + str(atlas_host) + ':' + str(atlas_port) + '/api/atlas/discovery/search?query=' + str(query)
    auth = (atlas_user,atlas_pw)
    r = requests.get(url,auth=auth)
    if r.status_code == 200:
        return r.content
    else:
        return '[ ERROR ] Status Code: ' + str(r.status_code) + ' --- ' + r.content

assets = json.loads(atlas_search('localhost','21000','admin','admin','*table1'))
list_assets = [asset for asset in assets['results']]



'''
/admin/session
/admin/stack
/admin/status
/admin/version

/lineage/hive/table/{tableName}/inputs/graph
/lineage/hive/table/{tableName}/outputs/graph
/lineage/hive/table/{tableName}/schema

/entities
/entities/{guid}
/entities/{guid}/audit
/entities/{guid}/traits
/entities/{guid}/traits/{traitName}

/lineage/{guid}/inputs/graph
/lineage/{guid}/outputs/graph
/lineage/{guid}/schema

/discovery/search
/discovery/search/dsl
/discovery/search/fulltext
/discovery/search/gremlin

/v1/taxonomies
/v1/taxonomies/{taxonomyName}
/v1/taxonomies/{taxonomyName}/terms
/v1/taxonomies/{taxonomyName}/terms/{rootTerm}/{remainder}
/v1/taxonomies/{taxonomyName}/terms/{termName}
/v1/taxonomies/{taxonomyName}/terms/{termName}/{remainder}

/types
/types/{typeName}
'''


#ZEND
