## JavaScript

### . 字符串
* toUpperCase()、toLowerCase(): 字符串大小写转换;`s.toLowerCase()`
* indexOf(): 搜索字符出现位置索引;`s.indexOf('szhu')`
* substring(): 字符串切片;`s.substring(3, 9)`
### . 数组
* indexOf(): 搜索元素出现为止;`s.indexOf(33)`
* slice(): 数组切片;`s.slice(3, 9)`
* push()、pop(): 数组末尾添加和弹出元素;`s.push('szi')`
* unshift()、shift(): 数组开头添加和弹出元素;`s.unshift('szi')`
* sort(): 排序;`s.sort()`
* reverse(): 反转数组;`s.reverse()`
* splice(): 数组任意位置插入元素;`s.splice(1, 'szhu')`
* concat(): 拼接数组;`s.concat([1, 'szhu'])`
* join(): 用指定连接符拼接数组中所有元素;`s.concat('-)`
### . 函数
* arguments: 获取调用者传入的所有参数array()
* rest: 接收任意个参数 `function foo(a,b,...rest){};`
* let: 替代var可以申明一个块级作用域的变量
* toString(): 对象转换为字符串
* find(fun)、findIndex(fun) : 查找第一个复合条件的元素，返回元素、返回索引 
### . 对象
* typeof : 判断对象类型; null、Array 类型为object
* parseInt、parseFloat: 任意类型转换到number
* isArray(): 判断Array类型  
* JSON.stringify(obj)、JSON.parse():JSON序列化和反序列化
* Object.create():  继承; `Object.create(obj)`
### . 浏览器
* navigator :表示浏览器信息;
* screen: 返回屏幕信息, `width、height`
* window: 全局、浏览器窗口信息`innerWidth、innerHeight`
* location: 当前页面,   
    url:`location.href`;  
    重载:`location.reload()`
* document: 页面DOM根节点,  
    查找节点(ID): `document.getElementById()`  
    class查找: `var res = document.getElementByClassName()`  
    获取节点下所有子节点: `res.children`  
    获取节点下第一个: `re.firstElementChild`  
    获取节点下最后一个: `res.lastElementChild` 
    创建一个元素: `var li = document.createElement('li')`  
    新元素添加属性: `li.class`、`li.style`、`li.innerText`、`li.innerHTML替换`  
    appendChild、removeChild: 添加删除元素
### . AJAX
* 加载库: `request = new XMLHttpRequest();` or   
`request = new ActiveXObject('microsoft.XMLHTTP');`
* 通过定义回调函数，检测响应，处理响应 [aj_demo](https://github.com/szhu9903/ascension/blob/master/python_up/python_web_test/javascript_web/js_test.html)
### . JQuery
* 层级选择器：层级下边所有p$('div p')来选择，层级之间用空格隔开。
* 子选择器$('parent>child')：类似层级选择器，但是限定了层级关系必须是父子关系，就是<child>节点必须是<parent>节点的直属子节点。
* 过滤器(Filter)： 配合层级选择元素的筛选  $('parent>child：last')
* 函数过滤器(map): jquery.map(function(){}) 例如：[aj_demo](https://github.com/szhu9903/ascension/blob/master/python_up/python_web_test/javascript_web/js_test.html)
* DOM操作: `css`添加样式  `addClass`、 添加class属性、`hide()、show()`隐藏显示元素；`attr()、removeAttr()`操作DOM节点的属性
### . 事件
* 鼠标事件  
`click`: 鼠标单击时触发；  
`dblcheck`：鼠标双击时触发；  
`mouseenter`：鼠标进入时触发；  
`mouseleave`：鼠标移出时触发；  
`mousemove`：鼠标在DOM内部移动时触发；  
`hover`：鼠标进入和退出时触发两个函数，相当于mouseenter加上mouseleave。
* 键盘事件:键盘事件仅作用在当前焦点的DOM上通常是`<input>`和`<textarea>`    
`keydown`：键盘按下时触发  
`keyup`：键盘松开时触发  
`keypress`：按一次键后触发。  
* 其他事件
`focus`：当DOM获得焦点时触发；
`blur`：当DOM失去焦点时触发；
`change`：当`<input>、<select>或<textarea>`的内容改变时触发；
`submit`：当`<form>`提交时触发；
`ready`：当页面被载入并且DOM树完成初始化后触发
