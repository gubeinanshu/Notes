## router-link传递参数并获取

跳转链接
```
<router-link :to="{path:'libraryDetail/', query:{library_id:data.library_id}}">
```

获取参数：

```
library_id = this.$route.query.library_id;
```

## 1.query方式传参和接收参数

```
传参: 
this.$router.push({
        path:'/xxx'
        query:{
          id:id
        }
      })
  
接收参数:
this.$route.query.id
```


## 2.params方式传参和接收参数

```
传参: 
this.$router.push({
        name:'xxx'
        params:{
          id:id
        }
      })
  
接收参数:
this.$route.params.id
```

> 注意:params传参，push里面只能是 name:'xxxx',不能是path:'/xxx',因为params只能用name来引入路由，如果这里写成了path，接收参数页面会是undefined！！！

> 另外，二者还有点区别，直白的来说query相当于get请求，页面跳转的时候，可以在地址栏看到请求参数，而params相当于post请求，参数不会再地址栏中显示

> 注意:传参是this.$router,接收参数是this.$route,这里千万要看清

- 1.$router为VueRouter实例，想要导航到不同URL，则使用$router.push方法
- 2.$route为当前router跳转对象，里面可以获取name、path、query、params等