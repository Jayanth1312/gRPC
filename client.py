import grpc
import square_root_pb2
import square_root_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = square_root_pb2_grpc.CalculatorStub(channel)
        try:
            number = float(input("Enter a number to find the square root: "))
            response = stub.SquareRoot(square_root_pb2.SquareRootRequest(number=number))
            print("Square Root:", response.root)
        except grpc.RpcError as e:
            print(f"gRPC Error: {e.code()}")
            print(f"Details: {e.details()}")

if __name__ == '__main__':
    run()
