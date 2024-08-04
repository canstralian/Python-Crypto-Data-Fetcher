from datasets import Dataset, DatasetDict
from huggingface_hub import Repository

# Initialize a Repository (your space)
repo = Repository(path="https://53c658a4-24e4-498a-a392-b096ecf51246-00-3uyjcmhfkf4h9.pike.replit.dev/")

# Save your dataset to the space
# repo.create_from_datasets(loaded_dataset, name="dataset 2.csv", description="Dataset for sentiment analysis in cryptocurrency.")

# Load your dataset from the space
# loaded_dataset = repo.load_dataset("dataset 2.csv")

# Print the loaded dataset
# loaded_dataset = repo.load_dataset("dataset 2.csv")

# Access individual elements
print(loaded_dataset["text"][0])
print(loaded_dataset["label"][0])

# Iterate over the dataset
for example in loaded_dataset:
    print(example)

# Save the dataset to a file
loaded_dataset.save_to_file("dataset_space.json")

# Load the dataset from a file
loaded_dataset = Dataset.load_from_disk("dataset_space.json")
print(loaded_dataset)


