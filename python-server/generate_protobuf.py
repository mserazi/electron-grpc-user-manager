#!/usr/bin/env python3
"""
Script to generate Python gRPC protobuf files from the shared user.proto file.

This script reads from ../shared/proto/user.proto (single source of truth)
and generates user_pb2.py and user_pb2_grpc.py in the local proto/ directory.
"""

import subprocess
import sys
import os

def generate_protobuf_files():
    """Generate Python protobuf files from the .proto file."""
    print("Generating Python protobuf files...")
    
    # Paths
    current_dir = os.path.dirname(__file__)
    proto_dir = os.path.join(current_dir, "..", "shared", "proto")
    proto_file = os.path.join(proto_dir, "user.proto")
    output_dir = os.path.join(current_dir, "proto")
    
    # Check if proto file exists
    if not os.path.exists(proto_file):
        print(f"❌ Proto file not found: {proto_file}")
        return False
    
    try:
        # Generate Python files using grpc_tools.protoc
        cmd = [
            sys.executable, "-m", "grpc_tools.protoc",
            f"--proto_path={proto_dir}",
            f"--python_out={output_dir}",
            f"--grpc_python_out={output_dir}",
            proto_file
        ]
        
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Protobuf files generated successfully!")
            print(f"Generated files in: {output_dir}")
            print("- user_pb2.py")
            print("- user_pb2_grpc.py")
            return True
        else:
            print(f"❌ Error generating protobuf files:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Exception occurred: {e}")
        return False

if __name__ == "__main__":
    generate_protobuf_files()
