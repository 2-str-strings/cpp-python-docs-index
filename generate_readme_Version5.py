import requests

def get_top_repos(language, per_page=10):
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc&per_page={per_page}"
    response = requests.get(url)
    repos = response.json().get('items', [])
    repo_strings = []
    for repo in repos:
        repo_strings.append(
            f"- [{repo['full_name']}]({repo['html_url']})  \n"
            f"  [README]({repo['html_url']}/blob/main/README.md)  \n"
            f"  {repo['description'] or 'No description.'}\n"
        )
    return repo_strings

def generate_readme():
    md_lines = []
    md_lines.append("# C++ and Python Documentation Index\n")

    # Python Section
    md_lines.append("## Top Python Repositories\n")
    for line in get_top_repos("Python"):
        md_lines.append(line)

    # C++ Section
    md_lines.append("\n## Top C++ Repositories\n")
    for line in get_top_repos("C++"):
        md_lines.append(line)

    # Write to README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

if __name__ == "__main__":
    generate_readme()