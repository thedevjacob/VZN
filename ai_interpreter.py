# Beginning

import base64
from openai import OpenAI

PROMPTS = {
    'Explain' : "Explain what is contextually seen in the image.",
    'Solve' : "Solve the equation seen in the image, if applicable. Go step by step without explaining your steps.",
    'Describe' : "Describe what is seen in the image, in great detail."
}

GUIDANCE = "Do not write multiple lines. Do not write any formatted/styled/rich text."

class Interpretation:
    def __init__(self, choice, prompt):
        self.prompt = prompt
        self.choice = choice
        self.interpretation_text = choice.message.content

# encode image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def interpret_image(image_path, interpretation_type) -> Interpretation:
    client = OpenAI()
    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": PROMPTS[interpretation_type] + GUIDANCE,
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
    )

    return Interpretation(response.choices[0], PROMPTS[interpretation_type])