# KV-store-grpc

This work is a Key-Value store in memory using gRPC.

The Key-Value Store primitives are:

* put(key, value)
* get(key) : value
* getAllKeys() : Key[]

This work uses gRPC protocol to allow the customer to add a key and value. It will not be necessary to implement data buckets for each customer. That is, all customers will be able to access a common database.

The work was developed in python.

## Student

* Carla d'Abreu Martins Vieira

## Teacher

* Hugo de Paula

## Prerequisites
All the following prerequisite information can be found on [grpc.io/docs/languages/python/quickstart/](https://grpc.io/docs/languages/python/quickstart/)

Python 2.7, or Python 3.4 or higher
```shell
pip version 9.0.1 or higher
```
If necessary, upgrade your version of pip:
```shell
$ python -m pip install --upgrade pip
```
If you cannot upgrade pip due to a system-owned installation, you can run the example in a virtualenv:
```shell
$ python -m pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ python -m pip install --upgrade pip
```

### gRPC
Install gRPC:
```shell
$ python -m pip install grpcio
```
Or, to install it system wide:
```shell
$ sudo python -m pip install grpcio
```
On El Capitan OSX, you may get the following error:
```shell
$ OSError: [Errno 1] Operation not permitted: '/tmp/pip-qwTLbI-uninstall/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/six-1.4.1-py2.7.egg-info'
```
You can work around this using:
```shell
$ python -m pip install grpcio --ignore-installed
```

### gRPC tools
Python’s gRPC tools include the protocol buffer compiler protoc and the special plugin for generating server and client code from .proto service definitions. For the first part of our quick-start example, we’ve already generated the server and client stubs from helloworld.proto, but you’ll need the tools for the rest of our quick start, as well as later tutorials and your own projects.

To install gRPC tools, run:
```shell
$ python -m pip install grpcio-tools
```
# Use Instructions

From one terminal, run the server:
```shell
$ python keyvalue_server.py
```

From another terminal, run the client:
```shell
$ python keyvalue_server.py
```
Select the option from the client menu.