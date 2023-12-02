import google.generativeai as genai
from google.generativeai.types.model_types import TunedModelState
import random
import csv
import time

from load_creds import load_creds

creds = load_creds()

genai.configure(credentials=creds)

name = f'curious-google-{random.randint(0,10000)}'

data = []
with open("data/curious-small.csv", mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append({
            'text_input': row['question'],
            'output': row['answer']
        })

print(name)

operation = genai.create_tuned_model(
    source_model='models/text-bison-001',
    training_data=data,
    id = name,
    epoch_count = 100,
    batch_size=64,
    learning_rate=0.001,
)

model = genai.get_tuned_model(f'tunedModels/{name}')

while model.state == TunedModelState.CREATING:
    print(model.state)
    time.sleep(5)

print("Training completed.")
print(model.state)


