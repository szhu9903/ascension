//引用其他模块输出的变量，var foo = require('应用模块的路径')
var greet = require('./node');
var s = 'Zhu';
greet(s)

//process对象
process.nextTick(function () {
    console.log('nextTick callback');
})

console.log('nextTick wek set!')

// 判断javascript执行环境
if (typeof (window) === 'undefined') {
    console.log('Node');
} else {
    console.log('brower');
}