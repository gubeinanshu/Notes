1. 介绍
```python
#上传的图片文件
pic = request.FILES["picture"]
# pic是 <class 'django.core.files.uploadedfile.InMemoryUploadedFile'> 类型的数据

# 而pillow的Image.open("./xxx.jpg") 则是：

<class 'PIL.JpegImagePlugin.JpegImageFile'> 类型的数据

# 问题是如何把InMemoryUploadedFile转化为PIL类型，并且处理之后再转回InMemoryUploadedFile，并save

```
2. 把InMemoryUploadedFile转化为PIL类型
```python
from PIL import Image

pic = request.FILES["picture"]
im_pic = Image.open(pic)
# 这样就把InMemoryUploadedFile转化为了PIL类型数据，pic是InMemoryUploadedFile，im_pic是PIL类型
```
3.  处理PIL类型的图片数据
```python
w, h = im_pic.size
if w >= h:
    w_start = (w-h)*0.618
    box = (w_start, 0, w_start+h, h)
    region = im_pic.crop(box)
else:
    h_start = (h-w)*0.618
    box = (0, h_start, w, h_start+w)
    region = im_pic.crop(box)

# region就是PIL处理后的正方形了
```
4.  将处理后的PIL类型转化为InMemoryUploadedFile类型
```python
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

// 先保存到磁盘io
pic_io = BytesIO()
region.save(pic_io, im_pic.format)
// 再转化为InMemoryUploadedFile数据
pic_file = InMemoryUploadedFile(
    file=pic_io,
    field_name=None,
    name=pic.name,
    content_type=pic.content_type,
    size=pic.size,
    charset=None
)

#pic_file 就是region转化后的InMemoryUploadedFile了
```
5. 保存InMemoryUploadedFile到数据库
```python
from ./models import Picture

p = Picture(picture=pic_file)
p.save()
```