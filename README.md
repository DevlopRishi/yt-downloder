# YouTube Video Downloader

A versatile YouTube Video Downloader script that allows you to:

- Download full videos or specific sections (time-stamped).
- Choose from multiple video quality options (144p to 4K).
- Save videos with custom file names directly to your system.

This script uses yt-dlp, a powerful tool for downloading videos from YouTube and other platforms.


---

## Features

✅ Download full videos or specific sections.
✅ Quality selector from 144p to 4K (default: Best).
✅ Save videos with custom file names (with extension bug fixed).
✅ Lightweight and easy-to-use CLI interface.


---

## Installation

1. Clone or download the script:

```curl -O https://github.com/DevlopRishi/YouTube-Downloader/raw/main/ytd.sh```


2. Make the script executable:

```chmod +x ytd.sh```


3. Run the script:

```./ytd.sh```




---

## Usage

1. Run the script:

```./ytd.sh```


2. Follow the prompts:

- Enter the YouTube video URL.

- Choose whether to download the full video or specify start and end times (format: HH:MM:SS).

- Select the video quality:

```1. 144p
2. 360p
3. 720p
4. 1080p
5. 1440p (2K)
6. 2160p (4K)
7. Best (Default)```

Provide a file name without extension.

3. The video will be saved in the Downloads folder (or equivalent default storage on your system).

Requirements

yt-dlp: The script installs this automatically if not already installed.

Python: Installed automatically by the script.

Troubleshooting

Common Issues:

"Permission Denied":

Ensure the script is executable:

```chmod +x ytd.sh```

Storage Setup Fails:

Manually ensure the necessary folders are accessible:

```mkdir -p ~/Downloads```


Dependencies:

Ensure your environment is updated:

```sudo apt update && sudo apt upgrade -y```