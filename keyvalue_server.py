from concurrent import futures
import grpc
import logging
import sys

import keyvalue_pb2 as keyvalue
import keyvalue_pb2_grpc as keyvalue_grpc


class ConfigError(Exception):
    pass

fake_db = {
}

class KeyValueServicer(keyvalue_grpc.KeyValueServiceServicer):
    def get(self, request, context):
        key = request.key
        if key in fake_db.keys():            
            value=fake_db.get(key)
            return keyvalue.Value(value=value, defined=True)
        else:
            return keyvalue.Value(value=None, defined=False)

    def put(self, request, context):
        key = str(request.key)
        value = str(request.value)
        fake_db[key] = value
        return keyvalue.Void()

    def getAllKeys(self, request, context):
        return keyvalue.StoredKeys(keys= fake_db.keys())


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    keyvalue_grpc.add_KeyValueServiceServicer_to_server(KeyValueServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Listening on 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    try:
        serve()
    except ConfigError as e:
        print("error:", e.args[0])