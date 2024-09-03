from concurrent import futures
import grpc
import math
import square_root_pb2
import square_root_pb2_grpc

class CalculatorService(square_root_pb2_grpc.CalculatorServicer):

    def SquareRoot(self, request, context):
        number = request.number
        if number < 0:
            context.set_details('Number is negative')
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return square_root_pb2.SquareRootResponse()

        try:
            root = math.sqrt(number)
            return square_root_pb2.SquareRootResponse(root=root)
        except Exception as e:
            context.set_details('Internal server error: ' + str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return square_root_pb2.SquareRootResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    square_root_pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
