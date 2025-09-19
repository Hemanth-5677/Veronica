#!/usr/bin/python3

import sounddevice
from gtts import gTTS
from io import BytesIO
import pygame
import time
import speech_recognition as sr
import warnings
warnings.filterwarnings("ignore")
# Initialize pygame mixer once
pygame.mixer.pre_init(44100, -16, 2, 4096)  # Adjust buffer size to 4096 for smoother playback
# Initialize pygame
pygame.init()
'''

def speak(text, lang='en'):
    """Convert text to speech and play it immediately (blocks execution)"""
    try:
        # Create in-memory MP3 file
        mp3_fo = BytesIO()
        tts = gTTS(text=text, lang=lang)
        tts.write_to_fp(mp3_fo)
        mp3_fo.seek(0)  # Reset buffer position
        
        # Load and play audio
        pygame.mixer.music.load(mp3_fo, 'mp3')
        pygame.mixer.music.set_volume(2)
        pygame.mixer.music.play()
        print(f"reply : {text}")        
        # Block while audio is playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
    except Exception as e:
        print(f"Error: {str(e)}")

'''
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
        query="None"
    return query 
from gtts import gTTS
from io import BytesIO
import pygame
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
import time
import rospy 
from humanoid.msg import Coordinates
from std_msgs.msg import String

nodeName1 = 'voice_node'
topicName1= 'voice_node'

latest1=""

rospy.init_node(nodeName1, anonymous=True)
publisher1 = rospy.Publisher(topicName1,String,queue_size=1)
rate = rospy.Rate(20)
x=0
# Initialize pygame mixer once

pygame.mixer.pre_init(44100, -16, 2, 4096)  # Adjust buffer size to 4096 for smoother playback

# Initialize pygame
pygame.init()
def get_message(msg):
    global latest1
    latest1 = msg.data.strip()
    
def kernel_average(samples, kernel_size):
    """Apply kernel averaging to smooth the signal."""
    # Create a kernel for averaging
    kernel = np.ones(kernel_size) / kernel_size
    # Convolve signal with kernel using 'same' mode to maintain original length
    smoothed_samples = np.convolve(samples, kernel, mode='same')
    return smoothed_samples

# def speak(text, lang='en'):
#     """Generate speech and visualize angles dynamically during playback."""
#     try:
#         # Generate speech audio in-memory
#         mp3_fo = BytesIO()
#         mp3_f1 = BytesIO()
#         tts = gTTS(text=text, lang=lang)
#         tts.write_to_fp(mp3_fo)
#         tts.write_to_fp(mp3_f1)
#         mp3_f1.seek(0)
#         mp3_fo.seek(0)

#         # Analyze audio and prepare angles for visualization
#         angles = audio_parser(mp3_f1)

#         # Playback audio from memory and visualize dynamically
#         # mp3_f1.seek(0)
#         pygame.mixer.music.load(mp3_fo,'mp3')
#         pygame.mixer.music.play()
#         # Real-time visualization during playback
#         visualize_angles(angles, mp3_fo)
#     except Exception as e:
#         print(f"Error: {str(e)}")

# def audio_parser(audio_buffer):
#     """Parse audio and calculate smoothed angles."""
#     # Load audio from memory buffer
#     audio = AudioSegment.from_file(audio_buffer, format="mp3")

#     # Convert to numpy array and mono channel if stereo
#     samples = np.array(audio.get_array_of_samples())
#     if audio.channels == 2:
#         samples = samples[::2]
    
#     samples = samples * (samples > 0)  # Ensure positive values only

#     # Normalize samples to [-1, 1]
#     normalized_samples = samples / np.max(np.abs(samples))

#     # Apply smoothing with a kernel size of 500
#     smoothed_signal = kernel_average(normalized_samples, kernel_size=5000)

#     # Map smoothed signal to servo angles (0° to 30°)
#     angles = np.interp(smoothed_signal, [0, 0.3], [0, 40])

#     return angles

