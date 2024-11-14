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

def preprocess_image(file) -> Image.Image:
    """Preprocesses the image uploaded via Flask request."""
    image = Image.open(BytesIO(file.read()))
    return image
