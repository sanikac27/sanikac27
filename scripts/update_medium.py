import requests
from bs4 import BeautifulSoup

MEDIUM_PROFILE = "https://medium.com/@sanikaschougule"

def get_medium_articles():
    response = requests.get(MEDIUM_PROFILE)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for link in soup.find_all("a", {"data-action": "open-post"}):
        title = link.text.strip()
        url = link["href"]
        if not url.startswith("http"):
            url = "https://medium.com" + url
        articles.append(f"- [{title}]({url})")

    return articles[:5]  # Get the latest 5 articles

latest_articles = get_medium_articles()

if latest_articles:
    new_content = "## 📖 Latest Medium Articles\n" + "\n".join(latest_articles)
else:
    new_content = "## 📖 Latest Medium Articles\nNo articles found."

# Read current README.md
with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()

# Replace placeholders in README.md
start_marker = "<!-- MEDIUM-ACTIVITY-START -->"
end_marker = "<!-- MEDIUM-ACTIVITY-END -->"
updated_content = content.split(start_marker)[0] + f"{start_marker}\n{new_content}\n{end_marker}" + content.split(end_marker)[1]

# Write back the updated content
with open("README.md", "w", encoding="utf-8") as file:
    file.write(updated_content)
