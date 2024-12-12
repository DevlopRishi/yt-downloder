# YouTube Section Downloader

## Features
- Download specific sections of YouTube videos
- Web interface for easy use
- Supports trimming videos to desired time range

## Prerequisites
- Python 3.7+
- FFmpeg installed on your system

## Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/DevlopRishi/yt-downloder/
cd youtube-section-downloader
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Install FFmpeg
- Windows: Download from FFmpeg official website
- macOS: `brew install ffmpeg`
- Linux: `sudo apt-get install ffmpeg`

5. Run the application
```bash
python app.py
```

6. Open a web browser and navigate to `http://localhost:5000`

## Usage
1. Paste YouTube video URL
2. Enter start and end times (in seconds)
3. Click "Download Video Section"
4. Download the trimmed video

## Notes
- Requires stable internet connection
- Some YouTube videos may have download restrictions
