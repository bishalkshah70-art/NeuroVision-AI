# 🧠 NeuroVision-AI

## AI-Powered Brain Tumor Classification Using Convolutional Neural Networks (CNN)

NeuroVision-AI is a deep learning-based medical image classification project that uses Convolutional Neural Networks (CNNs) to analyze brain MRI images and classify them into different categories of brain tumors.

The goal of this project is to demonstrate how Artificial Intelligence and Computer Vision can assist in medical image analysis by providing fast and accurate MRI classification.

---

## 🚀 Project Overview

Brain tumor diagnosis from MRI scans requires expert analysis and can be time-consuming. This project develops an AI model that learns patterns from MRI images and automatically predicts the category of brain abnormalities.

The CNN model is trained to classify MRI scans into four categories:

- 🧠 Glioma Tumor
- 🧠 Meningioma Tumor
- 🧠 Pituitary Tumor
- ✅ No Tumor

---

## 🎯 Objectives

- Build a deep learning model for brain MRI classification.
- Apply Convolutional Neural Networks for medical image analysis.
- Train and evaluate the model using MRI image datasets.
- Measure performance using accuracy, precision, recall, and F1-score.
- Develop an AI-based prediction system for MRI images.

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Deep Learning Framework
- TensorFlow
- Keras

### Data Processing
- NumPy
- Pandas
- Pillow (PIL)
- OpenCV

### Visualization
- Matplotlib

### Model Evaluation
- Scikit-learn

### Development Environment
- Jupyter Notebook
- Google Colab / VS Code

---

## 📂 Project Structure

```
NeuroVision-AI/
│
├── dataset/
│   ├── Training/
│   └── Testing/
│
├── notebooks/
│   └── brain_tumor_classification.ipynb
│
├── models/
│   └── brain_tumor_model.keras
│
├── screenshots/
│   ├── accuracy_graph.png
│   ├── loss_graph.png
│   └── confusion_matrix.png
│
├── predict.py
├── train.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📊 Dataset

Dataset used:

**Brain Tumor MRI Dataset**

Classes:

```
1. Glioma
2. Meningioma
3. Pituitary
4. No Tumor
```

The dataset contains MRI brain scan images used for training and evaluation of the deep learning model.

---

## 🧠 Model Architecture

The project uses a Convolutional Neural Network consisting of:

- Input Layer
- Convolutional Layers
- ReLU Activation
- Max Pooling Layers
- Batch Normalization
- Dropout Layers
- Fully Connected Dense Layers
- Softmax Output Layer

---

## 📈 Model Performance

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Example results:

```
Test Accuracy: XX%

Precision: XX%

Recall: XX%

F1 Score: XX%
```

*(Update these values after training your final model.)*

---

## 🔍 Prediction Example

Input:

```
Brain MRI Image
```

Output:

```
Prediction:
Glioma Tumor

Confidence:
95%
```

---

## 🔮 Future Improvements

- Add Explainable AI using Grad-CAM.
- Deploy as a web application.
- Add real-time MRI analysis.
- Improve accuracy using transfer learning models:
  - EfficientNet
  - ResNet
  - MobileNet
- Develop a healthcare AI assistant system.

---

## 👨‍💻 Author

**Bishal Kumar Sah**

AI/ML Engineer | Deep Learning Enthusiast

GitHub:
https://github.com/bishalkshah70-art

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Acknowledgements

- TensorFlow and Keras documentation
- Open-source medical imaging datasets
- Research community in Deep Learning and Computer Vision
