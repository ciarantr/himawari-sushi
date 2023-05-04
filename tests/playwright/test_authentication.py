from playwright.sync_api import Page, expect, BrowserContext, BrowserType
import random

# URLs
register_url = 'register/'
login_url = 'login/'
home_page = 'http://127.0.0.1:8000/'

# User credentials
# make a username with a random number at the end
user = 'testuser' + str(random.randint(1, 100))
email = 'test@gmail.cpm'
password = 'testpassword@@'


def test_registration_success(page: Page):
    """
    Test registration success

    1. Go to home page
    2. Click on login link
    3. Check if the user is redirected to register page
    4. Fill in the form
    5. Click on register button
    6. Check if the user is redirected to home page
    7. Check if the user is logged in
    8. Check if username is displayed in the account menu

    """
    page.goto(home_page)
    page.get_by_role("link", name="Sign up").click()
    page.wait_for_load_state('domcontentloaded')
    expect(page).to_have_url(home_page + register_url)

    # fill in the registration form & click on sign up button
    page.fill('input[name="username"]', user)
    page.fill('input[name="email"]', email)
    page.fill('input[name="password1"]', password)
    page.fill('input[name="password2"]', password)
    page.click('text="Sign up"')
    # wait for page to load & check if the user is redirected to home page
    page.wait_for_load_state('domcontentloaded')
    expect(page).to_have_url(home_page)

    # validate registration success alert message
    alert_message = page.locator('div[role="alert"] li')
    expect(alert_message).to_have_text(
        "Account created successfully"
    )
    # validate account menu name is displayed
    account_menu = page.locator('#account-menu')
    expect(account_menu).to_contain_text(f"Hi {user}")


def test_registration_mobile_pass(page: Page):
    """
    Test registration success with mobile device

    1. Go to home page
    2. Click on mobile menu button & validate mobile menu is displayed
    3. Click on Sign up link
    4. Check if the user is redirected to register page
    5. Fill in the form
    6. Click on register button
    7. Check if the user is redirected to home page
    8. Check if the user is logged in & navigate to profile page

    """
    # set device to mobile
    page.set_viewport_size({'width': 375, 'height': 812})
    # go to home page & click on mobile menu button
    page.goto(home_page)
    mobile_button = page.locator('button[id="nav-button"]')
    mobile_button.click()

    # validate aria-expanded attribute
    expect(mobile_button).to_have_attribute('aria-expanded', 'true')

    # First, get a reference to the nav element
    nav_menu = page.locator('nav').locator('> div').first

    # check mobile menu has style fixed & visible
    expect(nav_menu).to_have_css('position', 'fixed')
    expect(nav_menu).to_be_visible()

    # validate login link & sign up is displayed
    expect(nav_menu).to_contain_text('Login')
    expect(nav_menu).to_contain_text('Sign up')

    # click on sign up link & validate user is redirected to register page
    page.get_by_role("link", name="Sign up").click()
    page.wait_for_load_state('domcontentloaded')
    expect(page).to_have_url(home_page + register_url)

    # fill in the form
    page.fill('input[name="username"]', user + 'mobile')
    page.fill('input[name="email"]', email)
    page.fill('input[name="password1"]', password)
    page.fill('input[name="password2"]', password)
    page.click('text="Sign up"')

    # check if the user is redirected to home page
    page.wait_for_load_state('domcontentloaded')
    expect(page).to_have_url(home_page)


def test_login_mobile_pass(page: Page):
    """
    Test login success with mobile device

    1. Go to home page
    2. Click on mobile menu button & validate mobile menu is displayed
    3. Click on Login link
    4. Check if the user is redirected to login page
    5. Fill in the form
    6. Click on login button
    7. Check if the user is redirected to home page
    8. Check if the user is logged in & navigate to profile page

    """
    # set device to mobile
    page.set_viewport_size({'width': 375, 'height': 812})
    # go to home page & click on mobile menu button
    page.goto(home_page)
    page.locator('button[id="nav-button"]').click()

    # click on login link & validate user is redirected to login page
    page.get_by_role("link", name="Login").click()
    page.wait_for_load_state('domcontentloaded')
    expect(page).to_have_url(home_page + login_url)

    # fill login form
    page.fill('input[name="username"]', user)
    page.fill('input[name="password"]', password)
    page.click('text="Sign in"')

    # check if the user is redirected to home page
    page.wait_for_load_state('domcontentloaded')
    expect(page).to_have_url(home_page)


