

class HTMLTextModule:

    def __init__(self, url: str):
        self.url = url

    def run(self, dependencies: list) -> dict:
        # Get parsed pages from HTML parser module
        parsed_pages: dict = dependencies[0].copy()

        for url, soup in parsed_pages.items():
            parsed_pages[url] = soup.get_text(separator=' ', strip=True)

        return parsed_pages

        
