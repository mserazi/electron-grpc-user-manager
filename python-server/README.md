# Python gRPC Server

This directory contains a Python gRPC server implementation that provides the same user management functionality as the original Node.js gRPC server. It uses the same protobuf definitions and serves on the same port (50061).

## 📁 Directory Structure

```
python-server/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── start_server.py       # Main startup script
├── generate_protobuf.py  # Protobuf generation script
├── server.py            # gRPC server implementation
└── proto/
    ├── user_pb2.py        # Generated protobuf messages (auto-generated)
    └── user_pb2_grpc.py   # Generated gRPC service (auto-generated)
```

**Protocol Definitions**: Reads from `../shared/proto/user.proto` and generates Python files locally.

## 🚀 Quick Start

### 1. Install Dependencies and Generate Protobuf Files

```bash
cd python-server
python start_server.py --install
```

This will:
- Install `grpcio`, `grpcio-tools`, and `protobuf` packages
- Generate `user_pb2.py` and `user_pb2_grpc.py` from the `.proto` file

### 2. Start the Server

```bash
python start_server.py
```

The server will start on `localhost:50061` and be ready to accept gRPC connections.

## 🔧 Manual Setup (Alternative)

If you prefer to set things up manually:

```bash
cd python-server

# Install dependencies
pip install -r requirements.txt

# Generate protobuf files
python generate_protobuf.py

# Start the server
python server.py
```

## 📡 gRPC Service Methods

The server implements the following gRPC methods:

| Method | Description | Request | Response |
|--------|-------------|---------|----------|
| `GetUsers` | Get all users | `Empty` | `UserList` |
| `AddUser` | Create a new user | `User` | `User` |
| `UpdateUser` | Update an existing user | `User` | `User` |
| `DeleteUser` | Delete a user by ID | `UserRequest` | `Empty` |

## 🔌 Connection Details

- **Protocol**: gRPC over HTTP/2
- **Host**: `localhost`
- **Port**: `50061`
- **Credentials**: Insecure (for development)

## 💾 Data Storage

The server uses in-memory storage with sample data:

```python
users = [
    {
        "id": "1",
        "name": "John Doe",
        "email": "john@example.com",
        "status": "active",
        "created_at": timestamp
    },
    {
        "id": "2", 
        "name": "Jane Smith",
        "email": "jane@example.com",
        "status": "active",
        "created_at": timestamp
    }
]
```

## 🔄 Using with Electron App

The Python server is fully compatible with the existing Electron application. No changes are needed in the Electron client code - it will work seamlessly with either:

- **Node.js gRPC Server**: `node ../src/server/server.js`
- **Python gRPC Server**: `python start_server.py`

Both servers implement the same gRPC interface and use the same port.

## 🧪 Testing the Server

### Using gRPC Client (Python)

```python
import grpc
import user_pb2
import user_pb2_grpc

# Create channel and stub
channel = grpc.insecure_channel('localhost:50061')
stub = user_pb2_grpc.UserServiceStub(channel)

# Get all users
response = stub.GetUsers(user_pb2.Empty())
print("Users:", response.users)

# Add a new user
new_user = user_pb2.User(
    name="Alice Johnson",
    email="alice@example.com", 
    status="active"
)
response = stub.AddUser(new_user)
print("Added user:", response)
```

### Using grpcurl (Command Line)

```bash
# List services
grpcurl -plaintext localhost:50061 list

# Get all users
grpcurl -plaintext localhost:50061 user.UserService/GetUsers

# Add a user
grpcurl -plaintext -d '{"name":"Test User","email":"test@example.com","status":"active"}' \
    localhost:50061 user.UserService/AddUser
```

## 🛠 Development

### Server Features

- **Thread Pool**: Handles concurrent requests using `ThreadPoolExecutor`
- **Error Handling**: Proper gRPC status codes (NOT_FOUND, etc.)
- **Logging**: Console output for all operations
- **Hot Reload**: Restart the script to apply code changes

### Generated Files

After running the install command, these files are automatically generated from `../shared/proto/user.proto`:

- **`proto/user_pb2.py`**: Contains message classes (`User`, `UserList`, `Empty`, etc.)
- **`proto/user_pb2_grpc.py`**: Contains service stub and servicer classes

⚠️ **Note**: 
- Generated files are created from the shared proto definition
- Don't edit the generated `*_pb2.py` files manually - they will be overwritten
- To modify the API, edit `../shared/proto/user.proto` and regenerate

## 🐍 Python Dependencies

```
grpcio==1.59.0          # Core gRPC library
grpcio-tools==1.59.0    # Tools for code generation
protobuf==4.24.4        # Protocol Buffers library
```

## ✨ Advantages of This Implementation

1. **Python Ecosystem**: Access to Python's rich data science and ML libraries
2. **Same Interface**: 100% compatible with existing Electron client
3. **Performance**: gRPC provides high-performance RPC communication
4. **Type Safety**: Protocol Buffers ensure type-safe serialization
5. **Cross-Language**: Can be used by clients in any language that supports gRPC

## 🔧 Troubleshooting

### Common Issues

1. **Import Errors**: Run `python start_server.py --install` to install dependencies
2. **Proto Files Not Found**: The script will auto-generate them, or run `python generate_protobuf.py`
3. **Port Already in Use**: Make sure the Node.js server isn't already running on port 50061
4. **Permission Errors**: On Unix systems, you might need to make scripts executable: `chmod +x start_server.py`

### Logs

The server provides detailed console output:
- User operations (add, update, delete)
- Request counts
- Error messages with context

## 🚦 Production Considerations

For production deployment:

- [ ] Use secure credentials (TLS) instead of insecure connections
- [ ] Add authentication and authorization
- [ ] Implement proper database storage instead of in-memory data
- [ ] Add comprehensive logging and monitoring
- [ ] Implement health checks and graceful shutdown
- [ ] Add rate limiting and circuit breakers
- [ ] Use environment variables for configuration
