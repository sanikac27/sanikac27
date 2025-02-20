import feedparser
import markdownify

MEDIUM_RSS_FEED = "https://medium.com/feed/@sanikachougule"

# Fetch Medium RSS Feed
feed = feedparser.parse(MEDIUM_RSS_FEED)

# Get the latest 5 articles
latest_articles = feed.entries[:5]

# Generate Markdown content
md_content = "## 📖 Latest Medium Articles\n"
for article in latest_articles:
    title = article.title
    link = article.link
    md_content += f"- [{title}]({link})\n"

# Read current README.md
with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()

# Replace the placeholder in README
start_marker = "<!-- MEDIUM-ACTIVITY-START -->"
end_marker = "<!-- MEDIUM-ACTIVITY-END -->"
updated_content = content.split(start_marker)[0] + f"{start_marker}\n{md_content}\n{end_marker}" + content.split(end_marker)[1]

# Write back the updated content
with open("README.md", "w", encoding="utf-8") as file:
    file.write(updated_content)
