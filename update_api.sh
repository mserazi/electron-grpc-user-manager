#!/bin/bash

# Script to update the gRPC API across all components
# This demonstrates the workflow when you need to modify the API

echo "🔄 gRPC API Update Workflow"
echo "=========================="

echo "📝 Step 1: Edit the shared proto file"
echo "   File: shared/proto/user.proto"
echo "   This is the ONLY place to modify the API definition"

echo ""
echo "🔧 Step 2: Regenerate Python protobuf files"
echo "   Running: cd python-server && python generate_protobuf.py"
cd python-server
python generate_protobuf.py
cd ..

echo ""
echo "🔄 Step 3: Restart all services to pick up changes"
echo "   - Electron client: Reads proto at runtime"
echo "   - Node.js server: Reads proto at runtime" 
echo "   - Python server: Uses newly generated files"

echo ""
echo "✅ API update complete!"
echo ""
echo "🚀 To test the changes:"
echo "1. Start your chosen server (Node.js or Python)"
echo "2. Start the Electron client"
echo "3. Test the functionality"
