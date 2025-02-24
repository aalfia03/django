import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("http://localhost:8000/Klients/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Api Root"))

def test_get_started_link(page: Page):
    page.goto("http://localhost:8000/Klients/")

    # Click the get started link.
    page.get_by_role("link", name="Get").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Api Root")).to_be_visible()