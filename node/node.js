var s = 'Hello'
function greet(name) {
    console.log(s + ',' + name + '!')
}
// 在模块中对外输出变量，module.exports = variable
module.exports = greet
