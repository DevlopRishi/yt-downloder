import os
import uuid
from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS
from pytube import YouTube
import cv2

app = Flask(__name__)
CORS(app)

# Ensure download directory exists
DOWNLOAD_DIR = os.path.join(os.getcwd(), 'downloads')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_video_section(url, start_time, end_time):
    """
    Download and trim a section of a YouTube video using OpenCV
    
    Args:
    url (str): YouTube video URL
    start_time (float): Start time of the section in seconds
    end_time (float): End time of the section in seconds
    
    Returns:
    dict: Download result information
    """
    try:
        # Generate a unique identifier for this download
        unique_id = str(uuid.uuid4())
        
        # Download the video
        yt = YouTube(url)
        
        # Validate time inputs
        if start_time < 0 or end_time > yt.length or start_time >= end_time:
            return {
                'success': False, 
                'error': 'Invalid start or end time'
            }
        
        # Get the highest resolution progressive stream
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        
        # Generate filenames
        original_filename = f'{unique_id}_full.mp4'
        trimmed_filename = f'{unique_id}_section.mp4'
        original_filepath = os.path.join(DOWNLOAD_DIR, original_filename)
        trimmed_filepath = os.path.join(DOWNLOAD_DIR, trimmed_filename)
        
        # Download video
        video.download(DOWNLOAD_DIR, filename=original_filename)
        
        # Open the video
        cap = cv2.VideoCapture(original_filepath)
        
        # Get video properties
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # Set start and end frames
        start_frame = int(start_time * fps)
        end_frame = int(end_time * fps)
        
        # Initialize video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(trimmed_filepath, fourcc, fps, (width, height))
        
        # Set the starting position
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        
        # Write frames
        current_frame = start_frame
        while current_frame < end_frame:
            ret, frame = cap.read()
            if not ret:
                break
            
            out.write(frame)
            current_frame += 1
        
        # Release resources
        cap.release()
        out.release()
        
        # Remove the full video to save space
        os.remove(original_filepath)
        
        return {
            'success': True,
            'filename': trimmed_filename,
            'video_title': yt.title,
            'video_length': yt.length
        }
    
    except Exception as e:
        return {
            'success': False, 
            'error': str(e)
        }

# Rest of the Flask app remains the same as in the previous version
# (Keep the existing routes from the previous app.py)

if __name__ == '__main__':
    app.run(debug=True)