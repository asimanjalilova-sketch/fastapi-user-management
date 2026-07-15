import grpc

from . import user_pb2
from . import user_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = user_pb2_grpc.UserServiceStub(channel)
request = user_pb2.UserRequest(id=1)
response = stub.GetUser(request)

print(response.id)
print(response.username)