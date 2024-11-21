from flask import Flask, request, jsonify
import os
from PIL import Image
from models import get_clip_model, get_clip_text


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

    # Set the image to the filepath for the saved image
    image = Image.open(image_file.filename)

    # Now embed the images using the image
    embedding = get_clip_model(image)

    # Return the embedding for testing. Will need to instead send this to the database and return what is given from there.
    return embedding

@app.route('/text', methods =['POST'])
def upload_text():
    #Parse the text as a json into text
    data = request.get_json()

    #Get the data in the text field
    text = data.get('text','')

    #Get the embeddings for the text
    embedding = get_clip_text(text)

    #Return the embedding for testing. Will need to instead send this to the database and return what is given from there.
    return embedding
