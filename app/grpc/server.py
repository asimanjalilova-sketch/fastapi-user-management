from concurrent import futures
import grpc

from . import user_pb2
from . import user_pb2_grpc

class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        print(f"Received request with id = {request.id}")

        return user_pb2.UserResponse(
            id=request.id,
            username="Bob"
        )
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserService(), server
    )

    server.add_insecure_port("[::]:50051")

    server.start()

    print("gRPC server is running on port 50051...")

    server.wait_for_termination()

if __name__ == "__main__":
    serve()