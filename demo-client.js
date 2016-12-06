const grpc = require('grpc');
const demo = grpc.load('demo.proto').demo;
const rpcStub = new demo.Demo('127.0.0.1:50051', grpc.credentials.createInsecure());

rpcStub.sayText({text: 'hello world'}, function(err, reply) {
    console.log(reply.text);
});

