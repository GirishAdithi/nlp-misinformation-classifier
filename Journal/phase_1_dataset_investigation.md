# **Data**

### Finding the Dataset

Finding a credible raw dataset is one of the challenges I faced because most datasets were already preprocessed or did not have enough credibility. I found a credible dataset supported by the European Union's Horizon project: the [WELFake dataset for fake news detection in text data](https://zenodo.org/records/4561253).

I also liked this dataset because it isn't perfectly clean, and I can use my machine learning skills (learned in my course *CSE 40: Machine Learning Basics*) to investigate and enhance it with additional text-based features and processed columns to aid my models.

### **Goal**

> To understand the raw WELFake dataset, identify the problems or patterns in it, and clean it thoroughly to prepare it for modeling.

---

### **Initial Investigation**

I loaded the dataset using Pandas and examined its structure, columns, data types, and sample entries. The dataset contains **72,134 articles** with two labels:

- **0 = Fake**
- **1 = Real**

The labels are relatively balanced:

- **35,028** articles are labeled as fake.
- **37,106** articles are labeled as real.

This is a good starting point because there is not a major imbalance between the two classes.

### **Missing Data**

I checked the dataset for missing values, particularly in the `title` and `text` columns. Some articles are missing information, which is important since the article text will be one of the main features used by my models.

I will most likely remove the missing values or maybe replace them with placeholders if it isn't very crucial.

### **Duplicate Data**

I also checked for duplicate rows, titles, and article text. This is important because duplicate or repeated articles could cause **data leakage** if similar examples appear in both the training and testing sets.

I will use the results of these checks to determine how duplicates should be handled during preprocessing.

### **Article Length and Labels**

I created additional features for the number of characters and words in each article. I then compared article length between the two labels.

The articles have a wide range of lengths. The median article is approximately **395 words**, while some articles are much longer, with the maximum extending to **over 14,000 words**.

I visualized the article-length distributions for fake and real news. The distributions overlap substantially, although there are some differences between the two groups.

This investigation is useful because I want to determine whether **article length could become a shortcut for the model**. If one label consistently contained much shorter or longer articles, the model could potentially rely on length instead of learning meaningful linguistic patterns related to misinformation.

### **What I Have Learned So Far**

My initial investigation has shown me that the dataset cannot simply be treated as ready for modeling. There are several factors I need to consider, including missing information, duplicates, article-length differences, and potential sources of bias or data leakage.

I also learned that feature engineering can help during dataset investigation. Creating features such as word count allows me to better understand the data while identifying patterns that could affect model performance.

---

# **Phase 2 — Cleaning and Preprocessing**

### **Goal**

> To prepare the raw WELFake dataset for modeling by cleaning unnecessary information, processing the text, and creating useful features while keeping the original dataset unchanged.

After investigating the dataset, I started cleaning and preprocessing the data based on what I found during the investigation. I decided to create a separate processed dataset instead of changing the original dataset so that I can always go back to the raw data if needed.

### **Handling Missing Data**

First, I handled the missing values in the `title` and `text` columns. I replaced missing values with empty strings and removed articles that did not have any usable text since the text is necessary for my classification models.

I decided that keeping an article with no text would not be useful for a text-based classifier because there would not be enough information for the model to learn from.

### **Removing Duplicates**

I then removed duplicate articles based on their text. I did this because having the same article multiple times could affect the model and potentially cause data leakage when splitting the data into training and testing sets.

### **Combining Title and Text**

I combined the title and article text into a new `full_text` column. I decided to keep the title because headlines can contain useful information when identifying fake news.

This also gives the model more information instead of only using the article body.

### **Text Preprocessing**

I applied several text preprocessing steps to the combined text. I converted all text to lowercase, removed HTML tags, replaced URLs with a `URL` token, removed numbers and punctuation, and normalized extra spaces.

I wanted to reduce unnecessary formatting differences while keeping the actual language of the articles.

After the basic cleaning, I tokenized the text and removed common English stopwords. I also used lemmatization to reduce words to their base forms.

For example, different forms of the same word can be reduced to a more common representation. This should help reduce unnecessary variation in the vocabulary that the models have to process.

### **Feature Engineering**

I also created additional numerical features from the articles, including:

- `word_count`
- `char_count`
- `sentence_count`
- `url_count`
- `exclamation_count`
- `question_count`

I wanted to keep these features because some of the patterns I found during my investigation, such as article length and formatting, could potentially be useful for the models.

Having these features separately will also allow me to compare their usefulness later instead of assuming that they are important.

### **Final Dataset**

After preprocessing, I checked the dataset again for missing values, duplicates, and the label distribution to make sure that the cleaning process did not introduce any major issues.

I then saved the processed dataset separately as `WELFake_processed.csv` inside the `data/processed/` folder.

I kept the original dataset unchanged so that I can compare my preprocessing choices and reproduce my work later.

### **What I Learned**

This phase helped me understand that preprocessing is not just about making the dataset cleaner. Every decision can change the information that the model has access to.

For example, removing punctuation, numbers, or URLs could also remove patterns that might be useful for detecting misinformation. Because of this, I want to compare different approaches during the modeling stage instead of assuming that my preprocessing method will automatically give the best results.

I also learned the importance of keeping the raw dataset separate from the processed dataset. This makes it easier to go back and change my preprocessing decisions without losing the original data.

With the dataset now investigated and preprocessed, I am ready to move on to building my first baseline model.
Ad