r"""
Randy Rodriguez - 3/2025

- This script is a simple Python class that fetches and prints GitHub events for a given user.
There is an option to provide an access token for private repositories.
The class has two methods:
  get_events: Fetches GitHub events for the user.
  print_events: Prints formatted GitHub events.

"""
import requests
import json
from typing import Optional, List, Dict

class GHActivity:
    def __init__(self, username: str = 'rvndyr', access_token: Optional[str] = None):
        self.username = username
        self.access_token = access_token
        self.base_url = 'https://api.github.com'
        
    def _get_headers(self) -> Dict[str, str]:
        headers = {}
        if self.access_token:
            headers['Authorization'] = f'token {self.access_token}'
        return headers
    
    def get_events(self) -> List[Dict]:
        url = f'{self.base_url}/users/{self.username}/events/public'
        response = requests.get(url, headers=self._get_headers())
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve events: {response.status_code}, {response.text}")
    
    def print_events(self) -> None:
        try:
            events = self.get_events()
            if events:
                print(f"GitHub Activity Feed for {self.username}:\n")
                for event in events:
                    print(f"Repo: {event.get('repo', {}).get('name')}")
                    print(f"Event Type: {event.get('type')}")
                    print(f"Commit Author: {event.get('payload', {}).get('commits', [{}])[0].get('author', {}).get('name')}")
                    print(f"Commit Message: {event.get('payload', {}).get('commits', [{}])[0].get('message')}")
                    print(f"Created At: {event.get('created_at')}")
                    print("-" * 80)
            else:
                print(f"No activity found for {self.username}.")
        except Exception as e:
            print(f"Error: {str(e)}")