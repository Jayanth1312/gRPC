# gRPC
__gRPC(google remote procedure call)__ is a framework which helps micro services to communicate with each other. gRPC is mainly works in the back-end side and ensures the connection between services. the gRPC can be implemented in many laguages mainly using Python, Java, Golang.

# Example for realtime application which uses microservices:
__UBER__
__Overview:__ Uber relies heavily on microservices to manage its ride-hailing services, which includes everything from user authentication to real-time tracking of rides.

__Microservices Examples:__
*Maps Service:* Manages route calculations, real-time tracking, and estimated arrival times.
*Payment Service:* Processes payments, manages promotions, and handles refunds.
*Ride Matching Service:* Matches drivers with riders based on location and availability.
*Notification Service:* Sends notifications for ride status, driver arrival, and payment confirmations.

# How it works
gRPC uses HTTP/2 for transport, and Protocol Buffers for defining services and encoding data. It's designed to make the client think the server is on the same machine.

# Where it's used
gRPC is used in many environments, including connecting services inside or across data centers, and connecting remote services to backend services. 

# Why it's popular
gRPC is popular because it's performance-centric, easier to use than typical HTTP calls, and more reliable and secure. 

# Limitations
Because gRPC uses HTTP/2, it's not possible to call a gRPC service from a web browser directly. A proxy layer and gRPC-web are required to perform conversions between HTTP/1.1 and HTTP/2.

-> Python 3.8:
    - requests (HTTP 1.1)
-> Java SE 9:
    - HttpURLConnection: (HTTP 1.1)
-> GoLang 1.16:
    - http (HTTP 2.0 by default)

*Golang is optimal for creating a gRPC services rather in python and java because the gRPC framework built using Golang and seamless intergration will be effective when using a gRPC service built using Golang.*

# Protocol buffer
.proto file extension is used for Protocol Buffers, which is a binary data format that's used to describe data structures and services.

.proto files in gRPC contain the interface definition language (IDL) for a gRPC service. They define the service, methods, and data types used in the service. The file contains a series of definitions for the service, including

# Status codes
In gRPC, status codes represent the outcome of a remote procedure call (RPC). These codes are crucial for understanding the result of an operation, whether it succeeded, failed, or encountered an error. They are similar to HTTP status codes but are specific to gRPC and provide more granular control over error handling and response.
__Visit this site know what are the different status codes__
[Status codes](https://grpc.io/docs/guides/status-codes/)

# To create a microservice using gRPC follow these steps
_create a vitual environment (optional)_:
-> python -m venv env
-> .\env\Scripts\Activate

_Install required libraries_:
-> pip install grpcio grpcio-tools

_create no.of files required for the micro service you are working on and there should be a .proto file which conatin service method and data types used in the micro service_:
-> file_name.proto

_Compile the .proto file first for code generation which is also the code to use micro services_
-> python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. file_name.proto

_Finally run the server and client files or main files which you created along with the proto file_