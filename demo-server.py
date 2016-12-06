import grpc
import demo_pb2
import concurrent.futures as futures
import logging
import time

class Demo(demo_pb2.DemoServicer):
    def sayText(self, payload, more):
        logging.error("Got %s from node" % payload.text)
        return demo_pb2.Text(text="Successfully said " + payload.text)

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    demo_pb2.add_DemoServicer_to_server(Demo(), server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()

    while True:
        time.sleep(1)