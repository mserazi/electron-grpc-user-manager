#!/usr/bin/env python3
"""
Startup script for the Python gRPC server
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required Python packages"""
    print("Installing Python gRPC dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def generate_protobuf():
    """Generate Python protobuf files"""
    print("Generating Python protobuf files...")
    try:
        # Import generate_protobuf and run it
        import generate_protobuf
        return generate_protobuf.generate_protobuf_files()
    except Exception as e:
        print(f"❌ Error generating protobuf files: {e}")
        return False

def start_server():
    """Start the gRPC server"""
    print("Starting Python gRPC server...")
    try:
        # Start the server from current directory
        subprocess.run([sys.executable, "server.py"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    print("🚀 Python gRPC Server Setup")
    print("=" * 40)
    
    # Check if we should install dependencies
    if len(sys.argv) > 1 and sys.argv[1] == "--install":
        if install_dependencies():
            if generate_protobuf():
                print("\n✅ Setup complete!")
                print("Now you can start the server with:")
                print("python start_server.py")
            else:
                print("❌ Setup failed during protobuf generation")
        else:
            print("❌ Setup failed during dependency installation")
        sys.exit(0)
    
    # Check if requirements.txt exists
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt not found!")
        sys.exit(1)
    
    # Check if dependencies are installed
    try:
        import grpc
        import google.protobuf
        print("✅ gRPC dependencies found")
    except ImportError:
        print("❌ gRPC dependencies not installed!")
        print("Run: python start_server.py --install")
        sys.exit(1)
    
    # Check if protobuf files exist
    proto_dir = "proto"
    if not (os.path.exists(os.path.join(proto_dir, "user_pb2.py")) and 
            os.path.exists(os.path.join(proto_dir, "user_pb2_grpc.py"))):
        print("❌ Protobuf files not found! Generating them from shared proto...")
        if not generate_protobuf():
            print("❌ Failed to generate protobuf files")
            sys.exit(1)
    else:
        print("✅ Protobuf files found")
    
    start_server()
