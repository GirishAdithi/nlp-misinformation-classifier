# **Phase 5 — Error Analysis**

### **Goal**

> To understand where my best model makes mistakes and look for patterns in those mistakes.

### **Model Errors**

I used the Linear SVM from Phase 4 and looked at the articles it classified incorrectly. I separated the errors into **real articles predicted as fake** and **fake articles predicted as real**.

I also looked at the model's decision scores to see how confident it was when making incorrect predictions. This helped me find both uncertain mistakes and mistakes where the model was more confident.

### **Looking at the Articles**

I manually looked at some of the incorrectly classified articles and their titles. I also compared things like article length and word count between correctly and incorrectly classified articles.

This helped me see that some articles can be difficult to classify based only on their text, especially when the writing style or wording is similar between fake and real news.

### **What I Found**

The error analysis gave me a better idea of where the model struggles instead of only looking at its overall accuracy. It also showed me that even with a high accuracy, there are still cases where the model can confidently make the wrong prediction.
