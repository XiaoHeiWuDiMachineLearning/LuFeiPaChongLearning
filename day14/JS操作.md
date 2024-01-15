## 4.12、BOM对象（了解）

BOM:Broswer object model,即浏览器提供我们开发者在javascript用于操作浏览器的对象。

### 4.12.1、window对象

* 窗口方法

```js
// BOM  Browser object model 浏览器对象模型

// js中最大的一个对象.整个浏览器窗口出现的所有东西都是window对象的内容.
console.log( window );

// alert()  弹出一个警告框
window.alert("hello");

//confirm  弹出一个确认框,点击确认,返回true, 点击取消,返回false
var ret = confirm("您确认要删除当前文件么?");
console.log( ret  );

// 弹出一个消息输入框,当点击确认以后,则返回可以接收到用户在输入框填写的内容.如果点击取消,则返回null
var ret = prompt("请输入一个内容","默认值");
console.log( raet );

// close() 关闭当前浏览器窗口
window.close();

//打开一个新的浏览器窗口
window.open("http://www.baidu.com","_blank","width=800px,height=500px,left=200px,top=200px");

```

### 4.12.2、location ( 地址栏)对象

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<button onclick="func1()">查看Location对象</button>
<button onclick="func2()">跳转到百度</button>
<button onclick="func3()">F5刷新页面</button>
<script>
    function func1(){
        console.log( location );
    }
    // 地址栏对象控制和操作地址栏
    // 所谓的地址就是当前页面所在地址
    // 地址结构:
    // 协议://域名:端口/路径/文件名?查询字符串#锚点
    console.log( `协议=>${location.protocol}` );
    console.log( `域名=>${location.port}` );
    console.log( `域名=>${location.hostname}` );
    console.log( `域名:端口=>${location.host}` );
    console.log( `路径=>${location.pathname}` );
    console.log( `查询字符串=>${location.search}` );
    console.log( `锚点=>${location.hash}` );
    console.log(`完整的地址信息=>${location.href}`);

    function func2(){
        // location.href="http://www.baidu.com"; // 页面跳转
        location.assign("http://www.baidu.com"); // 页面跳转
    }

    function func3(){
        location.reload(); // 刷新页面
    }
</script>
</body>
</html>
```

### `4.12.3、history`对象：

代表当前窗口的浏览历史记录，可以通过`history`操作浏览器的前进和后退。例如：

```js
// 向前进一步（相当于点击浏览器的“前进”按钮）
history.forward();

// 向后退一步（相当于点击浏览器的“后退”按钮）
history.back();

```

### `4.12.4、navigator`对象：

提供了浏览器的相关信息，例如浏览器类型和版本、操作系统、语言等。例如：

```js
// 获取浏览器名称和版本信息
var browserName = navigator.appName;
var browserVersion = navigator.appVersion;
console.log(browserName + " " + browserVersion);

// 获取操作系统类型
var osName = navigator.platform;
console.log(osName);

// 获取语言设置
var language = navigator.language;
console.log(language);
```



## 4.13、DOM对象(了解)

DOM  document Object Model 文档对象模型

```js
// 整个html文档,会保存一个文档对象document
// console.log( document ); // 获取当前文档的对象
```

### 4.13.1、查找标签

* 直接查找标签

```js
document.getElementsByTagName("标签名")
document.getElementById("id值")
document.getElementsByClassName("类名")
//返回dom对象，就是标签对象或者数组
```

* CSS选择器查找

```JS
document.querySelector("css选择器")  //根据css选择符来获取查找到的第一个元素，返回标签对象（dom对象）
document.querySelectorAll("css选择器"); // 根据css选择符来获取查找到的所有元素,返回数组
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>


<div id="i1">DIV1</div>

<div class="c1">DIV</div>
<div class="c1">DIV</div>
<div class="c1">DIV</div>


<div class="outer">
    <div class="c1">item</div>
</div>


<div class="c2">
    <div class="c3">
        <ul class="c4">
            <li class="c5" id="i2">111</li>
            <li>222</li>
            <li>333</li>
        </ul>
    </div>
</div>

<script>

   // 直接查找
   var ele = document.getElementById("i1");  // ele就是一个dom对象
   console.log(ele);

   var eles = document.getElementsByClassName("c1"); // eles是一个数组 [dom1,dom2,...]
   console.log(eles);

   var eles2 = document.getElementsByTagName("div"); // eles2是一个数组 [dom1,dom2,...]
   console.log(eles2);

  //定位outer下的c1对应的标签
   var outer = document.getElementsByClassName("outer")[0];
   var te = outer.getElementsByClassName("c1");
   console.log(te);

    // css选择器
		//层级定位(空格可以表示一个或多个层级)
    var dom = document.querySelector(".c2 .c3 .c5");
    console.log(":::",dom);
		//层级定位
    var doms = document.querySelectorAll("ul li");
    console.log(":::",doms);
    
</script>

</body>
</html>
```

### 4.13.2、绑定事件

* 静态绑定 ：直接把事件写在标签元素中

```html

<div id="div" onclick="foo()">click</div>

