#!/usr/bin/env python3
"""
Test script to verify API server can start
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try:
    from src.api.main import app
    print("✅ FastAPI app imports successfully")
    print("✅ API server ready to start")
    print("Run: cd src && uvicorn api.main:app --reload")
except Exception as e:
    print(f"❌ Error importing FastAPI app: {e}")
    sys.exit(1)