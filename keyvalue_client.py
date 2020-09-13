from __future__ import print_function
import argparse
from http.client import REQUEST_ENTITY_TOO_LARGE
from platform import platform
from queue import Empty
from urllib import request
import keyvalue_pb2 as keyvalue
import keyvalue_pb2_grpc as keyvalue_grpc
import grpc
import sys

args = {}

class ConfigError(Exception):
    pass


def getKeyValue(stub):
    key = str(input('''\n
* Input the key: '''))
    response = stub.get(keyvalue.Key(key = key))
    
    if response.defined:
        print("\nKey: '%s'\nValue: '%s'" % (key, response.value))
    else:
        print("'%s': undefined" % key)



def putKeyValue(stub):
    key = str(input('''\n
* Input the key: '''))
    value = str(input('''\n
* Input the value: '''))
    new_keyvalue = keyvalue.NewKeyValue(key=key, value=value)
    
    stub.put(new_keyvalue)
    print("KeyValue added succesfully.")
    

def getKeys(stub):
    response = stub.getAllKeys(keyvalue.Void())
    print("\nList of all keys:\n")
    for key in response.keys:
        print(key)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        
        def main_menu():
            stub = keyvalue_grpc.KeyValueServiceStub(channel)
            option = int(input('''\n
*********  MENU  *********\n
1 - Get a value from a given key\n
2 - Add a new key and value set\n
3 - Get the list of all keys\n
0 - Exit\n
Enter the number:  '''))
            if option == 1:
                getKeyValue(stub=stub)
            elif option == 2:
                putKeyValue(stub=stub)
            elif option == 3:
                getKeys(stub=stub)
            elif option == 0:
                exit()
            else:
                print("This is not an option. Please input a number from the listed options.\n")
                main_menu()
        while True:
            try:
                main_menu()
            except ValueError:
                print("Please input a number from the options.\n")


if __name__ == '__main__':
    run()