import React, {useState} from 'react';
import './App.css';

const Home = () => {


    const [description, setDescription] = useState(''); // Stores the user input
    const [result, setResult] = useState(null); // Stores the search result
    const [loading, setLoading] = useState(false); // Tracks loading state
    const [error, setError] = useState(null); // Tracks any error

    // Handles form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);

        try {
            // Simulated backend response (replace this with real backend request)
            const mockResponse = await new Promise((resolve) =>
                setTimeout(() => {
                    resolve({
                        message: 'Image data received',
                        imageUrl: 'https://via.placeholder.com/150',
                    });
                }, 2000)
            );

            setResult(mockResponse);
        } catch (err) {
            setError('Failed to fetch image data. Please try again.');
        } finally {
            setLoading(false);
        }
    };




    return (


        <div className="App">
            <h1>Image Search App</h1>

            <form onSubmit={handleSubmit}>
                <label>
                    Enter description:
                    <input
                        type="text"
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        placeholder="Type keywords here..."
                        required
                    />
                </label>
                <button type="submit" disabled={loading}>
                    {loading ? 'Searching...' : 'Search'}
                </button>
            </form>

            {loading && <p>Loading...</p>}

            {error && <p className="error">{error}</p>}

            {result && (
                <div className="result">
                    <h3>{result.message}</h3>
                    <img src={result.imageUrl} alt="Search result"/>
                </div>
            )}
        </div>


    );
};

export default Home;