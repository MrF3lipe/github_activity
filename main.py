import requests, json, sys, os
from rich import print as rprint

def get_events(username: str):

    url = f"https://api.github.com/users/{username}/events"

    response = requests.get(url)

    if response.status_code == 200 :
        
        activity = response.json()

        rprint(f"Lasts activities of [bold green]{username}[bold green]:")
        for e in activity:
            if e['type'] == 'IssueCommentEvent':
                rprint(f"- commented on issue in {e['repo']['name']}")
            elif e['type'] == 'PushEvent':
                rprint(f"- pushed to {e['repo']['name']}")
            elif e['type'] == 'IssuesEvent':
                rprint(f"- created issue {e['payload']['issue']['number']}")
            elif e['type'] == 'WatchEvent':
                rprint(f"- starred {e['repo']['name']}")
            elif e['type'] == 'PullRequestEvent':
                rprint(f"- created pull request {e['payload']['pull_request']['number']}")
            elif e['type'] == 'PullRequestReviewEvent':
                rprint(f"- reviewed pull request {e['payload']['pull_request']['number']}")
            elif e['type'] == 'PullRequestReviewCommentEvent':
                rprint(f"- commented on pull request {e['payload']['pull_request']['number']}")
            elif e['type'] == 'CreateEvent':
                rprint(f"- created {e['payload']['ref_type']} {e['payload']['ref']}")
    else:
        rprint(f"Error {response.status_code} fetching activities for [bold green]{username}[bold green]")
if __name__ == "__main__":

    if len(sys.argv) > 1:
        get_events(sys.argv[1])
    else:
        print("Provide the Github username as an argument")