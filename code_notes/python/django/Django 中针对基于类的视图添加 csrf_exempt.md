[Django类视图笔记整理](https://www.jianshu.com/p/3ec42274013d)

# 方法一：在类的 dispatch 方法上使用 @csrf_exempt
```python
from django.views.decorators.csrf import csrf_exempt

class MyView(View):

    def get(self, request):
        return HttpResponse("hi")

    def post(self, request):
        return HttpResponse("hi")

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(MyView, self).dispatch(*args, **kwargs)
```


# 方法二：在 urls.py 中配置
```python
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
import views

urlpatterns = [
    url(r'^myview/$', csrf_exempt(views.MyView.as_view()), name='myview'),
]
```