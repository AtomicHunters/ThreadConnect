from flask import Flask, jsonify, request
from PIL import Image
from io import BytesIO

from scripts.regsetup import description

from models import find_similar_images, get_clip_text, find_similar_desc
import os

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

def preprocess_image(file) -> Image.Image:
    """Preprocesses the image uploaded via Flask request."""
    image = Image.open(BytesIO(file.read()))
    return image

#These set up a folder to store the uploaded files
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok= True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Set the types of images that are allowed
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods =['POST'])
def upload_image():
    # Check if the request contains a file
    if 'image' not in request.files:
        return jsonify({'error': 'No image file in request'}), 400

    # Get the image and make sure the file is the correct type
    image_file = request.files['image']
    if not allowed_file(image_file.filename):
        return jsonify({'error': 'Invalid file type'}), 400

    # Save the file
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
        image_file.save(file_path)

    #If there is an error, catch it, and return the error
    except Exception as e:
        return jsonify({'error':f'Failed to save file: {str(e)}'}),500

    search_results = find_similar_images(image_file.filename)

    filepaths = [], descriptions = [], product_ids = [], similarity_scores = []
    i = 1

    for result in search_results:
        payload = result.payload
        similarity_score = result.score

        filepaths[i] = payload['file_path']
        descriptions[i] = payload['description']
        product_ids[i] = payload['product_id']
        similarity_scores[i] = similarity_score

    result_json = {
        "filepaths": filepaths,
        "descriptions": descriptions,
        "product_ids": product_ids,
        "similarity_score":similarity_scores
    }

    return jsonify(result_json)


@app.route('/text', methods =['POST'])
def upload_text():
    #Parse the text as a json into text
    data = request.get_json()

    #Get the data in the text field
    text = data.get('text','')

    #Get the embeddings for the text
    search_results = find_similar_desc(text)

    filepaths = [], descriptions = [], product_ids = [], similarity_scores = []
    i = 1

    for result in search_results:
        payload = result.payload
        similarity_score = result.score

        filepaths[i] = payload['file_path']
        descriptions[i] = payload['description']
        product_ids[i] = payload['product_id']
        similarity_scores[i] = similarity_score

    result_json = {
        "filepaths": filepaths,
        "descriptions": descriptions,
        "product_ids": product_ids,
        "similarity_score": similarity_scores
    }

    #Return the embedding for testing. Will need to instead send this to the database and return what is given from there.
    return jsonify(result_json)
