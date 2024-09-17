import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.AdvancedCalculatorStub(channel)

        try:
            response = stub.Add(calculator_pb2.BinaryOpRequest(a=5, b=3))
            print(f"5 + 3 = {response.result}")
        except grpc.RpcError as e:
            print(f"Add RPC failed: {e.code()}: {e.details()}")

        try:
            response = stub.Add(calculator_pb2.BinaryOpRequest(a=1000001, b=3))
            print(f"1000001 + 3 = {response.result}")
        except grpc.RpcError as e:
            print(f"Add RPC failed: {e.code()}: {e.details()}")

        try:
            response = stub.Divide(calculator_pb2.BinaryOpRequest(a=10, b=2))
            print(f"10 / 2 = {response.result}")
        except grpc.RpcError as e:
            print(f"Divide RPC failed: {e.code()}: {e.details()}")

        try:
            response = stub.Divide(calculator_pb2.BinaryOpRequest(a=10, b=0))
            print(f"10 / 0 = {response.result}")
        except grpc.RpcError as e:
            print(f"Divide RPC failed: {e.code()}: {e.details()}")

        try:
            response = stub.Factorial(calculator_pb2.UnaryOpRequest(n=5))
            print(f"Factorial of 5 = {response.result}")
        except grpc.RpcError as e:
            print(f"Factorial RPC failed: {e.code()}: {e.details()}")

        try:
            response = stub.Factorial(calculator_pb2.UnaryOpRequest(n=25))
            print(f"Factorial of 25 = {response.result}")
        except grpc.RpcError as e:
            print(f"Factorial RPC failed: {e.code()}: {e.details()}")

        try:
            response = stub.Fibonacci(calculator_pb2.UnaryOpRequest(n=10))
            print(f"10th Fibonacci number = {response.result}")
        except grpc.RpcError as e:
            print(f"Fibonacci RPC failed: {e.code()}: {e.details()}")

        try:
            response = stub.Fibonacci(calculator_pb2.UnaryOpRequest(n=35))
            print(f"35th Fibonacci number = {response.result}")
        except grpc.RpcError as e:
            print(f"Fibonacci RPC failed: {e.code()}: {e.details()}")

        try:
            response = stub.Fibonacci(calculator_pb2.UnaryOpRequest(n=25), timeout=3)
            print(f"25th Fibonacci number = {response.result}")
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.DEADLINE_EXCEEDED:
                print("Fibonacci RPC timed out")
            else:
                print(f"Fibonacci RPC failed: {e.code()}: {e.details()}")

if __name__ == '__main__':
    run()