<script>
    function foo(){           
        console.log("foo函数");   
    }
</script>

```

* 动态绑定：在js中通过代码获取元素对象,然后给这个对象进行后续绑定

```html
<p id="i1">试一试!</p>

<script>

    var ele=document.getElementById("i1");

    ele.onclick=function(){
        console.log("ok");
        
    };

</script>
```

> 一个元素本身可以绑定多个不同的事件, 但是如果多次绑定同一个事件,则后面的事件代码会覆盖前面的事件代码

- 在 JavaScript 中 this 不是固定不变的，它会随着执行环境的改变而改变。

  - 单独使用 this，则它指向全局(Global)对象。在浏览器中，window 就是该全局对象为 

  - ```
    var x = this;
    ```

  - 在函数中(作为函数的返回值)，函数的所属者/调用者默认绑定到 this 上。

  - ```js
    function myFunction() {
      return this;
    }
    ```

  - 对象方法中的this就是对象本身

  - ```
    var person = {
      firstName  : "John",
      lastName   : "Doe",
      id         : 5566,
      myFunction : function() {
        return this;
      }
    };
    ```

  - 事件中的this就是接收事件的 HTML 标签

  - ```
    <button onclick="this.style.display='none'">
    点我后我就消失了
    </button>
    ```




## 4.14 进阶操作（重点）

- ES6新特性
  - ES6是JavaScript语言的下一代标准，已经在2015年6月正式发布了。Mozilla公司将在这个标准的基础上，推出JavaScript 2.0。

- 变量提升

  - 查看以下代码, 是否可以被运行

  - ```js
    function fn(){
        console.log(name);
        var name = '大马猴';
    }
    fn()
    ```

  - 发现问题了么. 这么写代码, 在其他语言里. 绝对是不允许的. 但是在js里. 不但允许, 还能执行. 为什么呢?  因为在js执行的时候. 它会首先检测你的代码.  发现在代码中会有name使用. OK. 运行时就会变成这样的逻辑:

  - ```js
    function fn(){
        var name;
        console.log(name);
        name = '大马猴';
    }
    fn();
    ```

  - 看到了么. 实际运行的时候和我们写代码的顺序可能会不一样....这种把变量提前到代码块第一部分运行的逻辑被称为**变量提升**. 这在其他语言里是绝对没有的. 并且也不是什么好事情. 正常的逻辑不应该是这样的. 那么怎么办?  在新的ES6中. 就明确了, 这样使用变量是不完善的. es6提出. 用let来声明变量. 就不会出现该问题了. 

  - ```js
    function fn(){
        console.log(name);  // 直接报错, let变量不可以变量提升.
        let name = '大马猴'; 
    }
    fn()
    ```

    - 用let声明变量是新版本javascript提倡的一种声明变量的方案

  - let还有哪些作用呢?

  - ```js
    function fn(){
        var name = "周杰伦";
        var name = "王力宏";
        console.log(name);
    }
    fn()
    ```

  - 显然一个变量被声明了两次. 这样也是不合理的. var本意是声明变量. 同一个东西. 被声明两次. 所以ES6规定. let声明的变量. 在同一个作用域内. 只能声明一次. 

  - ```js
    function fn(){
        let name = "周杰伦";
        console.log(name);
        let name = "王力宏";
        console.log(name);
    }
    fn()
    ```

  - 注意, 报错是发生在代码检查阶段. 所以. 上述代码根本就执行不了. 在同一个作用域内. let声明的变量只能声明一次. 其他使用上和var没有差别.

- eval函数

  - eval本身在js里面正常情况下使用的并不多. 但是很多网站会利用eval的特性来完成反爬操作. 我们来看看eval是个什么鬼?  

  - 从功能上讲, eval非常简单.  它可以动态的把字符串当成js代码进行运行. 

  - ```js
    s = "console.log('我爱你')";
    eval(s);
    ```

  - 也就是说. eval里面传递的应该是即将要执行的代码(字符串). 那么在页面中如果看到了eval加密该如何是好?  其实只要记住了一个事儿. 它里面不论多复杂. 一定是个字符串. 

  - 比如:

  - ```js
    eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--)d[e(c)]=k[c]||e(c);k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('0.1(\'我爱你\')',62,2,'console|log'.split('|'),0,{}))
    ```

    - 这一坨看起来, 肯定很不爽. 怎么变成我们看着很舒服的样子呢?  记住. eval()里面是字符串. 记住~!!
    - 那我想看看这个字符串长什么样?  就把eval()里面的东西拷贝出来. 执行一下. 最终一定会得到一个字符串. 要不然eval()执行不了的. 对不...于是就有了下面的操作.
    - ![Snip20220107_77](assets/Snip20220107_77.png)

    - http://tools.jb51.net/password/evalencode, 在赠送你一个在线JS处理eval的网站. 大多数的eval加密. 都可以搞定了. 
    - ![Snip20220107_78](assets/Snip20220107_78.png)

- 内置对象：window

  - window对象是一个很神奇的东西. 你可以把这东西理解成javascript全局的内置对象. 如果我们默认不用任何东西访问一个标识符. 那么默认认为是在用window对象. 

  - ```js
    window.mm = "爱你" //定义了一个全局变量
    console.log(mm); 
    ```
  
  - 综上,  我们可以得出一个结论. 全局变量可以用window.xxx来表示. 
  
  - ok. 接下来. 注意看了. 我要搞事情了
  
    - 想要在函数外部调用该函数内部定义的一个内置函数，不可使用返回值的机制，如何实现？
  
  - ```js
    (function(){
        let chi = function(){
            console.log("我是吃")
        }
        window.w_chi = chi //全局变量chi
    })();
    //如何调用
    w_chi() //chi()
    
    //换一种写法. 你还认识么?
    (function(w){
        let chi = function(){
            console.log("我是吃")
        }
        w.chi = chi
    })(window);
    chi()
    ```
  
  

# 第5章 、jQuery

## 5.1、jQuery介绍

* jQuery是什么

jQuery是一个快速、简洁的JavaScript框架。jQuery设计的宗旨是“write Less，Do More”，即倡导写更少的代码，做更多的事情。它封装JavaScript常用的功能代码，提供一种简便的JavaScript设计模式，优化HTML文档操作、事件处理等功能。

jQuery兼容各种主流浏览器，如IE 6.0+、FF 1.5+、Safari 2.0+、Opera 9.0+等

* jQuery的版本

目前在市场上, 1.x , 2.x, 3.x 功能的完善在1.x, 2.x的时候是属于删除旧代码,去除对于旧的浏览器兼容代码。3.x的时候增加es的新特性以及调整核心代码的结构

* jQuery的引入

根本上jquery就是一个写好的js文件,所以想要使用jQuery的语法必须先引入到本地

```html
<script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.js"></script>
```

## 5.2、jQuery的选择器

### 5.2.1、直接查找

* 基本选择器 

```go
/*
#id         # id选择符 
element     # 元素选择符
.class      # class选择符  
selector1, selector2, selectorN   # 同时获取多个元素的选择符 

jQ选择器：

$("#id")   == document.getElementById('id')
$(".class")  
$("element")  
*/
```

## 5.3、jQuery的事件绑定

```js
/*
用法:
	直接通过事件名来进行调用
  $().事件名(匿名函数)
  	 
*/
```

案例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
    <div id="d1">i am div tag</div>
    <input type="text" id="t">
</body>
<script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.js"></script>
<script>
    $('#d1').click(function () {
        window.alert('点击了div标签！')
    })

    $('#t').blur(function () {
        window.alert('写完了吗？')
    })
</script>
</html>
```

