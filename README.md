# YouTube Video Downloader

**A powerful and versatile YouTube Video Downloader script** that allows you to:  
- Download full videos or specific sections (time-stamped).  
- Choose from multiple video quality options (144p to 4K).  
- Save videos with custom file names directly to your system.

This script leverages the robust `yt-dlp` tool for downloading videos from YouTube and other platforms.

---

## ✨ Features

✅ **Download Options**: Full video or specific time segments (start and end).  
✅ **Quality Selector**: Choose from 144p, 360p, 720p, 1080p, 2K, 4K, or best available (default).  
✅ **Custom File Naming**: Save with user-defined names (auto-fix extension issues).  
✅ **Lightweight CLI Interface**: Easy and intuitive command-line experience.  

---

## 🚀 Installation

1. **Download the Script**  
   Use `curl` to download the script to your system:  
   ```bash
   curl -O https://github.com/DevlopRishi/YouTube-Downloader/raw/main/ytd.sh
   ```

2. **Make the Script Executable**  
   Grant execution permissions:  
   ```bash
   chmod +x ytd.sh
   ```

3. **Run the Script**  
   Execute the script from your terminal:  
   ```bash
   ./ytd.sh
   ```

---

## 🛠️ Usage

1. **Run the Script**  
   Start the script by entering:  
   ```bash
   ./ytd.sh
   ```

2. **Follow the Prompts**  
   - **Enter the YouTube Video URL**  
     Paste the URL of the desired video.  

   - **Choose Download Mode**  
     - Download the full video.  
     - Download a specific segment (provide start and end times in `HH:MM:SS` format).  

   - **Select Video Quality**  
     Choose from the options provided:  
     ```bash
     1. 144p  
     2. 360p  
     3. 720p  
     4. 1080p  
     5. 1440p (2K)  
     6. 2160p (4K)  
     7. Best Available (Default)  
     ```

   - **Specify File Name**  
     Enter a custom name for the downloaded file (without the extension).  

3. **Video Downloaded**  
   The video will be saved in your system’s `Downloads` folder or a user-specified location.  

---

## 📦 Requirements

- **yt-dlp**: Automatically installed by the script if not already present.  
- **Python**: Installed automatically by the script if required.  

---

## 🛠️ Troubleshooting

**"Permission Denied" Error**  
Ensure the script is executable:  
```bash
chmod +x ytd.sh
```

**Storage Issues**  
Ensure the `Downloads` folder exists and is accessible:  
```bash
mkdir -p ~/Downloads
```

**Dependencies Update**  
Keep your system updated to avoid compatibility issues:  
```bash
sudo apt update && sudo apt upgrade -y
```
```bash
sudo pacman -Sy 
sudo pacman -Syu
```