# Image Translator HTTP API

This project utilizes optical character recognition (OCR) and translation to translate text within images from one language to another via an HTTP API. It performs the following steps:

1. **OCR Processing:** The project extracts text and its bounding boxes from input images using the EasyOCR library.
2. **Translation:** It translates the extracted text using the Google Translator API.
3. **Text Replacement:** The translated text is then overlaid onto the image, replacing the original text while maintaining its position and style.
4. **Output:** Finally, the modified image with translated text is saved to an output folder.

## Setup

### Installation

1. Clone this repository to your local machine.
2. To use a Python virtual environment:
   - Create a new virtual environment by running:
     `python -m venv env`
   - Activate the virtual environment:
     - On Linux/Unix or macOS, run:
       `source env/bin/activate`
     - On Windows, run:
       `env\Scripts\activate`
   - Install the required dependencies:
     `pip install -r requirements.txt`

### Docker Setup

The API can also be served via Docker. The project includes both a Dockerfile and a docker-compose.yaml file. To run the API using Docker:

1. Ensure Docker and docker-compose are installed on your machine.
2. In the project directory, run:
   `docker-compose up`

## Usage

1. Place your input images in the `input` folder.
2. Start the HTTP API:
   - If using Python directly, run:
     `python main.py`
   - If using Docker, the API will be available as configured in docker-compose.yaml.
3. Use your preferred HTTP client (e.g., curl, Postman) to send requests to the API endpoints.
4. Translated images will be saved in the `output` folder.

## API Security

- If you set the environment variable `API_KEY`, the API will be protected with an API key.
- To authenticate your requests, include the API key in the header `x-api-key` when sending requests to the endpoints.

## API Endpoint

- To translate an image, call the endpoint:
  `/translate/image/{from_lang}/{to_lang}`  
  (`{from_lang}` and `{to_lang}` must be replaced with languages found in the class `src/classes/languages.py`)

- The request should be a POST request with a multipart/formdata body containing
  the image to translate. The name of the image file in the form-data must be:
  `file`

## Notes

- Supported languages are defined in the file `src/classes/languages.py`.

## Examples

![image-1](https://github.com/boysugi20/python-image-translator/assets/53815726/cc2a52b3-2627-4f08-a428-c0dba4341bda)  
![image-1-translated](https://github.com/boysugi20/python-image-translator/assets/53815726/3ecafe2e-df19-4ca2-aeff-b05cc89394db)

## Acknowledgments

- [EasyOCR](https://github.com/JaidedAI/EasyOCR) - For OCR processing.
- [Google Translator](https://pypi.org/project/deep-translator/) - For text translation.
- [Pillow (PIL Fork)](https://python-pillow.org/) - For image manipulation.
- [boysugi20/python-image-translator](https://github.com/boysugi20/python-image-translator) - For the base project.