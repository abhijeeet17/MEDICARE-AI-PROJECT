#!/usr/bin/env python3
"""
Local testing script for MediCare Backend
Tests all endpoints before deployment
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("\n🔍 Testing Health Endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ Health check passed!")
            print(json.dumps(response.json(), indent=2))
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to backend at {BASE_URL}")
        print(f"   Make sure it's running: uvicorn main:app --reload")
        return False

def test_model_info(model_name):
    """Test model info endpoint"""
    print(f"\n🔍 Testing {model_name.title()} Model Info...")
    try:
        response = requests.get(f"{BASE_URL}/info/{model_name}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Model: {data.get('model_name', 'Unknown')}")
            print(f"   Accuracy: {data.get('accuracy', 0):.2f}%")
            return True
        else:
            print(f"❌ Failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_heart_prediction():
    """Test heart disease prediction"""
    print("\n🔍 Testing Heart Disease Prediction...")
    try:
        test_data = {
            "age": 45,
            "sex": "male",
            "cp": 2,
            "bp": 120.0,
            "chol": 200.0,
            "maxHR": 150.0
        }
        response = requests.post(
            f"{BASE_URL}/predict/heart",
            json=test_data
        )
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Prediction: {data.get('prediction', 'Unknown')}")
            print(f"   Model: {data.get('model_used', 'Unknown')}")
            return True
        else:
            print(f"❌ Failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_diabetes_prediction():
    """Test diabetes prediction"""
    print("\n🔍 Testing Diabetes Prediction...")
    try:
        test_data = {
            "pregnancies": 2.0,
            "glucose": 120.0,
            "blood_pressure": 70.0,
            "insulin": 80.0,
            "age": 30.0,
            "bmi": 25.0
        }
        response = requests.post(
            f"{BASE_URL}/predict/diabetes",
            json=test_data
        )
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Prediction: {data.get('prediction', 'Unknown')}")
            print(f"   Model: {data.get('model_used', 'Unknown')}")
            return True
        else:
            print(f"❌ Failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Run all tests"""
    print("="*60)
    print("🏥 MediCare Backend - Local Testing")
    print("="*60)
    
    # Test health first
    if not test_health():
        print("\n❌ Backend is not running or not accessible!")
        print("   Start it with: cd MAINN/backend && uvicorn main:app --reload")
        return
    
    # Test model info
    test_model_info("heart")
    test_model_info("diabetes")
    
    # Test predictions
    test_heart_prediction()
    test_diabetes_prediction()
    
    print("\n" + "="*60)
    print("✅ All tests completed!")
    print("="*60)
    print("\n🎉 If all tests passed, your backend is ready!")
    print("   Now build and test the frontend:")
    print("   cd MAINN/frontend && npm run dev\n")

if __name__ == "__main__":
    main()
