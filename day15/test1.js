// data
var now = new Date();
console.log(now.getTime())

// Math对象
console.log(Math.random() * 10)
// json
data = {name:'yuan', age:18}
console.log(JSON.stringify(data))

JSON.parse('{"a":12}')

// js作用域
var x = 100;
function foo(){
    var x = 10;
    console.log(x);
}