from gtts import gTTS
from io import BytesIO
import pygame
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
import time
import rospy 
from robo_eye.msg import Coordinates
from std_msgs.msg import String

nodeName1 = 'message_publisher_2'
topicName1= 'sender'


rospy.init_node(nodeName1, anonymous=True)
publisher1 = rospy.Publisher(topicName1,String,queue_size=20)
rate = rospy.Rate(1000)
x=0
# Initialize pygame mixer once

pygame.mixer.pre_init(44100, -16, 2, 4096)  # Adjust buffer size to 4096 for smoother playback

# Initialize pygame
pygame.init()
def kernel_average(samples, kernel_size):
    """Apply kernel averaging to smooth the signal."""
    # Create a kernel for averaging
    kernel = np.ones(kernel_size) / kernel_size
    # Convolve signal with kernel using 'same' mode to maintain original length
    smoothed_samples = np.convolve(samples, kernel, mode='same')
    return smoothed_samples

def tts_speak(text, lang='en'):
    """Generate speech and visualize angles dynamically during playback."""
    try:
        # Generate speech audio in-memory
        mp3_fo = BytesIO()
        mp3_f1 = BytesIO()
        tts = gTTS(text=text, lang=lang)
        tts.write_to_fp(mp3_fo)
        tts.write_to_fp(mp3_f1)
        mp3_f1.seek(0)
        mp3_fo.seek(0)

        # Analyze audio and prepare angles for visualization
        angles = audio_parser(mp3_f1)

        # Playback audio from memory and visualize dynamically
        # mp3_f1.seek(0)
        pygame.mixer.music.load(mp3_fo,'mp3')
        pygame.mixer.music.play()
        # Real-time visualization during playback
        visualize_angles(angles, mp3_fo)
    except Exception as e:
        print(f"Error: {str(e)}")

def audio_parser(audio_buffer):
    """Parse audio and calculate smoothed angles."""
    # Load audio from memory buffer
    audio = AudioSegment.from_file(audio_buffer, format="mp3")

    # Convert to numpy array and mono channel if stereo
    samples = np.array(audio.get_array_of_samples())
    if audio.channels == 2:
        samples = samples[::2]
    
    samples = samples * (samples > 0)  # Ensure positive values only

    # Normalize samples to [-1, 1]
    normalized_samples = samples / np.max(np.abs(samples))

    # Apply smoothing with a kernel size of 500
    smoothed_signal = kernel_average(normalized_samples, kernel_size=5000)

    # Map smoothed signal to servo angles (0° to 30°)
    angles = np.interp(smoothed_signal, [0, 0.3], [0, 40])

    return angles

def visualize_angles(angles, mp3_fo):
    """Visualize angles dynamically during playback with reduced looping."""
    for i in range(0, len(angles), 3800):
        if not pygame.mixer.music.get_busy():
            break  # Stop visualization if audio playback ends
        msg= String()
        m = f'0,0,{int(angles[i])}'
        msg.data=m
        print(m)
        publisher1.publish(msg)
        time.sleep(0.15)  # Adjust delay for smoother visualization
# Example usage:
while True:
    # x = input("Enter the TTS text here :")
    m = f'0,0,0'
    msg= String()
    msg.data=m
    publisher1.publish(msg)
    speak("Hello world! My name is Veronica.")
    speak("I am an ai powered chat bot system for medical receptionist job")
#     tts_speak(x)
