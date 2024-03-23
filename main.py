import openai

openai.api_key = ""
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content": prompt}] 
    )

    return response.choices[0].message.content.strip()

