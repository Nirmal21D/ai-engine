"""
Quick test to verify server can be imported and basic startup works.
Run this before deployment to catch import errors.
"""
import sys
from pathlib import Path

# Add project root
ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

print("=" * 60)
print("Testing Server Import and Basic Setup")
print("=" * 60)

try:
    print("1. Loading configuration...")
    from config import CONFIG
    print(f"   ✓ Config loaded")
    print(f"   - MongoDB: {CONFIG['mongo_uri'][:20]}...")
    print(f"   - Ollama: {CONFIG['ollama_host']}")
    print(f"   - Model: {CONFIG['llm_model']}")
    
    print("\n2. Importing FastAPI app...")
    from server.main import app
    print("   ✓ FastAPI app imported successfully")
    
    print("\n3. Checking routes...")
    routes = [route.path for route in app.routes]
    print(f"   ✓ Found {len(routes)} routes")
    print(f"   - Health endpoint: {'/health' in routes}")
    print(f"   - Chat endpoint: {any('/chat' in r for r in routes)}")
    
    print("\n4. Test passed! Server should be able to start.")
    print("=" * 60)
    sys.exit(0)
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    print("\n" + "=" * 60)
    print("Fix the above error before deploying!")
    print("=" * 60)
    sys.exit(1)
