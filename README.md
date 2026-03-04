<div align="center">

# 🐱 Cats vs Dogs — SVM Classifier 🐶

<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/scikit--learn-1.8-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
<img src="https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
<img src="https://img.shields.io/badge/NumPy-2.x-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">

<br><br>

> _A machine learning project that classifies images of cats and dogs using a Support Vector Machine (SVM) with a linear kernel — built from scratch using raw pixel features._

<br>

<img src="https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif" width="200" alt="Cat">
&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://media.giphy.com/media/4Zo41lhzKt6iZ8xff9/giphy.gif" width="200" alt="Dog">

</div>

---

## 📌 Table of Contents

- [✨ Overview](#-overview)
- [🏗️ How It Works](#️-how-it-works)
- [📂 Project Structure](#-project-structure)
- [⚙️ Setup & Installation](#️-setup--installation)
- [🚀 Usage](#-usage)
- [📊 Results](#-results)
- [🔧 Configuration](#-configuration)
- [💡 Tips to Improve Accuracy](#-tips-to-improve-accuracy)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Overview

This project demonstrates **binary image classification** using a classical machine learning approach. Instead of deep learning, we use a **Support Vector Machine (SVM)** to distinguish between cat and dog images from the popular [Kaggle Dogs vs Cats](https://www.kaggle.com/c/dogs-vs-cats) dataset.

### 🎯 Key Highlights

| Feature                | Description                                       |
| ---------------------- | ------------------------------------------------- |
| 🧠 **Algorithm**       | Support Vector Machine (Linear Kernel)            |
| 📷 **Image Size**      | 64 × 64 pixels (resized)                          |
| 📦 **Feature Vector**  | 12,288 features (64 × 64 × 3 RGB channels)        |
| 📊 **Dataset**         | 25,000 labeled images (12,500 cats + 12,500 dogs) |
| ⚡ **Training Subset** | Configurable (default: 1,000 per class)           |

---

## 🏗️ How It Works

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│  Load Image │────▶│ Resize 64×64 │────▶│   Flatten   │────▶│  SVM Train   │
│  (cat/dog)  │     │   (RGB)      │     │ (12,288 px) │     │  (Linear)    │
└─────────────┘     └──────────────┘     └─────────────┘     └──────────────┘
                                                                     │
                                                                     ▼
                                                              ┌──────────────┐
                                                              │   Predict    │
                                                              │  🐱 or 🐶   │
                                                              └──────────────┘
```

**Step-by-step:**

1. **Load** images from `dataset/cats/` and `dataset/dogs/`
2. **Resize** each image to `64×64` pixels
3. **Flatten** into a 1D feature vector of 12,288 values
4. **Split** data into 80% training / 20% testing
5. **Train** a Linear SVM classifier
6. **Evaluate** accuracy on the test set

---

## 📂 Project Structure

```
cats_dogs_svm/
│
├── 📄 svm_cats_dogs.py      # Main classifier script
├── 📄 .gitignore             # Git ignore rules
├── 📄 README.md              # You are here!
│
└── 📁 dataset/               # (Download from Kaggle)
    ├── 📁 cats/              # 12,500 cat images
    │   ├── cat.0.jpg
    │   ├── cat.1.jpg
    │   └── ...
    └── 📁 dogs/              # 12,500 dog images
        ├── dog.0.jpg
        ├── dog.1.jpg
        └── ...
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/BhagyashreeMali/SVM-Cats-vs-Dogs.git
cd SVM-Cats-vs-Dogs
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install numpy opencv-python scikit-learn
```

### 4️⃣ Download the Dataset

1. Go to [Kaggle Dogs vs Cats](https://www.kaggle.com/c/dogs-vs-cats/data)
2. Download `dogs-vs-cats.zip`
3. Extract and organize into the following structure:

```
dataset/
├── cats/       # Place all cat.*.jpg images here
└── dogs/       # Place all dog.*.jpg images here
```

> 💡 **Tip:** The Kaggle zip contains a nested `train.zip` — extract that to get the labeled images, then sort them into `cats/` and `dogs/` folders.

---

## 🚀 Usage

Run the classifier with a single command:

```bash
python svm_cats_dogs.py
```

### Expected Output

```
  Loaded 200 cats images...
  Loaded 400 cats images...
  ...
  cats: 1000 images loaded
  Loaded 200 dogs images...
  ...
  dogs: 1000 images loaded
Dataset Loaded: (2000, 12288)
Training Model...
Model Accuracy: 0.54
```

---

## 📊 Results

| Metric              | Value                       |
| ------------------- | --------------------------- |
| **Training Images** | 1,600 (800 cats + 800 dogs) |
| **Testing Images**  | 400 (200 cats + 200 dogs)   |
| **Kernel**          | Linear                      |
| **Accuracy**        | ~54%                        |

> **Note:** The accuracy with raw pixel features is modest. See the [Tips to Improve Accuracy](#-tips-to-improve-accuracy) section below for enhancement ideas.

---

## 🔧 Configuration

You can tweak the classifier by editing `svm_cats_dogs.py`:

| Parameter       | Default    | Description                                               |
| --------------- | ---------- | --------------------------------------------------------- |
| `MAX_PER_CLASS` | `1000`     | Max images loaded per class. Set to `None` for all 12,500 |
| `test_size`     | `0.2`      | Train/test split ratio                                    |
| `kernel`        | `'linear'` | SVM kernel type (`'linear'`, `'rbf'`, `'poly'`)           |
| Image size      | `(64, 64)` | Resize dimensions for each image                          |

---

## 💡 Tips to Improve Accuracy

<details>
<summary>🔹 <b>1. Normalize Pixel Values</b></summary>

```python
X = X / 255.0  # Scale pixels to [0, 1]
```

</details>

<details>
<summary>🔹 <b>2. Use HOG Features Instead of Raw Pixels</b></summary>

```python
from skimage.feature import hog

def extract_hog(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    features = hog(gray, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
    return features
```

</details>

<details>
<summary>🔹 <b>3. Try RBF Kernel</b></summary>

```python
model = SVC(kernel='rbf', C=10, gamma='scale')
```

</details>

<details>
<summary>🔹 <b>4. Increase Training Data</b></summary>

```python
MAX_PER_CLASS = 5000  # Use more images (slower training)
```

</details>

<details>
<summary>🔹 <b>5. Use a CNN for Better Accuracy</b></summary>

For image classification, Convolutional Neural Networks (CNNs) typically achieve **90%+** accuracy. Consider using TensorFlow/Keras or PyTorch for a deep learning approach.

</details>

---

## 🛠️ Tech Stack

<div align="center">

|                                                    Technology                                                     |              Purpose              |
| :---------------------------------------------------------------------------------------------------------------: | :-------------------------------: |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="40"> |    **Python** — Core Language     |
|      <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="40">       | **Scikit-learn** — SVM Classifier |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/opencv/opencv-original.svg" width="40"> |   **OpenCV** — Image Processing   |
|  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" width="40">  |  **NumPy** — Numerical Computing  |

</div>

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. 🍴 Fork this repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔃 Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

### ⭐ Star this repo if you found it useful!

Made with ❤️ by [Bhagyashree Mali](https://github.com/BhagyashreeMali)

<img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="150" alt="Cat typing">

</div>
