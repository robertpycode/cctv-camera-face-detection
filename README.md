\# CCTV Face Detection System



A real-time computer vision application built with Python and OpenCV that uses a webcam to detect human faces and record video footage. The project explores practical applications of computer vision for security and monitoring systems.



\## Project Overview



This project was developed to strengthen my understanding of computer vision, real-time video processing, webcam integration, and Python application development.



The system captures live video from a webcam, processes each frame using OpenCV, detects human faces, and displays detection results in real time. It can also record captured footage for later review.



\## Features



\* Real-time webcam video capture

\* Human face detection using OpenCV

\* Face detection bounding boxes

\* Video recording

\* Motion/detection alert functionality

\* Real-time frame processing

\* Configurable camera settings

\* Automated video file generation



\## Technologies



\* \*\*Python\*\*

\* \*\*OpenCV\*\*

\* \*\*Computer Vision\*\*

\* \*\*Haar Cascade Classifier\*\*

\* \*\*Webcam/Video Processing\*\*



\## How It Works



The application accesses the computer's webcam and continuously captures video frames.



Each frame is processed using OpenCV's computer vision capabilities. The system converts frames into an appropriate format for detection and uses a Haar Cascade classifier to identify human faces.



When a face is detected, the application highlights it with a bounding box. The processed video can also be saved for later analysis.



\### Processing Pipeline



```text

Webcam

&#x20;  ↓

Capture Video Frame

&#x20;  ↓

Frame Preprocessing

&#x20;  ↓

Face Detection

&#x20;  ↓

Draw Detection Results

&#x20;  ↓

Display Live Video

&#x20;  ↓

Record / Save Video

```



\## Installation



\### 1. Clone the repository



```bash

git clone https://github.com/YOUR-USERNAME/cctv-camera-face-detection.git

```



\### 2. Navigate to the project directory



```bash

cd cctv-camera-face-detection

```



\### 3. Create a virtual environment



Windows:



```bash

python -m venv .venv

```



Activate it:



```bash

.venv\\Scripts\\activate

```



\### 4. Install dependencies



Install OpenCV:



```bash

pip install opencv-python

```



\## Usage



Run the application with:



```bash

python cctv\_camera\_face\_detection.py

```



Make sure your computer has a working webcam connected.



The application will open the camera feed and process the video in real time.



\## Project Structure



```text

cctv-camera-face-detection/

│

├── cctv\_camera\_face\_detection.py

├── .gitignore

└── README.md

```



\## What I Learned



Through this project, I gained practical experience with:



\* Python programming

\* OpenCV and computer vision

\* Real-time video processing

\* Webcam integration

\* Face detection algorithms

\* Image and video frame processing

\* Debugging hardware/software interactions

\* Git and GitHub version control



\## Challenges



One of the main challenges was working with real-time video processing and ensuring that frames were captured, processed, displayed, and recorded correctly.



I also worked through issues involving video codecs, camera performance, OpenCV configuration, and video file generation. Troubleshooting these issues helped me develop stronger debugging and problem-solving skills.



\## Future Improvements



Potential improvements include:



\* Adding facial recognition rather than basic face detection

\* Adding a database for recognized individuals

\* Implementing an automated alert system

\* Adding email or mobile notifications

\* Improving detection accuracy

\* Adding object detection

\* Creating a web-based monitoring dashboard

\* Adding multiple camera support

\* Implementing secure cloud-based video storage



\## Author



\*\*Robert Junior Osei Bonsu\*\*



Computer Information Systems Student

Aspiring AI/ML Engineer



\---



\*This project was developed as part of my ongoing journey in Python programming, computer vision, and artificial intelligence.\*



