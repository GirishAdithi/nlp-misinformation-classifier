# **Phase 3 — Baseline Modeling and Model Improvement**

### **Goal**

> To build a baseline model for classifying fake and real news and then test different approaches to see if I can improve the results.

After cleaning and preprocessing the dataset, I wanted to see how well machine learning models could classify the articles. I started with simple models so I could have a baseline to compare my later experiments against.

---

### **Train/Test Split**

I split the dataset into **80% training data and 20% testing data**. I used stratification so that the proportion of fake and real articles stayed similar in both sets.

I also used a fixed `random_state` so I could reproduce the same split and results.

---

### **TF-IDF**

I used **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert the article text into numerical features that the models could use.

I used both individual words and two-word combinations with `ngram_range=(1, 2)`. I also made sure to fit the TF-IDF vectorizer only on the training data to avoid data leakage from the testing set.

---

### **Baseline Models**

I first tested **Logistic Regression** and **Multinomial Naive Bayes** using the TF-IDF features.

#### **Logistic Regression**

* **Accuracy:** 95.49%
* **Precision:** 95.50%
* **Recall:** 94.39%
* **F1 Score:** 94.94%

Logistic Regression gave me a strong baseline for the project.

#### **Naive Bayes**

* **Accuracy:** 88.21%
* **Precision:** 86.07%
* **Recall:** 87.91%
* **F1 Score:** 86.98%

Naive Bayes performed noticeably lower than Logistic Regression even though both models used the same TF-IDF features.

---

### **Model Improvement Experiments**

After establishing my baseline, I tested different TF-IDF settings, additional features, and another model.

#### **Unigrams**

I tested Logistic Regression using only individual words instead of both words and two-word combinations.

* **Accuracy:** 95.02%
* **Precision:** 95.09%
* **Recall:** 93.73%
* **F1 Score:** 94.41%

The results were slightly lower than my original Logistic Regression model, suggesting that the bigrams provided some useful information.

#### **Text + Numerical Features**

I also tested the additional features I created during preprocessing:

* `word_count`
* `char_count`
* `sentence_count`
* `url_count`
* `exclamation_count`
* `question_count`

The results were:

* **Accuracy:** 91.65%
* **Precision:** 91.31%
* **Recall:** 89.92%
* **F1 Score:** 90.61%

Adding these features actually made the model perform worse. This showed me that adding more features does not necessarily improve a model.

#### **Linear SVM**

I then tested a **Linear SVM** using the TF-IDF features.

* **Accuracy:** 96.68%
* **Precision:** 96.56%
* **Recall:** 96.01%
* **F1 Score:** 96.29%

This was the highest-performing model out of the experiments I tested.

---

### **Comparing the Results**

| Experiment                                      |   Accuracy |  Precision |     Recall |   F1 Score |
| ----------------------------------------------- | ---------: | ---------: | ---------: | ---------: |
| Logistic Regression — Baseline                  |     95.49% |     95.50% |     94.39% |     94.94% |
| Naive Bayes                                     |     88.21% |     86.07% |     87.91% |     86.98% |
| Logistic Regression — Unigrams                  |     95.02% |     95.09% |     93.73% |     94.41% |
| Logistic Regression — Text + Numerical Features |     91.65% |     91.31% |     89.92% |     90.61% |
| Linear SVM                                      | **96.68%** | **96.56%** | **96.01%** | **96.29%** |

The results showed that both the text representation and the model choice affected performance. The original Logistic Regression model performed better with both unigrams and bigrams, while adding my numerical features decreased performance.

The **Linear SVM performed the best** in these experiments, reaching **96.68% accuracy** and a **96.29% F1 score**.