## 5.4 Ajax请求(重点)

- 什么是ajax？

  - AJAX = 异步的javascript和XML（Asynchronous Javascript and XML）

  - 它不是一门编程语言，而是利用JavaScript在保证页面不被刷新、页面链接不改变的情况下与服务器交换数据并更新部分网页的技术。

  - 对于传统的网页，如果想更新内容，那么必须要刷新整个页面，但有了Ajax，便可以在页面不被全部刷新的情况下更新其内容。在这个过程中，页面实际上是在后台与服务器进行了数据交互，获得数据之后，再利用JavaScript改变页面，这样页面内容就会更新了。（微博页面加载过程的例子，加载一会下方才会出现内容，这其实就是Ajax加载的过程。）

  - 简言之，在不重载整个网页的情况下，AJAX通过后台加载数据，并在网页上进行显示。

  - 通过 jQuery AJAX 方法，您能够使用 HTTP Get 和 HTTP Post 从远程服务器上请求文本、HTML、XML 或 JSON - 同时您能够把这些外部数据直接载入网页的被选元素中。

  - ```js
    //get()方式
       $("#btn").click(function(){
            var url = "yourUrl?param1=value1&param2=value2"; // 在url中添加参数
            $.ajax({
                type: "GET",
                url: url,
                dataType: "json",
                success: function(data){
                    console.log(data); // 处理回调数据
                },
                error : function(error) {
                    console.log(error); // 处理错误信息
                }
            });
        });
    
    //or
    $("#btn").click(function(){
            $.ajax({
                type: "GET",
                url: "yourUrl",
                data: { // 使用data选项传递参数
                    param1: "value1",
                    param2: "value2"
                },
                dataType: "json",
                success: function(data){
                    console.log(data); // 处理回调数据
                },
                error : function(error) {
                    console.log(error); // 处理错误信息
                }
            });
        });
    ```
  
- ```js
    //post()方式
     $("#btn").click(function() {
            $.ajax({
                type: "POST",
                url: "yourUrl", // 请求地址
                data: { // 请求参数
                    param1: "value1",
                    param2: "value2"
                },
                dataType: "json", // 服务器返回的数据类型
                success: function(data) { // 成功回调函数
                    console.log(data); // 打印服务器返回的数据
                },
                error: function(error) { // 失败回调函数
                    console.log(error); // 打印错误信息
                }
            });
        });
    ```



- 常用的抓包工具：

  - win：fiddler
  - mac：Charles

  易语言：适合写外挂 

  数据可视化：pyechars，matplotlib，Seaborn



























