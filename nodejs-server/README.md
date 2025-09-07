# Node.js gRPC Server

This directory contains the Node.js gRPC server implementation for the user management system.

## 📁 Directory Structure

```
nodejs-server/
├── README.md          # This file
├── package.json       # Node.js dependencies and scripts
├── server.js         # Main gRPC server implementation
└── .gitignore
```

**Protocol Definitions**: Uses `../shared/proto/user.proto` for consistency across all components.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd nodejs-server
npm install
```

### 2. Start the Server

```bash
npm start
```

Or for development with auto-restart:

```bash
npm run dev
```

The server will start on `localhost:50061`.

## 📡 gRPC Service

The server implements the `UserService` with the following methods:

| Method | Description | Request | Response |
|--------|-------------|---------|----------|
| `GetUsers` | Get all users | `Empty` | `UserList` |
| `AddUser` | Create a new user | `User` | `User` |
| `UpdateUser` | Update an existing user | `User` | `User` |
| `DeleteUser` | Delete a user by ID | `UserRequest` | `Empty` |

## 💾 Data Storage

The server uses in-memory storage with sample data for demonstration purposes. In production, you would integrate with a proper database.

## 🔧 Configuration

- **Port**: 50061 (configurable via `PORT` variable in `server.js`)
- **Protocol**: gRPC over HTTP/2
- **Credentials**: Insecure (for development)

## 🧪 Testing

You can test the server using:

### grpcurl
```bash
# List services
grpcurl -plaintext localhost:50061 list

# Get all users
grpcurl -plaintext localhost:50061 user.UserService/GetUsers
```

### Node.js Client
```javascript
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

// Load proto and create client
const packageDefinition = protoLoader.loadSync('proto/user.proto');
const userProto = grpc.loadPackageDefinition(packageDefinition).user;
const client = new userProto.UserService('localhost:50061', grpc.credentials.createInsecure());

// Get users
client.getUsers({}, (error, response) => {
  console.log('Users:', response.users);
});
```

## 📦 Dependencies

- `@grpc/grpc-js`: Core gRPC library for Node.js
- `@grpc/proto-loader`: Loads .proto files at runtime
- `uuid`: For generating unique user IDs

## 🚦 Production Considerations

For production deployment:

- [ ] Use secure credentials (TLS)
- [ ] Add authentication and authorization
- [ ] Integrate with a database (MongoDB, PostgreSQL, etc.)
- [ ] Add comprehensive logging
- [ ] Implement health checks
- [ ] Add rate limiting
- [ ] Use environment variables for configuration
- [ ] Add input validation and sanitization
