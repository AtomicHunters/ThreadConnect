import os
import pandas as pd
import random
from qdrant_client import QdrantClient
from PIL import Image
import torch
import open_clip

# Qdrant Cloud credentials
url = "https://c76b9de4-57dd-4d26-b97d-58e26fa20663.us-east4-0.gcp.cloud.qdrant.io"  # Replace with your Qdrant URL
api_key = "vskDD12BlMjBR7sz1uOExbYA6IiSjm7fsSxFAcIJoAT54VuLTlBXhw"  # Replace with your API key

# Initialize Qdrant client
db_client = QdrantClient(url=url, api_key=api_key)

# Load the CLIP model architecture and preprocessing transforms
model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained=None)
tokenizer = open_clip.get_tokenizer('ViT-B-32')

# Load the custom weights
model_link = r'finetuned_clip_model_weights1for_loss_0.13254774100542496.pth'
state_dict = torch.load(model_link, map_location=torch.device('cpu'))
model.load_state_dict(state_dict)
model.eval()  # Set model to evaluation mode

# Directory where images are stored
image_folder = r"images"  # Replace with the path to your images folder

# Load CSV file
csv_file = r"styles_fix.csv"  # Replace with the path to your CSV file
df = pd.read_csv(csv_file)

# Select only required columns: 'id' and 'productDisplayName'
df = df[['id', 'productDisplayName']]


def get_clip_model(image: Image.Image) -> torch.Tensor:
    """Generates the CLIP embedding for an image."""
    image_tensor = preprocess(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        # Generate the image embedding
        query_vector = model.encode_image(image_tensor)
        return query_vector.squeeze(0).tolist()  # Convert to list for Qdrant compatibility


def get_clip_text(text):
    # Tokenize the input
    txt = tokenizer([text])[0]

    # Generates the embedding with the text
    with torch.no_grad():
        query_vector = model.encode_text(txt)
    return query_vector.squeeze(0).tolist()


def upload_to_qdrant(image_path: str, product_id: int, description: str):
    """Uploads image embedding to Qdrant."""
    try:
        # Open image
        image = Image.open(image_path)

        # Generate embedding
        embedding = get_clip_model(image)

        # Generate a unique point ID
        point_id = product_id

        # Insert into Qdrant
        db_client.upsert(
            collection_name="image_embeddings",
            points=[
                {
                    "id": point_id,
                    "vector": embedding,
                    "payload": {
                        "file_path": image_path,
                        "product_id": product_id,
                        "description": description
                    }
                }
            ]
        )
        print(f"Uploaded: {image_path} with ID {product_id} and description '{description}'")
    except Exception as e:
        print(f"Failed to upload {image_path}: {e}")


def process_and_upload_all_images():
    """Processes all images and uploads them to Qdrant."""
    for index, row in df.iterrows():  # Iterate over all rows in the DataFrame
        product_id = row['id']
        description = row['productDisplayName']
        image_path = os.path.join(image_folder, f"{product_id}.jpg")  # Construct image path

        # Check if the image exists
        if os.path.exists(image_path):
            upload_to_qdrant(image_path, product_id, description)
        else:
            print(f"Image not found: {image_path}")


def find_similar_images(new_image_path: str, top_k: int = 5):
    """Finds the top-k most similar images to the new image in the Qdrant database."""
    try:
        # Open the new image
        new_image = Image.open(new_image_path)

        # Generate the embedding for the new image
        new_embedding = get_clip_model(new_image)

        # Perform a similarity search in Qdrant
        search_results = db_client.search(
            collection_name="image_embeddings",
            query_vector=new_embedding,
            limit=top_k,  # Number of results to return
            with_payload=True  # Retrieve payloads with results
        )

        return search_results

    except Exception as e:
        print(f"Failed to find similar images: {e}")

def find_similar_desc(new_text: str, top_k: int = 5):
    try:
        new_embedding = get_clip_text(new_text)

        # Perform a similarity search in Qdrant
        search_results = db_client.search(
            collection_name="text_embeddings",
            query_vector=new_embedding,
            limit=top_k,  # Number of results to return
            with_payload=True  # Retrieve payloads with results
        )

        return search_results

    except Exception as e:
        print(f"Failed to find similar descriptions: {e}")

if __name__ == "__main__":
    query_image_path = r"1534.jpg"
    find_similar_images(query_image_path)
