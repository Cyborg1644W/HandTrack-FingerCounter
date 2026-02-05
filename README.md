# HandTrack-FingerCounter
A real-time hand-tracking and finger-counting application built with Python, OpenCV, and MediaPipe. Optimized for performance on macOS Apple Silicon (M4).

# AI Hand Tracker & Finger Counter

A high-performance Computer Vision application that detects hand landmarks in real-time and calculates the number of extended fingers. This version is specifically configured to handle the unique environment requirements of macOS Apple Silicon (M1/M2/M3/M4).



## 🛠 Features
* **Dual-Hand Support:** Detects and tracks multiple hands simultaneously.
* **Orientation Awareness:** Different logic for Left and Right hand thumbs to ensure accuracy.
* **Skeleton Overlay:** Visualizes hand connections and joints using MediaPipe's drawing utilities.
* **macOS Optimized:** Specifically tested to bypass common `AttributeError` and `GraphConfig` bugs on M-series chips.

## 📐 How it Works
The counter uses the **Landmark Model** to track 21 points on the hand. 

* **Fingers:** A finger is counted as "open" if the tip landmark $y$-coordinate is higher on the screen (lower numerical value) than the PIP joint (the second joint from the tip).
  $$y_{tip} < y_{joint}$$
* **Thumb:** Uses lateral movement logic by comparing the $x$-coordinate of the tip to the $x$-coordinate of the MCP joint, adjusted for handedness.

## 🚀 Getting Started

### Prerequisites
* **Python 3.9** (Recommended for macOS stability)
* **OpenCV:** `pip install opencv-python`
* **MediaPipe:** `pip install mediapipe==0.10.14`

### Installation & Usage
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/HandTrack-FingerCounter.git](https://github.com/YOUR_USERNAME/HandTrack-FingerCounter.git)
   cd HandTrack-FingerCounter
