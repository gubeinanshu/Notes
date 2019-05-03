```
post_data = {'key1': 'value1'}
body = urllib.urlencode(post_data)
http_client = tornado.httpclient.AsyncHTTPClient()
http_client.fetch("url", method='POST', body=body)
```