import kagglehub

# Download latest version
path = kagglehub.model_download("keras/codegemma/keras/code_gemma_2b_en")

print("Path to model files:", path)

# Interface to interact with model
def load_model(model_path):
    from keras.models import load_model as keras_load_model
    model = keras_load_model(model_path)
    return model

model = load_model(path)
print("Model loaded successfully.")