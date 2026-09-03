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
