# -*- coding: utf-8 -*-
from g4f.client import Client

client = Client()
add_query = "Реши задачу по информатике на python (Только код). "
# gemini, gpt-4o, gpt-4-turbo, GigaChat:latest, gemini-flash, gemini-pro, llama-3.1-70b
response = client.chat.completions.create(
    model="gpt-4o",
    messages=
    [{"role": "user", "content":
        f"""{add_query}
        
        """
    }],
)

answer = response.choices[0].message.content

with open("answer.txt", "w", encoding='utf-8') as f:
    f.write(answer)