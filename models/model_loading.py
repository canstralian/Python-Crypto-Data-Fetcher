from transformers import BertTokenizer, BertForSequenceClassification

# Load tokenizer and model
tokenizer = BertTokenizer.from_pretrained("kk08/CryptoBERT")
model = BertForSequenceClassification.from_pretrained("kk08/CryptoBERT")

# Function to preprocess text
def preprocess_text(text):
  