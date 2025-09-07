#!/usr/bin/env python3
"""
Python gRPC Server
A Python implementation of the User Management gRPC service
that provides the same functionality as the original Node.js gRPC server.

This server uses the shared proto definition from ../shared/proto/user.proto
"""

import grpc
from concurrent import futures
import time
import uuid
import sys
import os

# Add the proto directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'proto'))

# Import the generated protobuf files
import user_pb2
import user_pb2_grpc

class UserServiceServicer(user_pb2_grpc.UserServiceServicer):
    """Implementation of the UserService gRPC service."""
    
    def __init__(self):
        # In-memory user storage (same as Node.js version)
        self.users = [
            user_pb2.User(
            id="1",
            name="John Dower",
            email="john@example.com",
            status="active",
            created_at=int(time.time() * 1000)
            ),
            user_pb2.User(
            id="2",
            name="Jane Smith",
            email="jane@example.com",
            status="active",
            created_at=int(time.time() * 1000)
            ),
            user_pb2.User(
            id="3",
            name="Alice Johnson",
            email="alice.johnson@example.com",
            status="active",
            created_at=int(time.time() * 1000)
            ),
            user_pb2.User(
            id="4",
            name="Bob Williams",
            email="bob.williams@example.com",
            status="inactive",
            created_at=int(time.time() * 1000)
            ),
            user_pb2.User(
            id="5",
            name="Charlie Brown",
            email="charlie.brown@example.com",
            status="active",
            created_at=int(time.time() * 1000)
            ),
            user_pb2.User(
            id="6",
            name="Diana Prince",
            email="diana.prince@example.com",
            status="active",
            created_at=int(time.time() * 1000)
            ),
            user_pb2.User(
            id="7",
            name="Ethan Hunt",
            email="ethan.hunt@example.com",
            status="inactive",
            created_at=int(time.time() * 1000)
            ),
            user_pb2.User(
            id="8",
            name="Fiona Gallagher",
            email="fiona.gallagher@example.com",
            status="active",
            created_at=int(time.time() * 1000)
            ),
            user_pb2.User(
            id="9",
            name="George Martin",
            email="george.martin@example.com",
            status="active",
            created_at=int(time.time() * 1000)
            ),
            user_pb2.User(
            id="10",
            name="Hannah Lee",
            email="hannah.lee@example.com",
            status="inactive",
            created_at=int(time.time() * 1000)
            ),
            user_pb2.User(
            id="11",
            name="Ian Wright",
            email="ian.wright@example.com",
            status="active",
            created_at=int(time.time() * 1000)
            ),
            user_pb2.User(
            id="12",
            name="Julia Roberts",
            email="julia.roberts@example.com",
            status="active",
            created_at=int(time.time() * 1000)
            )
        ]
    
    def GetUsers(self, request, context):
        """Get all users - equivalent to the Node.js getUsers method."""
        print(f"GetUsers called - returning {len(self.users)} users")
        return user_pb2.UserList(users=self.users)
    
    def AddUser(self, request, context):
        """Add a new user - equivalent to the Node.js addUser method."""
        new_user = user_pb2.User(
            id=str(uuid.uuid4()),
            name=request.name,
            email=request.email,
            status=request.status or "active",
            created_at=int(time.time() * 1000)
        )
        
        self.users.append(new_user)
        print(f"User added: {new_user}")
        return new_user
    
    def UpdateUser(self, request, context):
        """Update an existing user - equivalent to the Node.js updateUser method."""
        # Find the user by ID
        user_index = -1
        for i, user in enumerate(self.users):
            if user.id == request.id:
                user_index = i
                break
        
        if user_index == -1:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found")
            return user_pb2.User()
        
        # Update the user with provided fields
        existing_user = self.users[user_index]
        updated_user = user_pb2.User(
            id=existing_user.id,
            name=request.name if request.name else existing_user.name,
            email=request.email if request.email else existing_user.email,
            status=request.status if request.status else existing_user.status,
            created_at=existing_user.created_at
        )
        
        self.users[user_index] = updated_user
        print(f"User updated: {updated_user}")
        return updated_user
    
    def DeleteUser(self, request, context):
        """Delete a user - equivalent to the Node.js deleteUser method."""
        # Find and remove the user by ID
        user_index = -1
        for i, user in enumerate(self.users):
            if user.id == request.id:
                user_index = i
                break
        
        if user_index == -1:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found")
            return user_pb2.Empty()
        
        removed_user = self.users.pop(user_index)
        print(f"User deleted: {request.id}")
        return user_pb2.Empty()

def serve():
    """Start the gRPC server."""
    # Create server with thread pool
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Add the UserService to the server
    user_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    
    # Listen on port 50051 (same as Node.js server)
    port = '50051'
    server.add_insecure_port(f'[::]:{port}')
    
    # Start the server
    server.start()
    print(f"Python gRPC server started on port {port}")
    print("Server is ready to accept connections...")
    
    try:
        # Keep the server running
        while True:
            time.sleep(86400)  # Sleep for a day
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.stop(0)

if __name__ == "__main__":
    serve()
