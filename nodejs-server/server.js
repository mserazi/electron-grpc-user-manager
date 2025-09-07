const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const path = require('path');
const { v4: uuidv4 } = require('uuid');

// Load the protobuf
const PROTO_PATH = path.join(__dirname, '..', 'shared', 'proto', 'user.proto');
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true
});

const userProto = grpc.loadPackageDefinition(packageDefinition).user;

// In-memory user storage
let users = [
  {
    id: '1',
    name: 'John Doe',
    email: 'john@example.com',
    status: 'active',
    created_at: Date.now()
  },
  {
    id: '2',
    name: 'Jane Smith',
    email: 'jane@example.com',
    status: 'active',
    created_at: Date.now()
  }
];

// Service implementations
const userService = {
  getUsers: (call, callback) => {
    console.log('GetUsers called');
    callback(null, { users });
  },

  addUser: (call, callback) => {
    const newUser = {
      id: uuidv4(),
      name: call.request.name,
      email: call.request.email,
      status: call.request.status || 'active',
      created_at: Date.now()
    };
    
    users.push(newUser);
    console.log('User added:', newUser);
    callback(null, newUser);
  },

  updateUser: (call, callback) => {
    const userIndex = users.findIndex(u => u.id === call.request.id);
    
    if (userIndex === -1) {
      return callback({
        code: grpc.status.NOT_FOUND,
        details: 'User not found'
      });
    }

    users[userIndex] = {
      ...users[userIndex],
      name: call.request.name || users[userIndex].name,
      email: call.request.email || users[userIndex].email,
      status: call.request.status || users[userIndex].status
    };

    console.log('User updated:', users[userIndex]);
    callback(null, users[userIndex]);
  },

  deleteUser: (call, callback) => {
    const userIndex = users.findIndex(u => u.id === call.request.id);
    
    if (userIndex === -1) {
      return callback({
        code: grpc.status.NOT_FOUND,
        details: 'User not found'
      });
    }

    users.splice(userIndex, 1);
    console.log('User deleted:', call.request.id);
    callback(null, {});
  }
};

// Create and start the server
const server = new grpc.Server();
server.addService(userProto.UserService.service, userService);

const PORT = '50051';
server.bindAsync(`0.0.0.0:${PORT}`, grpc.ServerCredentials.createInsecure(), (err, port) => {
  if (err) {
    console.error('Failed to start server:', err);
    return;
  }
  
  console.log(`Node.js gRPC server running on port ${port}`);
  server.start();
});
