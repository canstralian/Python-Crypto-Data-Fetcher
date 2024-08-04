from datasets import Dataset

# Example data
data = {
    "text": ["Bitcoin is surging!", "Ethereum faces regulatory challenges."],
    "label": [1, 0]  # 1 for positive, 0 for negative sentiment
}

# Create a Dataset object
dataset = Dataset.from_dict(data)
# Print the dataset
print(dataset)

# Accessing the data
print(dataset["text"])
print(dataset["label"])

# Accessing individual elements
print(dataset["text"][0])
print(dataset["label"][0])

# Iterating over the dataset
for example in dataset:
    print(example)

# Saving the dataset to a file
dataset.save_to_file("hugging_data.json")

# Loading the dataset from a file
loaded_dataset = Dataset.load_from_file("hugging_data.json")
print(loaded_dataset)