直接返回图片文件流的方式

```python
#file: views.py

def my_image(request,news_id):
    d = path.dirname(__file__)
    #parent_path = path.dirname(d)
    print("d="+str(d))
    imagepath = path.join(d,"static/show/wordimage/"+str(news_id)+".png")
    print("imagepath="+str(imagepath))
    image_data = open(imagepath,"rb").read()
    return HttpResponse(image_data,content_type="image/png") #注意旧版的资料使用mimetype,现在已经改为content_type

```


```python
#file: 
urlpatterns = [
    url(r'^index/$', views.index,name="index"),
    url(r'^search/$', views.search,name="search"),
    url(r'^science/(?P<news_id>.+)/$', views.science,name="science"),
    url(r'^image/(?P<news_id>.+)/$',views.my_image,name="image"),
]

```

```python
#file: 


<img src="{% url 'show:image' param.id %}" alt="{{param.id}}"/>
```