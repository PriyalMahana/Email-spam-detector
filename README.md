# Spam Email Detector 

## Introduction
This project is a machine learning-based spam detection system. It classifies messages into spam or not spam using the Naive Bayes algorithm.

## Features
- Text classification using TF-IDF
- Naive Bayes model
- Custom user input prediction
- Simple and efficient

## Project Structure
```
project/
│── main.py
│── spam.csv
│── README.md
```

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

## How It Works
1. Load dataset
2. Convert labels to numbers
3. Convert text into TF-IDF features
4. Train Naive Bayes model
5. Evaluate accuracy
6. Predict user input

## How to Run
1. Place spam.csv in the same folder
2. Run the Python file:
```
python main.py
```
3. Enter messages to test

## Example
Input:
```
Win a free prize now
```
Output:
```
Spam
```

## Advantages
- Fast
- Simple
- Beginner-friendly

## Limitations
- Needs more data for better accuracy
- Not perfect for complex messages

## Future Improvements
- GUI application
- Web deployment
- Deep learning models

