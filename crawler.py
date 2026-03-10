from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urljoin, urlparse

def crawl(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        data = {
            "url": url,
            "metadata": {},
            "headings": {},
            "content": {},
            "links": {"internal": [], "external": []},
            "images": [],
            "seo_features": {}
        }

        # Metadados

        title = soup.title.string.strip() if soup.title else None
        data["metadata"]["title"] = title

        meta_desc = soup.find("meta", attrs={"name": "description"})
        data["metadata"]["meta_description"] = (
            meta_desc.get("content").strip() if meta_desc else None
        )

        canonical = soup.find("link", rel="canonical")
        data["metadata"]["canonical"] = canonical.get("href") if canonical else None

        # Headings

        for tag in ["h1", "h2", "h3"]:
            data["headings"][tag] = [
                h.get_text(strip=True) for h in soup.find_all(tag)
            ]

        # Content

        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text(separator=" ", strip=True)

        data["content"]["text"] = text
        data["content"]["word_count"] = len(text.split())

        # Links

        domain = urlparse(url).netloc

        for link in soup.find_all("a", href=True):

            href = link["href"]
            full_url = urljoin(url, href)

            if domain in urlparse(full_url).netloc:
                data["links"]["internal"].append(full_url)
            else:
                data["links"]["external"].append(full_url)

        # Images

        for img in soup.find_all("img"):

            data["images"].append({
                "src": img.get("src"),
                "alt": img.get("alt")
            })

        # SEO features

        data["seo_features"] = {
            "title_length": len(title) if title else 0,
            "meta_description_length": len(data["metadata"]["meta_description"])
            if data["metadata"]["meta_description"] else 0,
            "h1_count": len(data["headings"]["h1"]),
            "h2_count": len(data["headings"]["h2"]),
            "internal_link_count": len(data["links"]["internal"]),
            "external_link_count": len(data["links"]["external"]),
            "image_count": len(data["images"]),
            "images_without_alt": sum(
                1 for img in data["images"] if not img["alt"]
            )
        }

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


if __name__ == "__main__":

    url = "https://www.taqtile.com.br/"

    page_data = crawl(url)

    if page_data:
        print(json.dumps(page_data, indent=2, ensure_ascii=False))