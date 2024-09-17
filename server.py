import grpc
from concurrent import futures
import math
import time
from calculator_pb2 import CalculatorResponse
import calculator_pb2_grpc

class AdvancedCalculatorServicer(calculator_pb2_grpc.AdvancedCalculatorServicer):
    def Add(self, request, context):
        if request.a > 1000000 or request.b > 1000000:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Numbers too large (max 1,000,000)")
            return CalculatorResponse()
        return CalculatorResponse(result=request.a + request.b)

    def Divide(self, request, context):
        if request.b == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Cannot divide by zero")
            return CalculatorResponse()
        return CalculatorResponse(result=request.a / request.b)

    def Factorial(self, request, context):
        if request.n < 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Factorial is not defined for negative numbers")
            return CalculatorResponse()
        if request.n > 20:
            context.set_code(grpc.StatusCode.OUT_OF_RANGE)
            context.set_details("Input too large (max 20)")
            return CalculatorResponse()
        result = math.factorial(request.n)
        return CalculatorResponse(result=result)

    def Fibonacci(self, request, context):
        if request.n < 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Fibonacci is not defined for negative numbers")
            return CalculatorResponse()
        if request.n > 30:
            context.set_code(grpc.StatusCode.OUT_OF_RANGE)
            context.set_details("Input too large (max 30)")
            return CalculatorResponse()
        if request.n > 20:
            time.sleep(5)
            if context.is_active():
                a, b = 0, 1
                for _ in range(request.n):
                    a, b = b, a + b
                return CalculatorResponse(result=a)
            else:
                return CalculatorResponse()
        a, b = 0, 1
        for _ in range(request.n):
            a, b = b, a + b
        return CalculatorResponse(result=a)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_AdvancedCalculatorServicer_to_server(AdvancedCalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()