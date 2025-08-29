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
rate = rospy.Rate(10)
x=0
# Initialize pygame mixer once
pygame.mixer.init()

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
        tts = gTTS(text=text, lang=lang)
        tts.write_to_fp(mp3_fo)
        mp3_fo.seek(0)

        # Analyze audio and prepare angles for visualization
        # angles = audio_parser(mp3_fo)

        # Playback audio from memory and visualize dynamically
        mp3_fo.seek(0)

        pygame.mixer.music.load(mp3_fo, 'mp3')
        pygame.mixer.music.play()
        # Real-time visualization during playback
        #visualize_angles(angles, mp3_fo)

    except Exception as e:
        print(f"Error: {str(e)}")

tts_speak("hello world i am veronica")
