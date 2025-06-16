```markdown
# 🚘 Tesseract-OCR-car

A simple application that detects and extracts text from vehicle license plates using OpenCV for image preprocessing and [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for character recognition.

---

## 🧠 How It Works

1. Load an image or frame from a video.
2. Apply image preprocessing (grayscale, thresholding, edge detection).
3. Detect license plate region using contours.
4. Crop the detected plate area.
5. Use Tesseract to recognize and extract text.

---

## 🖼️ Example

![Demo](https://upload.wikimedia.org/wikipedia/commons/6/69/License_plate_of_the_Philippines_%282018_Albay_private%29.png)

> Output:
```

Detected Plate: ABC1234

````

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/DoNguyenAnhTuan/Tesseract-OCR-car.git
cd Tesseract-OCR-car
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract (if not installed)

* [Tesseract GitHub Releases](https://github.com/tesseract-ocr/tesseract)
* On Ubuntu:

  ```bash
  sudo apt install tesseract-ocr
  ```

### 4. Run the script

```bash
python detect_plate.py --image path/to/your/image.jpg
```

---

## 🧾 Requirements

* Python 3.7+
* OpenCV
* Pytesseract

---

## 📁 Folder Structure

```
Tesseract-OCR-car/
├── detect_plate.py
├── requirements.txt
├── samples/
│   └── example_car.jpg
```

---

## 🙋 Use Cases

* Smart parking systems
* Automated toll collection
* Vehicle tracking and logging

---

## 👨‍💻 Author

**Do Nguyen Anh Tuan**
📍 MSc in Information Technology @ Lac Hong University
🏫 FabLab @ Eastern International University
🔬 Focus: Computer Vision, OCR, AI Applications

