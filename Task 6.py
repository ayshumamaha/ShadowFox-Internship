from html.parser import HTMLParser

# Sample HTML page
html = """
<html>
<head>
    <title>ShadowFox Internship</title>
</head>
<body>
    <h1>Python Development Internship</h1>
    <p>Learn web scraping using Python.</p>
    <a href="https://shadowfox.in">Visit Website</a>
</body>
</html>
"""

class MyScraper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_h1 = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True
        if tag == "h1":
            self.in_h1 = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "h1":
            self.in_h1 = False

    def handle_data(self, data):
        if self.in_title:
            print("Website Title:", data)
        if self.in_h1:
            print("Main Heading:", data)

scraper = MyScraper()
scraper.feed(html)
