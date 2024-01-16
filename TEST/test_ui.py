from playwright.sync_api import Page, expect

#successful login and logout
def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("problem_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()