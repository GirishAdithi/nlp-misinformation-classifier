# **Phase 3 — Baseline Modeling**

### **Goal**

> What is my goal for building a baseline model?

Why am I starting with simple models instead of immediately using more advanced machine learning models?

---

### **Train/Test Split**

How did I split my dataset into training and testing data?

Why did I choose an 80/20 split?

Why did I use stratification for the labels?

What does using a fixed `random_state` help with?

---

### **TF-IDF**

Why can't I directly give the article text to my machine learning models?

What is TF-IDF and how does it convert the text into features?

Why did I use both individual words and two-word combinations?

Why is it important to fit the TF-IDF vectorizer only on the training data?

---

### **Logistic Regression**

Why did I choose Logistic Regression as my first baseline model?

What were the model's:

- Accuracy:
- Precision:
- Recall:
- F1 Score:

What did the confusion matrix show?

Were there more fake articles incorrectly classified as real, or more real articles incorrectly classified as fake?

---

### **Naive Bayes**

Why did I choose Naive Bayes as my second baseline model?

What were its:

- Accuracy:
- Precision:
- Recall:
- F1 Score:

How did its results compare to Logistic Regression?

---

### **Model Comparison**

How did the two baseline models perform compared to each other?

Were the differences between the models significant or relatively small?

Did accuracy, precision, recall, and F1 score tell the same story?

What surprised me about the results?

---

### **Important Features**

What words or combinations of words did Logistic Regression associate most strongly with each label?

Do these features make sense based on what I know about the dataset?

Could the model be learning shortcuts or dataset-specific patterns instead of actually learning meaningful misinformation patterns?

---

### **What I Have Learned So Far**

What did I learn about using TF-IDF for text classification?

What did I learn about evaluating machine learning models beyond just accuracy?

What did I learn from comparing two simple models?

---

### **Next Steps**

What do I want to improve after establishing my baseline?

Could different preprocessing methods improve the results?

Could adding my numerical text features improve the models?

What other models or approaches should I test next?