
> 使用 sublime 的时候，记录了一些不错的插件


## 主题

soda http://www.cnblogs.com/picaso/p/3339168.html
	在 Preference  -> Setting-User的配置文件中输入
	"theme": "Soda Light.sublime-theme"
	"theme": "Soda Light 3.sublime-theme"
	如果想要深色的就输入：
	"theme": "Soda Dark.sublime-theme"
	 "theme": "Soda Dark 3.sublime-theme"

## 插件

DocBlockr : 自动生成大块的注释，并且可以用tab在不同内容之间切换，
AllAutocomplete : AllAutocomplete可以对打开的所有文件的变量名进行提示，增强版的代码自动提示符。
CTags :代码标签生成器，它支持函数的跳转，用来阅读源码非常方便
SublimeLinter ：行内语法检测插件，支持： C/C++, Java, Python, PHP, JS, HTML, CSS, etc.

增强：
WordCount：可以实时显示当前文件的字数
ConvertToUTF8：比上面的那个要方便，直接在菜单栏中可以转了
Terminal ：Sublime版的在当前文件夹内打开
Side​Bar​Enhancements ：右键一下子多处那么多选择
Compare Side-By-Side ：文件对比，Sublime版本的Beyond Compare
BracketHighlighter ：显示我在哪个括号内，前端和Lisp的福音啊

markdown：
MarkDown Editing ：支持Markdown语法高亮；支持Github Favored Markdown语法；自带3个主题。
Markdown Extended + Monokai Extends ：不错的Markdown主题，支持对多种语言的高亮
TableEditor ：Markdown中的表格书写体验真心不咋样，所有有人为这个开发了一个插件，具有较好的自适应性，会自动对齐，强迫症患者喜欢。
首先需要用ctrl + shift + p打开这个功能（Table Editor: Enable for current syntax or Table Editor: Enable for current view or "Table Editor: Set table syntax ... for current view"），然后就可以狂用tab来自动完成了
MarkdownPreview ：按CTRL + B生成网页HTML；在最前面添加[TOC]自动生成目录；

other：
Emmet ：你只需按约定的缩写形式书写而不用写整个代码，然后按“扩展”键，这些缩写就会自动扩展为对应的代码内容。 比如，你只需要输入 ((h4>a[rel=external])+p>img[width=500 height=320])*12 ，然后它会被扩展转换成12个列表项和紧随其后的图像。

html，css：
CSSComb ：这是用来给CSS属性进行排序的格式化插件。
CanIUse ：如果您想检查浏览器是否支持你包括在你的代码中的CSS和HTML元素，那么这是你需要的插件。所有您需要做的就是选择有疑问的元素，插件将为你做其余的事情。

Alignment ：这个插件让你能对齐你的代码，包括 PHP、CSS 和 Javascript。代码看起来更简洁和可读，便于编辑。
TrailingSpaces :高亮显示尾部多余的空格，强迫症患者专用
Trimmer :你知道当你编写代码时，由于错误或别的某些原因，会产生一些不必要的空格。需要注意的是多余的空格有时也会造成错误。这个插件会自动删除这些不必要的空格
ColorPicker :如果你经常要查看或设置颜色值，这个插件可以很方便地调用你本机的调色板应用。
SublimeCodeIntel :代码自动补全插件。它支持以下语言的自动提示功能：
	JavaScript, Mason, XBL, XUL, RHTML, SCSS, Python, HTML, Ruby, Python3, XML, Sass, XSLT, Django, HTML5, Perl, CSS, Twig, Less, Smarty, Node.js, Tcl, TemplateToolkit, PHP

SublimeREPL :对开发者来讲这个可能是最有用的插件之一了。SublimeREPL 可以直接在编辑器中运行一个解释器，支持很多语言：
	Clojure, CoffeeScript, F#, Groovy, Haskell, Lua, MozRepl, NodeJS, Python, R, Ruby, Scala, shell
AutoFileName :自动补全文件路径-非常方便

Colorcoder :高亮所有变量，因此可以极大的简化代码定位。
Clipboard History : 为的剪切板保存历史记录
AdvancedNewFile ：看名字就知道来，可以配置新建文件的附属文件，直接生成一个工程都可以



## 配置c环境

C++.sublime-build:

"cmd": ["g++","-Wall", "${file}", "-o", "${file_path}/${file_base_name}"],
"file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
"working_dir": "${file_path}",
"selector": "source.c, source.c++",
"encoding":"cp936",
"variants":
[
{
"name": "Run",
"cmd": ["cmd", "/c", "g++", "-Wall","${file}", "-o", "${file_path}/${file_base_name}", "&&", "cmd", "/c", "${file_path}/${file_base_name}"]
},
{
"name": "RunInCommand",
"cmd": ["cmd", "/c", "g++", "-Wall","${file}", "-o", "${file_path}/${file_base_name}", "&&", "start", "cmd", "/c", "${file_path}/${file_base_name} & echo.&pause"]
}
]
}

c++按键绑定:

[
	{keys [f5], command build, args {variant RunInCommand}}
]
