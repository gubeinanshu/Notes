更多的参考 https://blog.csdn.net/qq_35573326/article/details/82049654 (过期时间等)

安装

```
npm install vue-cookies --save
```
main.js全局引用
```
import Vue from 'Vue'
import VueCookies from 'vue-cookies'
Vue.use(VueCookies)
```

Set a cookie


```
this.$cookies.set(keyName, value[, expireTimes[, path[, domain[, secure]]]])   //return this
```


Get a cookie


```
this.$cookies.get(keyName)       // return value
```
  

Remove a cookie


```
this.$cookies.remove(keyName [, path [, domain]])   // return  false or true , warning： next version return this； use isKey(keyname) return true/false,please
```

Exist a cookie name


```
this.$cookies.isKey(keyName)        // return false or true
```


Get All cookie name


```
this.$cookies.keys()  // return a array
```