def test_login_success(page: Page):
    """
    Test login success

    1. Go to home page
    2. Click on login link
    3. Check if the user is redirected to login page
    4. Fill in the form
    5. Click on login button
    6. Check if the user is redirected to home page
    7. Check if the user is logged in
    8. Check if username is displayed in the account menu

    """
    page.goto(home_page)
    page.get_by_role("link", name="Login").click()
    page.wait_for_load_state('domcontentloaded')
    expect(page).to_have_url(home_page + login_url)

    page.fill('input[name="username"]', user)
    page.fill('input[name="password"]', password)
    page.click('text="Sign in"')

    # check if the user is redirected to home page
    page.wait_for_load_state('domcontentloaded')
    expect(page).to_have_url(home_page)
    # validate login success alert message
    alert_message = page.locator('div[role="alert"] li')
    expect(alert_message).to_have_text(
        "You have successfully logged in"
    )
    account_menu = page.locator('#account-menu')
    expect(account_menu).to_contain_text(f"Hi {user}")


def test_login_fail(page: Page):
    """
    Test login fail invalid credentials

    1. Go to login page
    2. Fill in the form
    3. Click on login button
    4. Check if the user is redirected to login page
    5. Check if the error message is displayed
    """
    page.goto(home_page + login_url)
    page.fill('input[name="username"]', user)
    page.fill('input[name="password"]', password + '1')
    page.click('text="Sign in"')
    page.wait_for_load_state('domcontentloaded')

    expect(page).to_have_url(home_page + login_url)
    error_list = page.locator('ul[class="errorlist nonfield"] li')
    expect(error_list).to_contain_text(
        'Please enter a correct username and password.'
        ' Note that both fields may be case-sensitive.')


def test_logout_success(page: Page):
    """
    Test logout

    1. Go to home page
    2. Login
    3. Hover over account menu
    4. Click on sign out button & validate dialog is displayed
    5. Check if the user is redirected to home page & logged out
    6. Check if the user is logged out
    7. Check if login & register links are displayed in the navigation bar

    """
    # Initiate login test
    test_login_success(page)

    nav_element = page.locator('nav')
    account_menu = page.locator('#account-menu')

    account_menu.hover(force=True)

    account_submenu = page.locator('#account-submenu')
    expect(account_submenu).to_be_visible()

    page.get_by_role("button", name="Sign Out").click()

    dialog_logout = page.locator('dialog[id="logout"]')
    expect(dialog_logout).to_have_js_property('open', True)

    dialog_logout_link = dialog_logout.get_by_role("link", name="Logout")
    dialog_logout_button = dialog_logout.get_by_role("button", name="Cancel")

    dialog_logout_button.click()
    expect(dialog_logout).to_have_js_property('open', False)

    account_menu.hover(force=True)
    page.get_by_role("button", name="Sign Out").click()
    dialog_logout_link.click()
    # check if the user is redirected to home page
    page.wait_for_load_state('domcontentloaded')
    expect(page).to_have_url(home_page)
    # validate registration success alert message
    alert_message = page.locator('div[role="alert"] li')
    expect(alert_message).to_have_text(
        "You have successfully logged out"
    )
    # validate account menu is removed from the page
    expect(page.locator('#account-menu')).to_have_count(0)
    # validate navigation bar has login & register links
    expect(nav_element.get_by_role("link", name="Login")).to_be_visible()
    expect(nav_element.get_by_role("link", name="Sign up")).to_be_visible()
