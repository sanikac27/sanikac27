import feedparser

MEDIUM_RSS_FEED = "https://medium.com/feed/@sanikaschougule"

def get_medium_articles():
    feed = feedparser.parse(MEDIUM_RSS_FEED)
    articles = []
    
    for entry in feed.entries[:5]:  # Get the latest 5 articles
        title = entry.title
        url = entry.link
        articles.append(f"- [{title}]({url})")

    return articles

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

if start_marker in content and end_marker in content:
    updated_content = content.split(start_marker)[0] + f"{start_marker}\n{new_content}\n{end_marker}" + content.split(end_marker)[1]
else:
    updated_content = content + f"\n\n{start_marker}\n{new_content}\n{end_marker}"

# Write back the updated content
with open("README.md", "w", encoding="utf-8") as file:
    file.write(updated_content)

print("README.md updated successfully!")
