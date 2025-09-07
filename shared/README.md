# Shared Protocol Definitions

This directory contains the shared Protocol Buffer definitions used by all components in the project.

## 📁 Directory Structure

```
shared/
└── proto/
    └── user.proto    # Single source of truth for gRPC service definition
```

## 🎯 Purpose

This directory ensures that all components (Electron client, Node.js server, Python server) use the exact same gRPC service definition, preventing inconsistencies and compatibility issues.

## 📡 Service Definition

The `user.proto` file defines the `UserService` with the following methods:

```protobuf
service UserService {
  rpc GetUsers(Empty) returns (UserList);
  rpc AddUser(User) returns (User);
  rpc UpdateUser(User) returns (User);
  rpc DeleteUser(UserRequest) returns (Empty);
}
```

## 🔄 Usage by Components

### Electron Client
- References: `../shared/proto/user.proto`
- Uses: `@grpc/proto-loader` to load the proto file at runtime

### Node.js Server  
- References: `../shared/proto/user.proto`
- Uses: `@grpc/proto-loader` to load the proto file at runtime

### Python Server
- References: `../shared/proto/user.proto` 
- Generates: `proto/user_pb2.py` and `proto/user_pb2_grpc.py` in its own directory
- Process: Reads from shared proto, generates code locally

## 🛠 Modifying the Protocol

When you need to modify the gRPC service:

1. **Edit ONLY** the file in `shared/proto/user.proto`
2. **Regenerate Python files**: `cd python-server && python generate_protobuf.py`
3. **Restart all services** to pick up the changes

⚠️ **Important**: Never edit proto files in individual component directories - they are either removed or generated files.

## 🎨 Benefits of This Structure

- ✅ **Single Source of Truth**: One proto file for all components
- ✅ **Consistency**: All components always use the same interface
- ✅ **Version Control**: Easy to track API changes
- ✅ **Maintenance**: Update once, affects all components
- ✅ **Documentation**: Clear location for API documentation
