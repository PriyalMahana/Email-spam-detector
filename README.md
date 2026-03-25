# 📧 Email Spam Detector

A simple and effective **Machine Learning project** that classifies messages as **Spam or Not Spam** using Natural Language Processing (NLP).

---

## 🚀 Features
- 📊 Text classification using **TF-IDF**
- 🤖 Machine Learning model (**Naive Bayes**)
- 📨 Detects spam messages instantly
- 🧠 Learns patterns from dataset
- 💬 Custom user input prediction

---

## 🛠️ Tech Stack
- 🐍 Python  
- 📚 Pandas  
- 🤖 Scikit-learn  
- 🔤 TF-IDF Vectorizer  
- 📈 Multinomial Naive Bayes  

---

## Project Structure
```
project/
│── main.py
│── spam.csv
│── README.md
|── Report.docx
```

---

## Requirements
- Python 3.x
- pandas
- scikit-learn

Install using:
```
pip install pandas scikit-learn

```

## Dataset
A manually created dataset is used with two columns:
- v1 → label (spam/ham)
- v2 → message

## ▶️ How to Run

python code.py

Enter your message: Win a free prize now

Output:
Spam

---

## 🧠 How It Works
1. 📥 Loads dataset (`spam.csv`)
2. 🔄 Converts labels (spam = 1, ham = 0)
3. 🔤 Transforms text using **TF-IDF**
4. ✂️ Splits data into training & testing
5. 🤖 Trains **Naive Bayes model**
6. 📊 Predicts spam or not spam

---

## 📊 Example
| Message | Prediction |
|--------|-----------|
| Win money now | Spam |
| Let's meet tomorrow | Not Spam |

---

## ⚡ Advantages
- ✅ Simple and fast  
- ✅ Beginner-friendly  
- ✅ Good accuracy  
- ✅ Easy to extend  

---

## ⚠️ Limitations
- ❌ Small dataset reduces accuracy  
- ❌ Assumes words are independent  
- ❌ May fail on complex sentences  

---

## 🔮 Future Improvements
- 🎨 Add GUI (Tkinter)  
- 🌐 Convert to web app (Flask)  
- 📈 Use larger dataset  
- 🤖 Try deep learning models  

---

## 👨‍💻 Author
**Priyal Mahana**

---

## ⭐ Show Your Support
If you like this project:
- ⭐ Star the repo  
- 🍴 Fork it  
- 📢 Share it  
