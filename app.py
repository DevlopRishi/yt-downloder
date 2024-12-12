# app.py
import os
import uuid
from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS
from pytube import YouTube
from moviepy.editor import VideoFileClip

app = Flask(__name__)
CORS(app)

# Ensure download directory exists
DOWNLOAD_DIR = os.path.join(os.getcwd(), 'downloads')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_video_section(url, start_time, end_time):
    """
    Download and trim a section of a YouTube video
    
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
        
        # Trim video using moviepy
        with VideoFileClip(original_filepath) as clip:
            trimmed_clip = clip.subclip(start_time, end_time)
            trimmed_clip.write_videofile(trimmed_filepath, codec='libx264')
        
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

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    """Handle video download request"""
    url = request.form.get('url')
    start_time = float(request.form.get('start_time', 0))
    end_time = float(request.form.get('end_time', 0))
    
    result = download_video_section(url, start_time, end_time)
    
    if result['success']:
        return jsonify(result)
    else:
        return jsonify(result), 400

@app.route('/get_video/<filename>')
def get_video(filename):
    """Serve the downloaded video file"""
    return send_file(os.path.join(DOWNLOAD_DIR, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)