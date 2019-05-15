// fs :文件模块，负责文件读写
// 异步读取文件

var fs = require('fs')
fs.readFile('ceshi.txt','utf-8',function(err,data){
    if(err){
        console.log(err);
    }else{
        console.log(data);
    }
});
