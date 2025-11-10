import requests

def get_top_repos(language, per_page=10):
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc&per_page={per_page}"
    response = requests.get(url)
    repos = response.json().get('items', [])
    for repo in repos:
        print(f"{repo['full_name']}: {repo['html_url']}")
        print(f"  Description: {repo['description']}")
        print(f"  Stars: {repo['stargazers_count']}")
        print(f"  Homepage: {repo['homepage']}\n")
        print(f"  README: {repo['html_url']}/blob/main/README.md")
        print("-" * 60)

print("\nTop Python Repositories:\n")
get_top_repos("Python")

print("\nTop C++ Repositories:\n")
get_top_repos("C++")