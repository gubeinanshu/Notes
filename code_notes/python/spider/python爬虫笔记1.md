
## 识别网站所用的技术

安装第三方包

```
pip install builtwith
```

```python

import builtwith
builtwith.parse('http://example.webscraping.com')

```

## 寻找网站所有者

安装第三方包
```
pip install python-whois
```

```python

import whois
print whois.whois('appspot.com')

```
