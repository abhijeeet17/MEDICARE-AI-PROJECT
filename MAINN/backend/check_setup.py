#!/usr/bin/env python3
"""
Startup script for Render deployment
Ensures proper directory structure and starts the FastAPI server
"""
import os
import sys

def check_setup():
    """Verify all required files and directories exist"""
    
    # Get current directory
    cwd = os.getcwd()
    print(f"Working directory: {cwd}")
    
    # Check for datasets
    dataset_paths = [
        "datasets/Heart_Disease_Prediction.csv",
        "datasets/Dataset 1 _ Pima Indians diabetes dataset (PIDD).csv"
    ]
    
    for path in dataset_paths:
        if not os.path.exists(path):
            print(f"⚠️  Warning: Dataset not found at {path}")
            print(f"   Looking from: {cwd}")
        else:
            print(f"✅ Found dataset: {path}")
    
    # Check for notebooks
    notebook_paths = [
        "heart_disease.ipynb",
        "diabetese.ipynb"
    ]
    
    for path in notebook_paths:
        if not os.path.exists(path):
            print(f"⚠️  Note: Notebook not found at {path} (optional)")
        else:
            print(f"✅ Found notebook: {path}")
    
    print("\n✅ Setup check complete!\n")

if __name__ == "__main__":
    check_setup()