# def visualize_angles(angles, mp3_fo):
#     """Visualize angles dynamically during playback with reduced looping."""
#     for i in range(0, len(angles), 3800):
#         if not pygame.mixer.music.get_busy():
#             break  # Stop visualization if audio playback ends
#         msg= String()
#         m = f'{int(angles[i])},{int(angles[i])},{int(angles[i])}'
#         msg.data=m
#         print(m)
#         publisher1.publish(msg)
#         time.sleep(0.15) # Adjust delay for smoother visualization

import time
import numpy as np
from gtts import gTTS
from io import BytesIO
import pygame
from pydub import AudioSegment
from std_msgs.msg import String

# Assumes publisher1 is initialized ROS publisher for angle messages

def speak(text, lang='en'):
    """Generate speech and synchronize angle publishing with audio playback in real-time."""
    try:
        # Generate speech audio in-memory
        mp3_buffer = BytesIO()
        tts = gTTS(text=text, lang=lang)
        tts.write_to_fp(mp3_buffer)
        mp3_buffer.seek(0)

        # Parse audio to get angles
        angles = audio_parser(mp3_buffer)

        # Initialize pygame mixer and load audio
        pygame.mixer.init()
        mp3_buffer.seek(0)
        pygame.mixer.music.load(mp3_buffer, 'mp3')

        # Start playback
        pygame.mixer.music.play()

        # Retrieve total playback length in seconds
        audio = AudioSegment.from_file(BytesIO(mp3_buffer.getbuffer()), format='mp3')
        duration_sec = audio.duration_seconds

        total_angles = len(angles)
        start_time = time.time()

        # Loop while music is playing
        while pygame.mixer.music.get_busy():
            elapsed = time.time() - start_time
            # Map elapsed time to angle index
            idx = int((elapsed / duration_sec) * total_angles)
            if idx >= total_angles:
                break

            angle_value = int(angles[idx])
            msg = String()
            msg.data = f"{angle_value},{angle_value},{angle_value}"
            print(msg.data)
            # Publish angles
            publisher1.publish(msg)

            # Sleep shortly for smooth updates (e.g. 50ms)
            time.sleep(0.05)

        # Send final angle message at end for safety
        final_angle = int(angles[-1])
        msg = String()
        msg.data = f"{final_angle},{final_angle},{final_angle}"
        publisher1.publish(msg)

    except Exception as e:
        print(f"Error in speak_and_sync: {str(e)}")


def audio_parser(audio_buffer):
    """Parse audio and calculate smoothed angles."""
    audio = AudioSegment.from_file(audio_buffer, format="mp3")
    samples = np.array(audio.get_array_of_samples())
    if audio.channels == 2:
        samples = samples[::2]
    samples = samples * (samples > 0)  # Positive values only
    normalized_samples = samples / np.max(np.abs(samples))
    smoothed_signal = kernel_average(normalized_samples, kernel_size=5000)
    angles = np.interp(smoothed_signal, [0, 0.3], [0, 40])
    return angles


def kernel_average(signal, kernel_size=5000):
    """Simple moving average kernel for smoothing."""
    kernel = np.ones(kernel_size) / kernel_size
    return np.convolve(signal, kernel, mode='same')


def main():
    global latest1, latest2

    rospy.Subscriber('adk_server', String, get_message)
    # pub = rospy.Publisher('merger_node', String, queue_size=50)

    rate = rospy.Rate(20)  # 20 Hz loop
    i = 0
    while not rospy.is_shutdown():
        # Combine the two strings
        message = latest1
        if(latest1!=""):
            speak(latest1)
        latest1=""
        rate.sleep()

# Example usage:

# while True:
#     x = input("Enter the TTS text here :") 
#     m = f'0,0,0'
#     msg= String()
#     msg.data=m
#     publisher1.publish(msg)
#     # speak("where is my award?")
#     #speak("I am an ai powered chat bot system for medical receptionist job")
#     speak(x)

#while True:
#    y=takecommand()
#    print(y)
#    speak(y)

if __name__ == '__main__':
    main()