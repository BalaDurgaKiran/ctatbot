import openai

openai.api_key = "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"
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content": prompt}] 
    )

    return response.choices[0].message.content.strip()

