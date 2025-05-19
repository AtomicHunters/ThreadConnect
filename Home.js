import React, { useState } from 'react';
import './App.css';

const Home = () => {
    const [description, setDescription] = useState(''); // User input description
    const [file, setFile] = useState(null); // Uploaded file
    const [result, setResult] = useState(null); // Backend response
    const [loading, setLoading] = useState(false); // Loading state
    const [error, setError] = useState(null); // Error state

    // Handles form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        setResult(null);

        try {
            const formData = new FormData();

            if (file) {
                // Append the uploaded file
                formData.append('file', file);
            } else if (description) {
                // Append the description
                formData.append('description', description);
            } else {
                setError('Please provide a description or upload an image.');
                setLoading(false);
                return;
            }

            // Simulate backend response (replace with actual API call)
            const mockResponse = await new Promise((resolve) =>
                setTimeout(() => {
                    resolve({
                        message: "Closest matches found",
                        images: [
                            "https://via.placeholder.com/150/0000FF", // Mock image 1
                            "https://via.placeholder.com/150/FF0000", // Mock image 2
                        ],
                    });
                }, 2000)
            );

            setResult(mockResponse);
        } catch (err) {
            setError('Failed to fetch matches. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    // Handle file selection
    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
        setDescription(''); // Clear description if a file is selected
    };

    // Handle description input
    const handleDescriptionChange = (e) => {
        setDescription(e.target.value);
        setFile(null); // Clear file if a description is entered
    };

    return (
        <div className="App">
            <h1>Image Search App</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>
                        Enter a description:
                        <input
                            type="text"
                            value={description}
                            onChange={handleDescriptionChange}
                            placeholder="Type keywords here..."
                            disabled={!!file} // Disable if a file is selected
                        />
                    </label>
                </div>
                <p>OR</p>
                <div>
                    <label>
                        Upload an image:
                        <input
                            type="file"
                            accept="image/*"
                            onChange={handleFileChange}
                            disabled={!!description} // Disable if a description is entered
                        />
                    </label>
                </div>
                <button type="submit" disabled={loading}>
                    {loading ? 'Searching...' : 'Search'}
                </button>
            </form>

            {loading && <p>Loading...</p>}
            {error && <p className="error">{error}</p>}

            {result && (
                <div className="result">
                    <h3>{result.message}</h3>
                    <div className="image-grid">
                        {result.images.map((imageUrl, index) => (
                            <img key={index} src={imageUrl} alt={`Result ${index + 1}`} />
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
};

export default Home;
