import React from "react";

const Image_Upload = () => {
    return (


        /* Page for retailers to upload their own styles into our database*/
        <div style={{textAlign: "center", padding: "20px"}}>
            <div style={{marginBottom: "20px"}}>
                <h1>For Retailers</h1>
            </div>
            <div style={{marginTop: "0", fontSize: "1rem", color: "#666"}}>
                Application for retailers that wish to upload their products to expand our AI and give customers more
                sustainable, trusted sources.
            </div>

            <div style={{marginTop: "40px"}}></div>


            <form style={{maxWidth: "600px", margin: "0 auto", textAlign: "left"}}>
                {/* Company Name */}
                <div style={{marginBottom: "15px"}}>
                    <label htmlFor="companyName" style={{display: "block", marginBottom: "5px"}}>
                        Company Name:
                    </label>
                    <input
                        type="text"
                        id="companyName"
                        name="companyName"
                        style={{width: "100%", padding: "8px", fontSize: "1rem"}}
                        placeholder="Enter your company name"
                    />
                </div>

                {/* Company Email */}
                <div style={{marginBottom: "15px"}}>
                    <label htmlFor="companyEmail" style={{display: "block", marginBottom: "5px"}}>
                        Company Email:
                    </label>
                    <input
                        type="email"
                        id="companyEmail"
                        name="companyEmail"
                        style={{width: "100%", padding: "8px", fontSize: "1rem"}}
                        placeholder="Enter your company email"
                    />
                </div>

                {/* Products Offered */}
                <div style={{marginBottom: "15px"}}>
                    <label htmlFor="productsOffered" style={{display: "block", marginBottom: "5px"}}>
                        Products Offered:
                    </label>
                    <input
                        type="text"
                        id="productsOffered"
                        name="productsOffered"
                        style={{width: "100%", padding: "8px", fontSize: "1rem"}}
                        placeholder="Products you offer"
                    />
                </div>

                {/* Sustainability Question */}
                <div style={{marginBottom: "15px"}}>
                    <label htmlFor="sustainability" style={{display: "block", marginBottom: "5px"}}>
                        How are you a sustainable business?
                    </label>
                    <textarea
                        id="sustainability"
                        name="sustainability"
                        style={{width: "100%", padding: "8px", fontSize: "1rem", height: "100px"}}
                        placeholder="Explain how your business practices sustainability"
                    />
                </div>

                {/* Submit Button */}
                <div style={{textAlign: "center", marginTop: "20px"}}>
                    <button
                        type="button"
                        style={{
                            padding: "10px 20px",
                            fontSize: "1rem",
                            backgroundColor: "#4CAF50",
                            color: "white",
                            border: "none",
                            borderRadius: "5px",
                            cursor: "pointer",
                        }}
                    >
                        Submit
                    </button>
                </div>
            </form>


        </div>


    );
};

export default Image_Upload;
