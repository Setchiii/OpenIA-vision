import base64
import requests
from change_format import change_format

# OpenAI API Key
with open("api_key.txt", "r") as file:
    api_key = file.read()


# encore the image to base64


def encode_image(image_path):
    with open(image_path, "rb") as file:
        image = file.read()
        return base64.b64encode(image).decode("utf-8")


# Path to your image
image_path = "test.bmp"


# Getting the base64 string
if image_path.endswith(".bmp"):
    image_path = change_format(image_path)
base64_image = encode_image(image_path)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "In the red circle in the center of the image, how many white dots are there?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    "max_tokens": 300
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())
