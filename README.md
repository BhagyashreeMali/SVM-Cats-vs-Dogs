<div align="center">

# 🐱 Cats vs Dogs — SVM Classifier 🐶

<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/scikit--learn-SVM-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
<img src="https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
<img src="https://img.shields.io/badge/NumPy-2.x-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">

<br><br>

> _A binary image classifier that distinguishes cats from dogs using Support Vector Machine (SVM) with a linear kernel._

<br>

<img src="https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif" width="180" alt="Cat">
&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://media.giphy.com/media/4Zo41lhzKt6iZ8xff9/giphy.gif" width="180" alt="Dog">

</div>

---

## 🏗️ How It Works

```
📷 Load Images ──▶ 🔄 Resize (64×64) ──▶ 📐 Flatten (12,288 px) ──▶ 🧠 SVM (Linear) ──▶ 🎯 Predict
```

1. **Load** cat & dog images from `dataset/cats/` and `dataset/dogs/`
2. **Resize** each image to `64×64` pixels using **OpenCV**
3. **Flatten** into a 1D array of 12,288 features (64 × 64 × 3 RGB)
4. **Split** into 80% training / 20% testing using **train_test_split**
5. **Train** a **Linear SVM** classifier using **scikit-learn**
6. **Evaluate** using **accuracy_score**

---

## 📂 Project Structure

```
SVM-Cats-vs-Dogs/
├── svm_cats_dogs.py       # Main SVM classifier script
├── .gitignore             # Ignores dataset/, .venv/, .DS_Store
├── README.md
└── dataset/               # (Download from Kaggle)
    ├── cats/              # 12,500 cat images
    └── dogs/              # 12,500 dog images
```

---

## ⚙️ Setup & Installation

### 1. Clone & Setup

```bash
git clone https://github.com/BhagyashreeMali/SVM-Cats-vs-Dogs.git
cd SVM-Cats-vs-Dogs
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
```

### 2. Install Dependencies

```bash
pip install numpy opencv-python scikit-learn
```

### 3. Download Dataset

1. Go to [Kaggle Dogs vs Cats](https://www.kaggle.com/c/dogs-vs-cats/data)
2. Download & extract `dogs-vs-cats.zip` → then extract `train.zip` inside it
3. Sort images into:
   - `dataset/cats/` — all `cat.*.jpg` files
   - `dataset/dogs/` — all `dog.*.jpg` files

---

## 🚀 Run

```bash
python svm_cats_dogs.py
```

### Output

```
  cats: 1000 images loaded
  dogs: 1000 images loaded
Dataset Loaded: (2000, 12288)
Training Model...
Model Accuracy: 0.54
```

---

## 📊 Results

| Metric                 | Value                   |
| ---------------------- | ----------------------- |
| **Total Images Used**  | 2,000 (1,000 per class) |
| **Train / Test Split** | 80% / 20%               |
| **SVM Kernel**         | Linear                  |
| **Accuracy**           | ~54%                    |

---

## 🔧 Configuration

Edit these values in `svm_cats_dogs.py`:

| Parameter       | Default    | Description                                  |
| --------------- | ---------- | -------------------------------------------- |
| `MAX_PER_CLASS` | `1000`     | Images per class (set `None` for all 12,500) |
| `test_size`     | `0.2`      | Fraction reserved for testing                |
| `kernel`        | `'linear'` | SVM kernel type                              |
| Image size      | `(64, 64)` | Resize dimensions                            |

---

## �️ Technologies Used

|    Technology    |                   Purpose                    |
| :--------------: | :------------------------------------------: |
|    **Python**    |                Core language                 |
|    **OpenCV**    |           Image loading & resizing           |
|    **NumPy**     |               Array operations               |
| **scikit-learn** | SVM model, train/test split, accuracy metric |

---

<div align="center">

### ⭐ Star this repo if you found it useful!

Made with ❤️ by [Bhagyashree Mali](https://github.com/BhagyashreeMali)

<img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="150" alt="Cat typing">

</div>
