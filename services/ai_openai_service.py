import os

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

class OpenAIAssistant:
    @staticmethod
    def generate(prompt: str) -> str:
        api_key = os.getenv("OPENAI_API_KEY")

        # SAFE FALLBACK (no key required)
        if not api_key or OpenAI is None:
            return (
                "AI Assistant (Simulated): Based on current data trends, "
                "focus should be placed on reducing high-severity incidents "
                "and improving response times."
            )

        client = OpenAI(api_key=api_key)
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a cybersecurity analyst."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=120
        )
        return resp.choices[0].message.content
