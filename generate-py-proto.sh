#!/usr/bin/env bash
pip install grpcio-tools
python3 -m grpc.tools.protoc -I./ --python_out=. --grpc_python_out=. ./demo.proto