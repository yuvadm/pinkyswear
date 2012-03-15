from urllib3.connectionpool import connection_from_url

url = 'https://twitter.com'

http_pool = connection_from_url(url, strict=False)
print http_pool.__dict__


r = http_pool.urlopen('GET', url)
# print r.data
# print r.data
