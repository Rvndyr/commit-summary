from openai import OpenAI
from typing import Optional

class AISummary:
    def __init__(self, api_key: Optional[str] = None):
        if not api_key:
            raise ValueError("OpenAI API key is missing")
        self.client = OpenAI(api_key=api_key)
    
    def generate_summary(self, github_activity: str) -> str:
        """
        Generate an AI summary of GitHub activity using OpenAI API
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that summarizes GitHub activity. "
                        "Provide a concise summary of the recent activities."
                    },
                    {
                        "role": "user",
                        "content": f"Can you summarize what this github user is doing on a week to week basis? For each week, write a short summary on what he is working on. This should be a short message for each summary similar to this: March 15, 2024 Deployed a new Kubernetes cluster with ArgoCD for continuous delivery:\n{github_activity}"
                    }
                ],
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"Error generating summary: {str(e)}"