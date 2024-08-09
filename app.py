import streamlit as st
import requests
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Function to call Google Gemini API
def analyze_code_with_gemini_api(code):
    api_key = os.getenv("GOOGLE_API_KEY")
    
    
    # Payload to send to the API
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f"Analyze the following code and provide its time and space complexity along with optimization suggestions: {code}"}
                ]
            }
        ]
    }
    
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(api_key, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to analyze code. Status code: {response.status_code}, Response: {response.text}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

# Streamlit app
def main():
    st.title("Code Reviewer")
    
    
    # Input field for code
    code = st.text_area("Enter your code here:", height=300)
    
    # Button to trigger analysis
    if st.button("Analyze Code"):
        if code:
            # Call the function to analyze the code using the API
            analysis = analyze_code_with_gemini_api(code)
            
            # Display the results
            if "error" in analysis:
                st.error(analysis["error"])
            else:
                st.subheader("Analysis Result:")
                # Assuming the response contains a field 'generatedText' which holds the AI's response.
                for content in analysis.get("contents", []):
                    for part in content.get("parts", []):
                        st.write(part.get("text", "No text generated."))
        else:
            st.error("Please enter some code to analyze.")

if __name__ == "__main__":
    main()
