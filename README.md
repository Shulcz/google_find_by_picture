# Find by picture

This Python program allows you to find visually similar images to a given input image URL using Google Lens. It utilizes the Google Images search functionality to retrieve a list of URLs of images that are visually similar to the provided image.

## Installation

1. Clone this repository to your local machine with:
   ```sh
   git clone https://github.com/Shulcz/google_find_by_picture.git
   ```
2. Navigate to the Repository Directory:
   ```sh
   cd google_find_by_picture
   ```
3. Set up a Virtual Environment (Optional but Recommended):
   ```sh
   python -m venv venv
   ```
 - Activate the virtual environment:
   - **On macOS and Linux:**
   ```sh
   source venv/bin/activate
   ```
4. Install Required Packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Provide the URL of the image you want to find similar images for in the main.py file:
  ```sh
     image_url = <YOUR_URL>
  ```
2. Run the script:
  ```sh
     python main.py
  ```
3. The program will output a list of URLs for images that are visually similar to the provided input image.
