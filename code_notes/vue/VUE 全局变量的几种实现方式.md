# 变量全局使用
## 1，全局变量专用模块
> file name: Globa.vue  ,建议用Globa.js
> 使用时，引入模块便可
```
test = 1
export default
{
    test
}
```


## 2，全局变量模块挂载到Vue.prototype里

```
Global.js同上，在程序入口的main.js里加下面代码
import global_ from './components/tool/Global'
Vue.prototype.GLOBAL = global_

使用
<script>
export default {
  data () {
    return {
      getColor: this.GLOBAL.getRandColor,
    }
  }
}
</script>
```

## 3，使用VUEX
[VUEX官方](https://vuex.vuejs.org/zh/guide/)


# 函数全局使用

## 方法1. 在main.js里面直接写函数

```js
Vue.prototpye.test_one = ()=>alert('a')
Vue.prototpye.test_two = function () {
    return alert('b')
}
```

## 方法2. 新建一个模块文件，挂载到main.js上面

file name: global_func.js
```
// param为传入参数
function packageFunc (param) {
  alert(param)
}

export default {
  // Vue.js的插件应当有一个公开方法 install。这个方法的第一个参数是 Vue 构造器，第二个参数是一个可选的选项对象。
  install: function (Vue) {
    Vue.prototype.global_func = (param) => packageFunc(param)
  }
}
```
main.js写

```
import globalFunc from "@/api/global_func"
Vue.use(globalFunc)
```
使用

```
this.global_func("test")
```

