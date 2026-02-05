#! /usr/bin/env python3

import requests
import rospy
from std_msgs.msg import String
import speech_recognition as sr
import warnings
warnings.filterwarnings("ignore")

#create session variable 
url = "http://localhost:8000/apps/veronica_agent/users/forusone/sessions/session_10"
payload = {}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, json=payload, headers=headers)
# response.raise_for_status()  # raise exception if HTTP error

def find_key_in_dict(d, key):
    """
    Recursively search for a key in nested dictionaries or lists and return its value.
    Returns first found value or None if not found.
    """
    if isinstance(d, dict):
        if key in d:
            return d[key]
        for v in d.values():
            result = find_key_in_dict(v, key)
            if result is not None:
                return result
    elif isinstance(d, list):
        for item in d:
            result = find_key_in_dict(item, key)
            if result is not None:
                return result
    return None

# def get_adk_response(querry : str) -> str:
#     url = "http://localhost:8000/run"
#     payload = {
#         "app_name": "veronica_agent",
#         "user_id": "forusone",
#         "session_id": "session_10",
#         "new_message": {
#             "role": "user",
#             "parts": [{"text": querry}]
#         },
#         "streaming": False
#     }
    
#     headers = {
#         'Content-Type': 'application/json'
#     }
    
#     response = requests.post(url, json=payload, headers=headers)
#     # response.raise_for_status()  # raise exception if HTTP error
    
#     data = response.json()
    
#     # Example expected response extraction:
#     # Assuming response contains keys like "messages" or "response" with the final message
#     # But you gave only partial response, so assuming response has 'role', 'parts'...
#     # print(data)
#     final_output=find_key_in_dict(data, 'final_output')
#     print(final_output)
#     # Extract the text parts to form human readable answer
#     if final_output:
#         return final_output
#     else:
#         return "No valid response text found."

import requests

def get_adk_response(querry: str) -> str:
    url = "http://localhost:8000/run"
    payload = {
        "app_name": "veronica_agent",
        "user_id": "forusone",
        "session_id": "session_10",
        "new_message": {
            "role": "user",
            "parts": [{"text": querry}]
        },
        "streaming": False
    }

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=5)

        # If server gives bad HTTP code
        if response.status_code != 200:
            print(f"[ADK ERROR] HTTP {response.status_code}: {response.text}")
            return "..."

        # Try to parse JSON safely
        try:
            data = response.json()
        except Exception as e:
            print(f"[ADK ERROR] Invalid JSON response: {e}")
            return "..."

        # Try to extract model output
        try:
            final_output = find_key_in_dict(data, 'final_output')
            if final_output:
                return final_output
            else:
                print("[ADK ERROR] 'final_output' not found in response")
                return "..."
        except Exception as e:
            print(f"[ADK ERROR] Parsing issue: {e}")
            return "..."

    except requests.exceptions.RequestException as e:
        print(f"[ADK ERROR] Request failed: {e}")
        return "..."


def takecommand():
    r= sr.Recognizer()
    r.energy_threshold = 2000
    try:
        with sr.Microphone() as source:
             print("listening...")            
             audio = r.listen(source,timeout=1.0)
             print("recognizing.....")
             query = r.recognize_google(audio, language="en")
             print(f"user :  {query}")
    except Exception:
        print("waiting....")
        query=None
    return query 

def main():
    global latest1, latest2

    rospy.init_node('adk_server', anonymous=True)
    pub = rospy.Publisher('adk_server', String, queue_size=1)

    rate = rospy.Rate(200)  # 20 Hz loop
    i = 0
    while not rospy.is_shutdown():
        # Combine the two strings
        # querry = input("\033[33m[user]::\033[00m")
        querry = takecommand()
        if not querry:
            continue

        print("\033[33m[user]::\033[00m" + querry)
        if querry == None:
            continue
        answer = get_adk_response(querry)
        print("Agent response:\n")
        print(answer)
        response = f"{answer}"
        
        msg = String(data=response)
        pub.publish(response)
        print(f"\033[33m[agent]::\033[00m {response}")
        rate.sleep()

if __name__ == '__main__':
    main()