# ✍️ GestureWriter


**GestureWriter** is a real-time hand gesture recognition system that converts static hand signs into typed text using your webcam. It supports alphabets A–Z, along with `SPACE` and `BACKSPACE` signs.

> 🔗 **Repository**: [https://github.com/Nikhil-avula/GestureWriter](https://github.com/Nikhil-avula/GestureWriter)

---

## 🎯 Key Features

- 🖐️ Detects hand landmarks using **MediaPipe**
- 🔤 Classifies signs into A-Z + space/backspace
- 🧠 Uses a pre-trained ML model (`model_03.pkl`)
- 🛑 Stable predictions using time threshold (1.5s hold)
- 💬 Real-time display of typed text on the video feed
- ⚙️ No external dependencies beyond standard Python ML stack

---


## 🗂️ Folder Structure

```

GestureWriter/
├── model\_03.pkl           # Pre-trained gesture classification model
├── hand\_sign.py          # Main app file (run this)
├── README.md              # Project overview and instructions
├── requirements.txt       # Python dependencies

````

---

## 🧠 How It Works

1. Captures frames from your webcam.
2. Detects 21 hand landmarks using **MediaPipe**.
3. Normalizes landmarks relative to the wrist.
4. Flattens and passes them to a trained ML model.
5. If the prediction stays consistent for 1.5 seconds:
   - Adds character to the text box.
   - Allows space or backspace gestures.
6. Displays the recognized gesture and full sentence live.

---

## 🛠️ Installation & Setup

```bash
git clone https://github.com/Nikhil-avula/GestureWriter.git
cd GestureWriter
pip install -r requirements.txt
````

### Requirements

* Python 3.8+
* OpenCV
* MediaPipe
* scikit-learn
* numpy
* pandas

---

## ▶️ Run the App

```bash
python hand_sign.py
```

* Make sure your webcam is connected.
* Press `c` to quit the app.

---

## 🔁 Customization

Want to build your own model?

1. Collect hand landmark data using MediaPipe.
2. Normalize using wrist-relative 3D coordinates.
3. Train a classifier (RandomForest, SVM, etc.)
4. Save it with `pickle` and use it in place of `model_03.pkl`.

---

## ✍️ Author

**Nikhil Avula**
📧 (mailto:avulanikhil25@gmail.com)
🔗 [GitHub]((https://github.com/Nikhil-avula/GestureWriter)) | [LinkedIn](www.linkedin.com/in/avula-nikhil-3521b72b1)

---


---

## 🙌 Acknowledgments

* [MediaPipe]((https://ai.google.dev/edge/mediapipe/solutions/guide))
* [OpenCV]((https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html))
* [scikit-learn]((https://scikit-learn.org/stable/index.html))

```


