import flickr_api
import json
import urllib2
from flickr_api.api import flickr
flickr_api.set_keys(api_key='d04bd43da79177f2d73fe21acc8cf915', api_secret='8971319cb8111932')
a = flickr_api.auth.AuthHandler.load("accessflickr2.txt", "r")
flickr_api.set_auth_handler(a)


eee=flickr_api.api.call_api(
    method='flickr.photos.search',
    tags=('monumentos','valparaiso'),
    tag_mode= 'all',
    extras='date_taken, ownername, url_z, tags',
    page=1,
    format="json",
    per_page=50, )
aaa= eee
############################################### generar el archivo JSON
f= open("C:\Users\MaycollScots\Desktop\Valckr Final\Valckr\Python apps\ monumentos2valpo.json","a")
x = json.dumps(aaa, f)
f.writelines(x)

############################################## se pruebaa imprimiendo (mientras)
print aaa
print x