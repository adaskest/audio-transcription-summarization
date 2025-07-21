import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize(text: str, summary_path: str) -> str:
    os.makedirs(os.path.dirname(summary_path), exist_ok=True)
    
    prompt = (
        "Sutrumpink šį tekstą lietuvių kalba ir pateik aiškią santrauką. Santrauka turėtų būti pusia teksto ilgio:\n\n"
        f"{text}\n\nSantrauka:"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7,
        )
        summary = response.choices[0].message.content.strip()

        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary)

        return summary

    except Exception as e:
        return f"Error while calling OpenAI API: {str(e)}"
