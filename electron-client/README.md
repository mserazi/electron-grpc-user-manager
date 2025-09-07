# Electron gRPC Client

This directory contains the Electron desktop application that serves as the frontend client for the user management system.

## 📁 Directory Structure

```
electron-client/
├── README.md          # This file
├── package.json       # Electron dependencies and build scripts
├── main.js           # Main Electron process (backend)
├── preload.js        # Preload script for secure IPC
└── renderer/
    └── index.html    # Frontend UI (renderer process)
```

**Note**: Protocol buffer definitions are now located in `../shared/proto/user.proto` to ensure consistency across all components.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd electron-client
npm install
```

### 2. Start the Electron App

```bash
npm start
```

For development mode (with DevTools):

```bash
npm run dev
```

## 🔧 How It Works

The Electron app consists of three main components:

### 1. Main Process (`main.js`)
- Creates the application window
- Handles gRPC client connections
- Manages IPC communication with the renderer process

### 2. Preload Script (`preload.js`)
- Provides a secure bridge between main and renderer processes
- Exposes safe APIs to the frontend via `contextBridge`

### 3. Renderer Process (`renderer/index.html`)
- Contains the user interface
- Handles user interactions
- Communicates with the main process via exposed APIs

## 📡 gRPC Integration

The app connects to the gRPC server and provides a user-friendly interface for:

- ✅ **View Users**: Display all users in a table
- ✅ **Add User**: Create new users with name, email, and status
- ✅ **Edit User**: Modify existing user information
- ✅ **Delete User**: Remove users from the system

## 🎨 User Interface

The application features a modern, responsive design with:

- **Glass morphism effect**: Semi-transparent panels with backdrop blur
- **Gradient backgrounds**: Smooth color transitions
- **Interactive buttons**: Hover effects and smooth transitions
- **Status indicators**: Color-coded user status badges
- **Form validation**: Client-side validation with error messages
- **Real-time updates**: Automatic refresh after operations

## 🔗 Server Connection

The client expects the gRPC server to be running on:
- **Host**: `localhost`
- **Port**: `50061`
- **Protocol**: gRPC (insecure for development)

Make sure either the Node.js server or Python server is running before starting the Electron app.

## 🛠 Development

### Available Scripts

```bash
npm start      # Start the Electron app
npm run dev    # Start with developer tools open
npm run build  # Build distributables (requires electron-builder config)
```

### IPC Communication

The app uses Electron's IPC (Inter-Process Communication) for secure communication:

```javascript
// Renderer process can call:
window.electronAPI.getUsers()
window.electronAPI.addUser(userData)
window.electronAPI.updateUser(userData)
window.electronAPI.deleteUser(userId)
```

## 📦 Dependencies

### Runtime Dependencies
- `@grpc/grpc-js`: gRPC client library
- `@grpc/proto-loader`: Protocol buffer loader

### Development Dependencies
- `electron`: Cross-platform desktop framework
- `electron-builder`: Build and package tool

## 🔒 Security

The application follows Electron security best practices:

- **Context Isolation**: Enabled to prevent code injection
- **Node Integration**: Disabled in renderer for security
- **Preload Script**: Used for secure IPC communication
- **CSP Ready**: Prepared for Content Security Policy implementation

## 🚦 Production Build

To prepare for production:

1. Configure `electron-builder` in `package.json`
2. Add code signing certificates
3. Set up auto-updater
4. Implement proper error handling
5. Add telemetry and crash reporting

## 🔄 Server Compatibility

This client works with any of the following server implementations:

- **Node.js gRPC Server**: `../nodejs-server/`
- **Python gRPC Server**: `../python-server/`

All servers implement the same gRPC interface defined in `proto/user.proto`.
