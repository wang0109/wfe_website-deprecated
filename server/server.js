console.log("hello world");


var http = require('http');

var server = http.createServer(function(req,res) {
    res.writeHead(200, {"Content-Type:": "text/plain"});
    res.end("hello world");
});

server.listen(8888);

console.log("server running");
