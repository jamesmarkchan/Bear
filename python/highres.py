import requests
import json
from datetime import datetime
import os

API_PORT = 30010 # 30010 is default Unreal Remote Control API port
UNREAL_API_URL = f"http://127.0.0.1:{API_PORT}/remote/object/call"

def trigger_unreal_screenshot():

    # Determine Save Directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir) 
    save_dir = os.path.join(project_root, "Saved", "Screenshots").replace("\\", "/")
    # Create directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Generate Timestamped Filename
    timestamp = datetime.now().strftime("%m%d-%H%M%S")
    filename = f"{timestamp}_capture.png"
    
    # Use forward slashes for Unreal console commands
    save_path = os.path.join(save_dir, filename).replace("\\", "/")

    # Prepare the Payload
    # Note: options for HighResShot: are 1920x1080, 1, 2
    # Note: access='READ_ACCESS' is sometimes required depending on engine version
    payload = {
        "objectPath": "/Script/Engine.Default__KismetSystemLibrary",
        "functionName": "ExecuteConsoleCommand",
        "parameters": {
            "Command": f'HighResShot 1 filename="{save_path}"',
            #note: omission of filename param generates capture in `Saved/Screenshots/WindowsEditor`
            #"Command": f'HighResShot 1',
            "SpecificPlayer": None
        },
        "generateTransaction": False
    }

    try:
        response = requests.put(UNREAL_API_URL, json=payload, timeout=5)
        
        if response.status_code == 200:
            print("--- Success ---")
            print(f"Command sent to Unreal Engine.")
            print(f"File should appear at: {save_path}")
            return save_path
        elif response.status_code == 404:
            print(f"Error 404: resource not found.")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None
            
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

if __name__ == "__main__":
    trigger_unreal_screenshot()