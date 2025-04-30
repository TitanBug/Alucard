import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_misconfig(description, resource_yaml):
    prompt = f"Explain why this is a misconfiguration: {description}\nResource YAML:\n{resource_yaml}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content
