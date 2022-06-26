# Python Media Editor

  Automated productivity tool for Video/Image watermarking and adding music. It automatically transfers media from Android device, processes and pushes processed media back on Android. It adds specified watermark text label over Image/Video and adds music over video. It also compresses videos to 720p if specified. It has configurable properties, such as text label, size, position, color, encoding, fps and etc.


## usage

1. In android device, move target Images/Videos to gallery album with the name **`Transfer`**
2. Connect Android with Computer using USB Cable
3. Run `python3 process.py` and the rest will be done automatically

all processed Images/Videos will be in newly created album with the name **`Processed`** in Android device.

#### Process (Algorithm)

1. Transfers all media from Android `Transfer` album to `Transfer` directory locally on machine.
2. Scannimg transfered media and organizing it seperately as Images and Videos.
3. Processing Images
	- adds text label (watermark) over each image
	- each Image is saved in `Processed/` directory locally
4. Processing Videos 
	- adds text label (watermark) over each video
	- select random music from `resources/music/` folder and add it over current video
	- if `compress` is set to **True**, each video is compressed to 720p (HD) if possible.
	- each Video is saved in `Processed/` directory locally
5. Transfering processed media in Android device
	- all media is transfered in `Transfered` album in android gallery.
6. Media files are removed locally
		
## requirements
- **python 3**
- **moviepy** library `pip3 install moviepy`
- **PIL** library `pip3 install pillow`

also listed in `requirements.txt`

#### Other Software
- **ADB shell** [Android Debug Bridge]
- **ImageMagick** [Software used by moviepy for adding text over video]

read about installation below


## Installation

1. Clone/Download this repository and extract it on your machine. 
2. Install **python 3** if not installed on your machine
3. Install required packages with **pip3** 
	- `pip3 install -r requirements.txt` **or** `pip3 install pillow moviepy` (on some machines use pip instead of pip3)
4. Install **ImageMagick** on your machine. [view detailed explanation below]
5. Download **ADB shell** on your machine. [view detailed explanation below]

## configuration

in `settings.py` file you can configure program. Options are:


#### ImageConfig

- `text` - text to be written over each image **[string]**
- `text_color` - color of the text **[string]**
- `text_stroke_fill` - text outline color **[string]**
- `text_stroke_weight` - text outline size **[integer]**
- `text_width_fraction` - fraction of text width over image **[float: 0-1]**
- `text_pos` - text to be written over each image **[tuple (posX, posY)]**

#### VideoConfig

- `text` - text to be written over each video **[string]**
- `text_pos` - text alignment over video **[top, bottom, left, right]**
- `text_color` - color of the text **[string]**
- `fps` - processed video fps **[integer]**
- `threads` - number of threads used for processing **[integer]**
- `codec` - video codec **[string]**
- `compress` - compresses video to 720p if True **[boolean True/False]**

#### Paths

Paths will be automatically configured if you follow default conventions [view below]. For more advanced configuration view `settings.py` Paths class.


## Default Conventions
It is recommended to store all program components as shown below. For advanced usage, you can change this, but then you have to configure Paths in `settings.py`

```
media_editor/
├── resources/
  ├── font.ttf
  ├── music/
    ├── music1.mp3
    ├── music2.mp3
    └── ...
  └── platform-tools/
    └── ...
├── process.py
├── editor_image.py
├── editor_video.py
├── media.transfer.py
├── helpers.py
├── settings.py
└── requirements.txt

```

## ADB shell Download Guide

**ADB** (Android Debug Bridge) is software developed by Google for accessing Android using USB debugging. In this case, it is used to transfer media from android to machine and vice versa.

1. Download source code
	- [Windows](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)
	- [Linux](https://dl.google.com/android/repository/platform-tools-latest-linux.zip)
2. Move this folder in `resources/` directory in program folder.
3. Enable USB debugging on Android device and pair it with your computer [read more in below links]

- [Official ADB website](https://developer.android.com/studio/command-line/adb)
- [Read more detailed install guide](https://www.xda-developers.com/install-adb-windows-macos-linux/)

## ImageMagick Installation

**ImageMagick** is video editing software. In this program it is used by python `moviepy` video editing library for writing text watermark over videos.

#### WIndows

1. Download [installer](https://imagemagick.org/archive/binaries/ImageMagick-7.1.0-39-Q16-HDRI-x64-dll.exe) 
2. Follow instructions and install
3. in `settings.py`, set `IMAGEMAGICK_BINARY` variable with magick.exe executable path. By default, it should be `C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe` (this path is already set as value).

#### Linux
- for linux, read installation guide on official [website](https://imagemagick.org/script/download.php)
