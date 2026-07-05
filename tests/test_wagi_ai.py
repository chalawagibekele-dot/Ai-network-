"""
WAGI AI - Unit Tests
Tests for core AI engine functionality
"""

import sys
import os
from pathlib import Path

# Add the project root to the Python path BEFORE importing pytest
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Change to project root directory
os.chdir(project_root)

import pytest
from src.main import WAGIAICore


class TestWAGIAICore:
    """Test suite for WAGI AI core functionality"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.ai = WAGIAICore()
    
    def test_initialization(self):
        """Test AI core initialization"""
        print("\n🧠 Testing WAGI AI initialization...")
        assert self.ai.name == "WAGI AI"
        assert self.ai.version == "1.0.0"
        assert self.ai.status == "initialized"
        print("✅ Initialization test passed")
    
    def test_initialize_method(self):
        """Test initialize method"""
        print("\n🧠 Testing initialize method...")
        self.ai.initialize()
        assert self.ai.status == "ready"
        print("✅ Initialize method test passed")
    
    def test_process_input(self):
        """Test input processing"""
        print("\n🧠 Testing input processing...")
        test_input = "Hello WAGI AI"
        result = self.ai.process_input(test_input)
        assert "WAGI AI Processing" in result
        assert test_input in result
        print(f"✅ Input processing test passed: {result}")
    
    def test_connect_external_api(self):
        """Test external API connection"""
        print("\n🧠 Testing external API connection...")
        api_name = "TestAPI"
        result = self.ai.connect_external_api(api_name)
        assert result is True
        print(f"✅ API connection test passed for {api_name}")


class TestWAGIAIIntegration:
    """Integration tests for WAGI AI"""
    
    def test_full_workflow(self):
        """Test complete workflow"""
        print("\n🧠 Testing full workflow integration...")
        ai = WAGIAICore()
        
        # Initialize
        ai.initialize()
        assert ai.status == "ready"
        print("✅ Initialization passed")
        
        # Process input
        response = ai.process_input("test input")
        assert response is not None
        print(f"✅ Processing passed: {response}")
        
        # Connect to API
        api_connected = ai.connect_external_api("TestAPI")
        assert api_connected is True
        print("✅ API connection passed")
        print("✅ Full workflow integration test passed")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
