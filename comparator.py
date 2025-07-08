from playwright.sync_api import sync_playwright
from llm_matcher import is_match

def fetch_flipkart(query):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://www.flipkart.com/search?q={query.replace(' ', '+')}")
        page.wait_for_timeout(4000)

        products = []
        items = page.query_selector_all("._1AtVbE")

        for item in items:
            title = item.query_selector("div._4rR01T")
            price = item.query_selector("div._30jeq3")
            link = item.query_selector("a")

            if title and price and link:
                title_text = title.inner_text()
                price_text = price.inner_text().replace("₹", "").replace(",", "")
                url = "https://www.flipkart.com" + link.get_attribute("href")

                if is_match(query, title_text):
                    products.append({
                        "productName": title_text,
                        "price": price_text,
                        "currency": "INR",
                        "link": url,
                        "seller": "Flipkart"
                    })
        browser.close()
        return products

def compare_prices(country, query):
    if country.upper() == "IN":
        return fetch_flipkart(query)
    return []
