const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

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

// Create gRPC client
const client = new userProto.UserService('localhost:50051', grpc.credentials.createInsecure());

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1000,
    height: 700,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    }
  });

  mainWindow.loadFile('renderer/index.html');
  
  if (process.argv.includes('--dev')) {
    mainWindow.webContents.openDevTools();
  }
}

// IPC handlers for gRPC calls
ipcMain.handle('get-users', async () => {
  return new Promise((resolve, reject) => {
    client.getUsers({}, (error, response) => {
      if (error) {
        console.error('Error getting users:', error);
        reject(error);
      } else {
        resolve(response.users);
      }
    });
  });
});

ipcMain.handle('add-user', async (event, userData) => {
  return new Promise((resolve, reject) => {
    client.addUser(userData, (error, response) => {
      if (error) {
        console.error('Error adding user:', error);
        reject(error);
      } else {
        resolve(response);
      }
    });
  });
});

ipcMain.handle('update-user', async (event, userData) => {
  return new Promise((resolve, reject) => {
    client.updateUser(userData, (error, response) => {
      if (error) {
        console.error('Error updating user:', error);
        reject(error);
      } else {
        resolve(response);
      }
    });
  });
});

ipcMain.handle('delete-user', async (event, userId) => {
  return new Promise((resolve, reject) => {
    client.deleteUser({ id: userId }, (error, response) => {
      if (error) {
        console.error('Error deleting user:', error);
        reject(error);
      } else {
        resolve(response);
      }
    });
  });
});

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
