# Electron gRPC User Manager

A modern desktop application for user management built with Electron and gRPC. This project demonstrates microservices architecture with multiple backend implementations and a desktop frontend.

## 🏗️ Project Architecture

```
electron-grpc-user-manager/
├── shared/                   # 📋 Shared protocol definitions
│   └── proto/
│       └── user.proto       # Single source of truth for gRPC service
├── electron-client/          # 🖥️ Electron desktop application
│   ├── main.js               # Main Electron process
│   ├── preload.js           # Secure IPC bridge
│   └── renderer/            # Frontend UI
├── nodejs-server/           # 🟢 Node.js gRPC server
│   └── server.js           # gRPC server implementation
├── python-server/          # 🐍 Python gRPC server
│   ├── server.py          # gRPC server implementation
│   └── proto/             # Generated protobuf files (auto-created)
└── README.md              # This file
```

## ✨ Features

- **🖥️ Cross-Platform Desktop App**: Built with Electron for Windows, macOS, and Linux
- **⚡ High-Performance gRPC**: Binary serialization with HTTP/2 transport
- **🔄 Multiple Server Options**: Choose between Node.js or Python backend
- **🎨 Modern UI**: Glass morphism design with smooth animations
- **🔒 Secure Architecture**: Context isolation and secure IPC communication
- **📊 Real-Time Updates**: Automatic UI refresh after operations

## 🚀 Quick Start

### 1. Choose Your Server

#### Option A: Node.js gRPC Server
```bash
cd nodejs-server
npm install
npm start
```

#### Option B: Python gRPC Server
```bash
cd python-server
python start_server.py --install  # First time only
python start_server.py
```

### 2. Start the Electron Client
```bash
cd electron-client
npm install
npm start
```

## 📡 gRPC API

All servers implement the same `UserService` interface defined in `shared/proto/user.proto`:

| Method | Description | Request | Response |
|--------|-------------|---------|----------|
| `GetUsers` | Get all users | `Empty` | `UserList` |
| `AddUser` | Create new user | `User` | `User` |
| `UpdateUser` | Update existing user | `User` | `User` |
| `DeleteUser` | Delete user by ID | `UserRequest` | `Empty` |

### User Schema
```protobuf
message User {
  string id = 1;
  string name = 2;
  string email = 3;
  string status = 4;
  int64 created_at = 5;
}
```

### 🔄 Single Source of Truth
All components reference the same protocol definition from `shared/proto/user.proto`, ensuring consistency across the entire system. The Python server generates its protobuf files from this shared definition.

## 🔧 Development

### Component Documentation

Each component has its own detailed README:

- **[Shared Protocols](shared/README.md)**: Protocol buffer definitions and API documentation
- **[Electron Client](electron-client/README.md)**: Desktop application setup and development
- **[Node.js Server](nodejs-server/README.md)**: Node.js gRPC server implementation
- **[Python Server](python-server/README.md)**: Python gRPC server implementation

### Server Switching

You can run any server implementation - the Electron client works with all of them:

```bash
# Node.js Server (Port 50061)
cd nodejs-server && npm start

# Python Server (Port 50061)  
cd python-server && python start_server.py

# Electron Client
cd electron-client && npm start
```

## 🛠️ Technology Stack

### Frontend (Electron Client)
- **Electron**: Cross-platform desktop framework
- **HTML/CSS/JavaScript**: Modern web technologies
- **gRPC-JS**: gRPC client library for Node.js

### Backend Options

#### Node.js Server
- **Node.js**: JavaScript runtime
- **@grpc/grpc-js**: gRPC implementation
- **UUID**: Unique identifier generation

#### Python Server
- **Python 3.7+**: Programming language
- **grpcio**: Python gRPC library
- **protobuf**: Protocol buffer support

## 📦 Installation & Setup

### Prerequisites
- **Node.js 16+** (for Electron client and Node.js server)
- **Python 3.7+** (for Python server option)
- **npm** or **yarn** package manager

### Full Setup
```bash
# Clone the repository
git clone git@github.com:mserazi/electron-grpc-user-manager.git
cd electron-grpc-user-manager

# Setup Electron Client
cd electron-client
npm install
cd ..

# Setup Node.js Server (Optional)
cd nodejs-server
npm install
cd ..

# Setup Python Server (Optional)
cd python-server
python start_server.py --install
cd ..
```

## 🚦 Production Deployment

### Electron App
- Use `electron-builder` for packaging
- Add code signing certificates
- Implement auto-updater
- Configure CSP and security policies

### Servers
- Use TLS/SSL for gRPC connections
- Add authentication and authorization
- Implement proper database storage
- Add monitoring and logging
- Use process managers (PM2, systemd)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎯 Use Cases

- **Enterprise User Management**: Employee directory and user administration
- **Customer Database**: Client information management system
- **Educational Systems**: Student and faculty management
- **Microservices Demo**: Example of gRPC-based architecture