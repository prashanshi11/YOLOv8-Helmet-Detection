# 🦺 Construction Safety Helmet Detection using YOLOv8


This project implements a **real-time helmet detection system** using **YOLOv8** to monitor safety on construction sites. It identifies whether workers are wearing helmets and safety vests through a live webcam feed and raises alerts when violations are detected.

---

## 📌 Features

- ✅ Detects "Hardhat", "No-Hardhat", and "Vest"
- 📷 Real-time object detection from webcam
- 🔔 Audio alert if any person is detected **without a helmet**
- 📦 YOLOv8 training on custom dataset
- 🛠️ Fully compatible with Windows (and Linux/Mac with minor tweaks)

---

## 📁 Project Structure

```

construction\_safety\_yolo/
├── dataset/
│   ├── train/
│   ├── test/
│   └── data.yaml
├── scripts/
│   ├── train\_model.py        # YOLOv8 model training script
│   └── live\_detect.py        # Real-time detection script
├── runs/                     # YOLO training results (contains best.pt)
├── requirements.txt
└── README.md

````

---

## 🧠 Classes Explained

| Label        | Meaning                  |
|--------------|---------------------------|
| `Hardhat`     | Worker without a helmet (⚠️ alert) |
| `No-Hardhat`  | Worker wearing a helmet (✅ safe)  |
| `Vest`        | Worker wearing a safety vest      |

---

## 🚀 Getting Started

### ✅ 1. Install Required Packages

```bash
pip install ultralytics opencv-python
````

> **Linux/Mac users:** For sound alerts, install `sox`:

```bash
sudo apt-get install sox
```

---

### ✅ 2. Train the Model

```python
# scripts/train_model.py
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.train(
    data='./dataset/data.yaml',
    epochs=15,
    imgsz=320,
    batch=4
)
```

**data.yaml:**

```yaml
train: C:/.../dataset/train/images
val: C:/.../dataset/test/images

nc: 3
names: ["Hardhat", "No-Hardhat", "Vest"]
```

---

### ✅ 3. Run Real-Time Detection

```bash
python scripts/live_detect.py
```

* Press `q` to quit webcam stream.
* Alerts are printed in the terminal and sound will play if someone is not wearing a helmet.

---

## 🔊 Sound Alert Logic

```python
if heads > helmets:
    print("⚠️ No helmet detected!")
    beep_alert()
```

* **Windows**: uses `winsound`
* **Linux/Mac**: uses `sox` (`play` command)

---

## 🎯 Use Cases

* Construction site monitoring
* Industrial safety audits
* Real-time alerts in hazardous areas
* Smart surveillance systems

---

## 📷 Output Example

* Bounding boxes for Hardhat, No-Hardhat, and Vest
* Audio + terminal alert for non-compliance

---

## 🧑‍💻 Author

**Prashanshi Yadav**
📫 **Email**: [prashanshiyadav.dev@gmail.com](mailto:prashanshi674@gmail.com)
🔗 **GitHub**: [github.com/prashanshi11](https://github.com/prashanshi11)
📸 **Project Video**:https://www.linkedin.com/posts/prashanshi_machinelearning-computervision-yolov8-activity-7341694858056658944-tmDO?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD2-DKMB2mzbi7yGhAg37zLCWTnlVB7eKX0


---
