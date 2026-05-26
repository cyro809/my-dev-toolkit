from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto("https://example.com")

    page.wait_for_selector(".item")

    items = page.query_selector_all(".item")

    for item in items:
        print(item.inner_text())

    browser.close()