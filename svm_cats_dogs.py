import os
import sys
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

data = []
labels = []

dataset_path = "dataset"
categories = ["cats", "dogs"]

# Verify dataset exists
for category in categories:
    cat_path = os.path.join(dataset_path, category)
    if not os.path.isdir(cat_path) or len(os.listdir(cat_path)) == 0:
        print(f"ERROR: '{cat_path}' directory is missing or empty!")
        print("\nTo set up the dataset, run:")
        print("  python setup_dataset.py")
        print("\nOr manually place images in dataset/cats/ and dataset/dogs/")
        sys.exit(1)

# Limit images per class for practical SVM training (set to None to use all)
MAX_PER_CLASS = 1000

for category in categories:
    
    path = os.path.join(dataset_path, category)
    label = categories.index(category)
    count = 0
    
    for img in os.listdir(path):
        if MAX_PER_CLASS and count >= MAX_PER_CLASS:
            break
        
        img_path = os.path.join(path, img)
        
        try:
            image = cv2.imread(img_path)
            image = cv2.resize(image, (64,64))
            image = image.flatten()
            
            data.append(image)
            labels.append(label)
            count += 1
            
            if count % 200 == 0:
                print(f"  Loaded {count} {category} images...")
            
        except:
            pass
    
    print(f"  {category}: {count} images loaded")

X = np.array(data)
y = np.array(labels)

print("Dataset Loaded:", X.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = SVC(kernel='linear')

print("Training Model...")
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)