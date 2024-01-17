  // js代码  JS：事件驱动
var dom = document.getElementsByTagName("h3")[0]
dom.onclick = function () {
    // alert(123)
    this.style.color = "green"
}