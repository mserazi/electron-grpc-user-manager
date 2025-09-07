#!/bin/bash

# Validation script to check that all components can access the shared proto file

echo "🔍 Validating Shared Proto File Access..."
echo "=" * 50

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if shared proto file exists
SHARED_PROTO="shared/proto/user.proto"
if [ -f "$SHARED_PROTO" ]; then
    echo -e "${GREEN}✅ Shared proto file exists: $SHARED_PROTO${NC}"
else
    echo -e "${RED}❌ Shared proto file missing: $SHARED_PROTO${NC}"
    exit 1
fi

# Check Electron Client
echo -e "\n${YELLOW}📱 Checking Electron Client...${NC}"
cd electron-client
ELECTRON_PROTO_PATH="../shared/proto/user.proto"
if [ -f "$ELECTRON_PROTO_PATH" ]; then
    echo -e "${GREEN}✅ Electron client can access shared proto${NC}"
else
    echo -e "${RED}❌ Electron client cannot access shared proto${NC}"
fi

# Check if package.json exists
if [ -f "package.json" ]; then
    echo -e "${GREEN}✅ Electron package.json exists${NC}"
else
    echo -e "${RED}❌ Electron package.json missing${NC}"
fi
cd ..

# Check Node.js Server
echo -e "\n${YELLOW}🟢 Checking Node.js Server...${NC}"
cd nodejs-server
NODEJS_PROTO_PATH="../shared/proto/user.proto"
if [ -f "$NODEJS_PROTO_PATH" ]; then
    echo -e "${GREEN}✅ Node.js server can access shared proto${NC}"
else
    echo -e "${RED}❌ Node.js server cannot access shared proto${NC}"
fi

# Check if package.json exists
if [ -f "package.json" ]; then
    echo -e "${GREEN}✅ Node.js package.json exists${NC}"
else
    echo -e "${RED}❌ Node.js package.json missing${NC}"
fi
cd ..

# Check Python Server
echo -e "\n${YELLOW}🐍 Checking Python Server...${NC}"
cd python-server
PYTHON_PROTO_PATH="../shared/proto/user.proto"
if [ -f "$PYTHON_PROTO_PATH" ]; then
    echo -e "${GREEN}✅ Python server can access shared proto${NC}"
else
    echo -e "${RED}❌ Python server cannot access shared proto${NC}"
fi

# Check if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo -e "${GREEN}✅ Python requirements.txt exists${NC}"
else
    echo -e "${RED}❌ Python requirements.txt missing${NC}"
fi

# Check if proto directory exists for generated files
if [ -d "proto" ]; then
    echo -e "${GREEN}✅ Python proto directory exists (for generated files)${NC}"
else
    echo -e "${YELLOW}⚠️  Python proto directory missing (will be created during setup)${NC}"
fi
cd ..

echo -e "\n${GREEN}🎉 Validation Complete!${NC}"
echo -e "\n📋 Next Steps:"
echo "1. Install dependencies in each component directory"
echo "2. For Python server, run: python start_server.py --install"
echo "3. Start your chosen server, then start the Electron client"
