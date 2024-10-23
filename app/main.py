from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import requests
from PIL import Image, ImageDraw, ImageFont
import io
import os

app = FastAPI()

# Define the directory to save images
OUTPUT_DIR = "output_images"

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/create_image/")
async def create_image(data: dict):
    try:
        # Extract the URLs and title from the input JSON
        image1_url = data["image1"]
        image2_url = data["image2"]
        title = data["title"]

        # Download the background image
        background_response = requests.get(image1_url)
        background_image = Image.open(io.BytesIO(background_response.content))

        # Download the overlay image
        overlay_response = requests.get(image2_url)
        overlay_image = Image.open(io.BytesIO(overlay_response.content))

        # Resize overlay to fit the background
        overlay_image = overlay_image.resize((background_image.width, background_image.height))

        # Combine background and overlay
        combined = Image.alpha_composite(background_image.convert("RGBA"), overlay_image.convert("RGBA"))
        
        # Add text
        draw = ImageDraw.Draw(combined)
        font = ImageFont.load_default()  # Default font, or specify a custom one
        
        # Position the text (centered)
        text_position = (combined.width // 2 - len(title) * 3, combined.height // 2)
        draw.text(text_position, title, font=font, fill="white")

        # Save to a BytesIO stream
        output = io.BytesIO()
        combined.save(output, format="PNG")
        output.seek(0)

        # Save the image to the specified directory
        output_path = os.path.join(OUTPUT_DIR, "output_image.png")
        combined.save(output_path, format="PNG")

        # Return the image as a StreamingResponse
        return StreamingResponse(output, media_type="image/png")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
