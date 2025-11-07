# 🖐 Finger Counter using Hand Tracking 📷🤚

Welcome to the **Finger Counter** project! This Python project uses OpenCV and MediaPipe to detect hands and count the number of fingers shown in front of a webcam in real time.

---

## ✨ Features

- **Real-Time Hand Detection** 🖐
- **Finger Count Recognition** (0 to 5) ✋
- **Live FPS Display** 💡
- **Simple & Intuitive UI** (streamed from your webcam) 🎥
- **Fast and Lightweight** 🚀

---

## 🛠️ Requirements

- Python 3.7+
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)

---

## ⚡ Installation

1. **Clone this repository**
```shell script
git clone https://github.com/your-username/finger-counter.git
   cd finger-counter
```


2. **Install dependencies**
```shell script
pip install -r requirements.txt
```


   *requirements.txt*:
```
opencv-python
   mediapipe
```


---

## ▶️ Usage

Run the finger counter script:

```shell script
python fingercounter.py
```


- The application window will show your webcam feed.
- Hold up your hand—the number of extended fingers is displayed onscreen.
- **Press `q`** to quit the application.

---

## 📁 Project Structure

```
├── HTModule.py         # Hand tracking and landmark detector module
├── fingercounter.py    # Finger counting application
```


---

## 🤖 How it Works

- **Hand Detection:** Uses MediaPipe Hands for robust, real-time hand and finger landmark detection.
- **Finger Counting:** Compares landmark positions to determine which fingers are up.
- **Display:** Overlays the detected finger count and frames per second (FPS) onto the webcam video stream.

---

## 👨‍💻 Credits

- Built with ❤️ using [MediaPipe](https://mediapipe.dev/) and [OpenCV](https://opencv.org/).

---

