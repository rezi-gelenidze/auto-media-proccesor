# AutoMediaProccesor - Python Automation Project

Automated productivity tool for Video/Image watermarking and adding music. It automatically transfers media from an Android device, processes it, and pushes the processed media back to the device. Features include adding a specified watermark text label over Image/Video, adding music to videos, and optional video compression to 720p. Configurable properties include text label size, position, color, encoding, fps, and more.

## Usage

1. On your Android device, move target Images/Videos to a gallery album named **`Transfer`**.
2. Connect your Android device to your computer using a USB cable.
3. Run `python3 process.py` and the rest will be handled automatically.

All processed Images/Videos will be in a newly created album named **`Processed`** on your Android device.

#### Process (Algorithm)

1. Transfers all media from the Android `Transfer` album to a `Transfer` directory locally on the machine.
2. Scans transferred media and organizes it separately as Images and Videos.
3. Processes Images:
   - Adds a text label (watermark) over each image.
   - Saves each Image in the `Processed/` directory locally.
4. Processes Videos:
   - Adds a text label (watermark) over each video.
   - Selects random music from the `resources/music/` folder and adds it to the video.
   - Compresses videos to 720p if `compress` is set to **True**.
   - Saves each Video in the `Processed/` directory locally.
5. Transfers processed media back to the Android device:
   - All media is transferred to the `Processed` album in the Android gallery.
6. Removes media files locally after the transfer.

## Requirements

- **Python 3**
- **MoviePy** library (`pip3 install moviepy`)
- **PIL (Python Imaging Library)** (`pip3 install pillow`)

Also listed in `requirements.txt`.

#### Other Software

- **ADB (Android Debug Bridge) Shell** - for transferring media between Android and computer.
- **ImageMagick** - Used by MoviePy for adding text over videos.

Read about installation below.

## Installation

1. Clone/download this repository and extract it on your machine.
2. Install **Python 3** if not already installed.
3. Install required packages with **pip3**:
   - `pip3 install -r requirements.txt` **or** `pip3 install pillow moviepy`
4. Install **ImageMagick** on your machine. [View detailed explanation below]
5. Download **ADB shell** on your machine. [View detailed explanation below]

## Configuration

Configure the program in the `settings.py` file. Options include:

#### ImageConfig

- `text` - Text to be written over each image **[string]**
- `text_color` - Color of the text **[string]**
- `text_stroke_fill` - Text outline color **[string]**
- `text_stroke_weight` - Text outline size **[integer]**
- `text_width_fraction` - Fraction of text width over image **[float: 0-1]**
- `text_pos` - Position of text over each image **[tuple (posX, posY)]**

#### VideoConfig

- `text` - Text to be written over each video **[string]**
- `text_pos` - Text alignment over video **[top, bottom, left, right]**
- `text_color` - Color of the text **[string]**
- `fps` - Processed video fps **[integer]**
- `threads` - Number of threads used for processing **[integer]**
- `codec` - Video codec **[string]**
- `compress` - Compresses video to 720p if True **[boolean True/False]**

#### Paths

Paths are automatically configured if you follow default conventions. For advanced configuration, view `settings.py` Paths class.

## Default Conventions

It's recommended to store all program components as shown below. For advanced usage, you can change this, but then you have to configure Paths in `settings.py`.

```
media_editor/
├── resources/
│   ├── font.ttf
│   ├── music/
│   │   ├── music1.mp3
│   │   ├── music2.mp3
│   │   └── ...
│   └── platform-tools/
│       └── ...
├── process.py
├── editor_image.py
├── editor_video.py
├── media_transfer.py
├── helpers.py
├── settings.py
└── requirements.txt
```

## ADB Shell Download Guide

**ADB (Android Debug Bridge)** is a tool developed by Google for interfacing with Android devices via USB debugging. It's used

 here for transferring media between Android devices and computers.

1. Download the source code:
   - [Windows](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)
   - [Linux](https://dl.google.com/android/repository/platform-tools-latest-linux.zip)
2. Move the `platform-tools` folder to the `resources/` directory in the program folder.
3. Enable USB debugging on your Android device and pair it with your computer. 
   - [Official ADB website](https://developer.android.com/studio/command-line/adb)
   - [Detailed install guide](https://www.xda-developers.com/install-adb-windows-macos-linux/)

## ImageMagick Installation

**ImageMagick** is a video editing tool used by the Python `moviepy` library for adding text watermarks over videos.

#### Windows

1. Download the [installer](https://imagemagick.org/archive/binaries/ImageMagick-7.1.0-39-Q16-HDRI-x64-dll.exe).
2. Follow the installation instructions.
3. In `settings.py`, set the `IMAGEMAGICK_BINARY` variable to the path of `magick.exe`. By default, it should be `C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe`.

#### Linux

- For Linux, refer to the installation guide on the official [ImageMagick website](https://imagemagick.org/script/download.php).
