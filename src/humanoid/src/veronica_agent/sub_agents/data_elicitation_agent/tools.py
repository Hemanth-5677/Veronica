import hashlib
from typing import Dict, Any
import os
import json
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, db
from typing import Dict, Any, List
import os
from dotenv import load_dotenv, find_dotenv
import firebase_admin
from firebase_admin import credentials

def initialize_firebase():
    """
    Initialize Firebase Admin SDK using environment variables loaded from a .env file.
    """
    # Find and load .env (specify path if needed)
    env_path = find_dotenv()
    if not env_path:
        raise FileNotFoundError(".env file not found. Please create one with required variables.")
    load_dotenv(env_path)

    # Debug prints (remove in production)
    print(f"Loaded .env path: {env_path}")
    cred_path = os.getenv('FIREBASE_CREDS_PATH') or './credentials.json'
    database_url = os.getenv('FIREBASE_DATABASE_URL')
    print(f"FIREBASE_CREDENTIALS_PATH: {cred_path}")
    print(f"FIREBASE_DATABASE_URL: {database_url}")

    if not cred_path or not database_url:
        raise ValueError("Environment variables FIREBASE_CREDENTIALS_PATH and FIREBASE_DATABASE_URL must be set in .env file.")

    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred, {'databaseURL': database_url})

def get_data(user_info: Dict[str, Any]) -> Dict[str, Any]:
    """
    Fetch data for user at path `user/<sha1(name+phonenumber)>` in Firebase Realtime Database.
    If data does not exist, uploads the given data by calling set_data function.

    Args:
        user_info (dict): User information dictionary; must include 'name' and 'phonenumber'.

    Returns:
        dict: Status dictionary. If data found, returns:
            {
              "status": "success",
              "data": <fetched_data>,
              "message": "Data fetched successfully."
            }
        If data not found and uploaded successfully via set_data:
            {
              "status": "success",
              "message": "Data not found. ask the user if they want to create an entry."
            }
        If required attributes missing or other failure, returns failure dictionary.

    Usage:
        response = fetch_or_create_data({"name": "Alice", "phonenumber": "1234567890", "age": 25})
    """
    required_attrs = ['name', 'phonenumber']
    for attr in required_attrs:
        if attr not in user_info:
            return {"status": "failed", "error": f"attribute '{attr}' not found. Please mention it."}

    name = user_info['name']
    phonenumber = user_info['phonenumber']

    # Compute SHA-1 hash of name+phonenumber
    path_hash = hashlib.sha1((name + phonenumber).encode('utf-8')).hexdigest()
    subpath = f"user/{path_hash}"

    ref = db.reference(subpath)
    data = ref.get()

    if data is None:
        return {"status": "success", "message": "Data not found. ask the user if they want to create an new entry?"}


    return {"status": "success", "data": data, "message": "Data fetched successfully."}

def set_data(json_data: Dict[str, Any]) -> Dict[str, str]:
    """
    Upload/overwrite JSON data at path `user/<sha1(name+phonenumber)>` in Firebase Realtime Database.

    Constructs the path by SHA-1 hashing concatenated 'name' and 'phonenumber' values.
    If required attributes are missing, returns dict with failure status and error message.
    On success, returns dict with success status and confirmation message.

    Args:
        json_data (dict): Data to upload; must include 'name' and 'phonenumber' keys.

    Returns:
        dict: Status dictionary with keys 'status' and either 'error' or 'message'.

    Usage:
        response = set_data({"name": "Alice", "phonenumber": "1234567890", "age": 25})
    """
    required_attrs = ['name', 'phonenumber']
    for attr in required_attrs:
        if attr not in json_data:
            return {"status": "failed", "error": f"attribute '{attr}' not found. Please ask the user to mention it."}

    name = json_data['name']
    phonenumber = json_data['phonenumber']

    # Compute SHA-1 hash of concatenated name and phonenumber
    concat_bytes = (name + phonenumber).encode('utf-8')
    path_hash = hashlib.sha1(concat_bytes).hexdigest()

    subpath = f"user/{path_hash}"

    ref = db.reference(subpath)
    ref.set(json_data)

    return {"status": "success", "message": "User data is stored in the database."}

def list_keys(path: str) -> List[str]:
    """
    List all keys (child node names) under the given path in Realtime Database.

    Args:
        path (str): Database path (e.g. "/users")

    Returns:
        list of str: List of keys (user IDs or child node keys)

    Usage:
        user_ids = list_keys_in_path('/users')
    """
    ref = db.reference(path)
    data = ref.get(shallow=True)  # get only keys, not full data
    if data is None:
        return []
    return list(data.keys())

def make_key(user_name:str , phone_number:str) -> str:
    concat_bytes = (user_name + phone_number).encode('utf-8')
    path_hash = hashlib.sha1(concat_bytes).hexdigest()
    return {"status":"success", "key_path":f"user/{path_hash}" , "message":"this is the path to the user's hashkey if the data is correct , uste the listing function to verify it"}

def record_data():
    return {"status":"success"}

# if __name__ == "__main__":
#     # Initialize Firebase once
#     initialize_firebase()

#     # Fetch data example
#     user_data = fetch_data_from_path('/users/userid456')
#     print("User Data:", user_data)
    
#     # Upload data example
#     upload_data_at_subpath({"name": "Bob", "age": 30 , "sensor_data":{"hr_data":[1,2,3,4,5,6,7,8]}}, '/users/userid456')
    
#     # Fetch data example
#     user_data = fetch_data_from_path('/users/userid456')
#     print("User Data:", user_data)


#     # List keys example
#     user_ids = list_keys_in_path('/users')
#     print("User IDs:", user_ids)
    