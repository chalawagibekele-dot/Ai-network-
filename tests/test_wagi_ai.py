"""
WAGI AI - Unit Tests
Tests for core AI engine functionality
"""

import sys
import os
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from src.main import WAGIAICore


class TestWAGIAICore:
    """Test suite for WAGI AI core functionality"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.ai = WAGIAICore()
    
    def test_initialization(self):
        """Test AI core initialization"""
        assert self.ai.name == "WAGI AI"
        assert self.ai.version == "1.0.0"
        assert self.ai.status == "initialized"
    
    def test_initialize_method(self, capsys):
        """Test initialize method"""
        self.ai.initialize()
        assert self.ai.status == "ready"
        captured = capsys.readouterr()
        assert "WAGI AI" in captured.out
    
    def test_process_input(self):
        """Test input processing"""
        test_input = "Hello WAGI AI"
        result = self.ai.process_input(test_input)
        assert "WAGI AI Processing" in result
        assert test_input in result
    
    def test_connect_external_api(self, capsys):
        """Test external API connection"""
        api_name = "TestAPI"
        result = self.ai.connect_external_api(api_name)
        assert result is True


class TestWAGIAIIntegration:
    """Integration tests for WAGI AI"""
    
    def test_full_workflow(self):
        """Test complete workflow"""
        ai = WAGIAICore()
        
        # Initialize
        ai.initialize()
        assert ai.status == "ready"
        
        # Process input
        response = ai.process_input("test input")
        assert response is not None
        
        # Connect to API
        api_connected = ai.connect_external_api("TestAPI")
        assert api_connected is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
