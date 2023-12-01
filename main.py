import google.generativeai as genai

from load_creds import load_creds

creds = load_creds()

genai.configure(credentials=creds)

chat_prompt = """product_name: MagicMobile
product_description: Introducing MagicMobile, the future of transportation and communication combined! Seamlessly switch between a high-end mobile phone and a stylish five-wheeled car. With cutting-edge technology and a dash of magic, MagicMobile adapts to your needs, wherever you are.
reviewer: Henry Paddock"""

completion = genai.generate_text(
                model=f'tunedModels/devfesthkprodreviews-p989bn7rdqwf',
                prompt=chat_prompt
            )

print(completion.result)