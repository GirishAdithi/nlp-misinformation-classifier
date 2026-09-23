import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load model
MODEL_PATH = "data/transformer_model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

model.eval()


# Page
st.title("Fake News Classifier")

st.write(
    "Paste a news article below and the model will predict "
    "whether it is more likely to be fake or real."
)

article = st.text_area(
    "Article text",
    height=300,
    placeholder="Paste an article here..."
)

# Prediction
if st.button("Predict"):

    if not article.strip():
        st.warning("Please enter an article first.")

    else:

        # Tokenize article
        inputs = tokenizer(
            article,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=256
        )

        # Run model
        with torch.no_grad():
            outputs = model(**inputs)

        # Raw model scores
        logits = outputs.logits

        # Convert scores to probabilities
        probabilities = torch.softmax(logits, dim=1)

        # Get predicted class
        prediction = torch.argmax(
            probabilities,
            dim=1
        ).item()

        # Get confidence
        confidence = probabilities[0][prediction].item() * 100

        # Label mapping
        labels = {
            0: "Fake",
            1: "Real"
        }

        predicted_label = labels[prediction]

        # Display prediction
        st.subheader("Prediction")

        if prediction == 0:
            st.error(
                f"Predicted: FAKE\n\n"
                f"Confidence: {confidence:.2f}%"
            )

        else:
            st.success(
                f"Predicted: REAL\n\n"
                f"Confidence: {confidence:.2f}%"
            )


        # Show probabilities
        st.subheader("Model Probabilities")

        fake_probability = probabilities[0][0].item() * 100
        real_probability = probabilities[0][1].item() * 100

        st.write(f"Fake: {fake_probability:.2f}%")
        st.write(f"Real: {real_probability:.2f}%")


        # -----------------------------
        # Debug information
        # -----------------------------

        with st.expander("Model details"):

            st.write("Raw logits:")
            st.write(logits.tolist())

            st.write("Label mapping:")
            st.write(model.config.id2label)

            st.write("Tokens used:")
            st.write(inputs["input_ids"].shape)

            st.write(
                "The article is truncated to the first 256 tokens "
                "before being classified."
            )


# Disclaimer

st.caption(
    "This model provides a machine-learning prediction based on "
    "patterns learned from the WELFake dataset. It does not verify "
    "whether an article is factually true or false."
)

