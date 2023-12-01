import google.generativeai as genai

for i, m in zip(range(5), genai.list_tuned_models()):
    print(m.name)