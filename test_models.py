import torch
from models import get_clip_model, preprocess_image
from PIL import Image

def test_get_clip_model():
    # Specify the local image path
    image_path = r"C:\Users\nachi\Desktop\ThreadConnect\1534.jpg"
    
    try:
        # Open the local image file
        image = Image.open(image_path)
        print("Image loaded successfully from local directory.")
    except FileNotFoundError:
        print(f"Image file not found at {image_path}. Please check the path.")
        return

    # Generate the CLIP embedding
    embedding = get_clip_model(image)

    # Check the embedding dimensions
    assert isinstance(embedding, torch.Tensor), "Output is not a torch.Tensor"
    print("CLIP embedding generated successfully.")
    print("Embedding shape:", embedding.shape)
    print("Embedding values (limited to first 10):", embedding.flatten()[:10].tolist())

if __name__ == "__main__":
    test_get_clip_model()
