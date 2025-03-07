import os
from gh_activity import GHActivity
from ai_summary import AISummary
from io import StringIO
import sys

def capture_output(func):
    output = StringIO()
    sys.stdout = output
    func()
    sys.stdout = sys.__stdout__
    return output.getvalue()

def main():
    activity = GHActivity(username='rvndyr')
    activity_output = capture_output(activity.print_events)
  
    openai_api_key = os.getenv('OPENAI_API_KEY')
    ai_summarizer = AISummary(api_key=openai_api_key)
    
    summary = ai_summarizer.generate_summary(activity_output)
    print("---")
    print(summary)
    print("---")

if __name__ == '__main__':
    main()