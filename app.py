from flask import Flask, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Define the home route
@app.route("/")
def home():
    return "Welcome to the default Flask app!"

# Add a simple health check route
@app.route("/health")
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    # Run the Flask app
    app.run(port=5000) 
models.py:import open_clip
import torch
from PIL import Image
from io import BytesIO

# Load the CLIP model architecture and preprocessing transforms
model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained=None)

# Load the custom weights
model_link = r'C:\Users\nachi\Desktop\ThreadConnect\finetuned_clip_model_weights1for_loss_0.13254774100542496.pth'
state_dict = torch.load(model_link, map_location=torch.device('cpu'))
model.load_state_dict(state_dict)
model.eval()  # Set model to evaluation mode

def get_clip_model(image: Image.Image) -> torch.Tensor:
    """Generates the CLIP embedding for an image."""
    image_tensor = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        # Generate the image embedding
        query_vector = model.encode_image(image_tensor)
    return query_vector

def preprocess_image(file) -> Image.Image:
    """Preprocesses the image uploaded via Flask request."""
    image = Image.open(BytesIO(file.read()))
    return image
