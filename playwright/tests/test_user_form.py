from playwright.sync_api import Page, expect

# URLs
user_details_url = 'profile/dashboard/my-details/'
login_url = 'login/'
home_page = 'http://127.0.0.1:8000/'

# User credentials
username = 'testuser'
first_name = 'fname'
last_name = 'lname'
email = 'user@gmail.com'
phone_number = '123456789'
password = 'testpassword@@'

message_success = 'Your details have been updated.'
message_no_changes = 'No changes were made.'


def login(page):
    """
    Login to user account
    """
    page.goto(home_page + login_url)
    page.wait_for_load_state('domcontentloaded')
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    page.locator('input[type="submit"]').click()
    page.wait_for_load_state('domcontentloaded')


def input_new_details(page):
    """
    Input new details into user details form
    """
    page.fill('input[name="username"]', username + '1')
    page.fill('input[name="first_name"]', first_name)
    page.fill('input[name="last_name"]', last_name)
    page.fill('input[name="email"]', email)
    page.fill('input[name="phone_number"]', phone_number)


def validate_dialog_details(page):
    """
    Validate dialog box details
    """
    #
    dialog_information = page.locator('dialog[id="dialog"]')
    # username_text = dialog_information.locator('div').nth(0)
    # expect(username_text).to_have_text('Username:' + "\n" + username + '1')

    username_text = dialog_information.locator('div').nth(1)
    expect(username_text).to_have_text('Username:' + "\n" + username + '1')

    first_name_text = dialog_information.locator('div').nth(2)
    expect(first_name_text).to_have_text('First name:' + "\n" + first_name)

    last_name_text = dialog_information.locator('div').nth(3)
    expect(last_name_text).to_have_text('Last name:' + "\n" + last_name)

    email_text = dialog_information.locator('div').nth(4)
    expect(email_text).to_have_text('Email address:' + "\n" + email)

    phone_number_text = dialog_information.locator('div').nth(5)
    expect(phone_number_text).to_have_text(
        'Phone number:' + "\n" + phone_number)


def validate_details_updated(page: Page):
    """
    Check user details have been updated
    """

    # validate user details are updated
    form = page.locator('form[id="customer-form"]')
    # validate username
    username_input = form.locator('input[name="username"]')
    expect(username_input).to_have_value(username + '1')

    # validate first name
    first_name_input = form.locator('input[name="first_name"]')
    expect(first_name_input).to_have_value(first_name)

    # validate last name
    last_name_input = form.locator('input[name="last_name"]')
    expect(last_name_input).to_have_value(last_name)

    # validate email
    email_input = form.locator('input[name="email"]')
    expect(email_input).to_have_value(email)

    # validate phone number
    phone_number_input = form.locator('input[name="phone_number"]')
    expect(phone_number_input).to_have_value(phone_number)


def test_user_details_form_update_success(page: Page):
    """
    Test user details form success

    1. Go to login page & login
    2. Go to user details page
    3. Input user details & check dialog box details are correct
    4. Check cancel button closes dialog box
    5. Check update button updates user details

    """
    # login
    login(page)
    # go to user details page
    page.goto(home_page + user_details_url)
    page.wait_for_load_state('domcontentloaded')

    # input new details & click update button
    input_new_details(page)
    page.locator('input[type="submit"]').click()

    # validate dialog box is visible
    dialog = page.locator('dialog[id="dialog"]')
    expect(dialog).to_be_visible()

    # validate dialog box details with new details
    validate_dialog_details(page)

    # confirm new details
    dialog.get_by_role("button", name="Confirm").click()
    expect(dialog).not_to_be_visible()

    # validate alert message text
    alert_message = page.locator('div[role="alert"] li')
    expect(alert_message).to_have_text(message_success)

    # validate user details are updated
    validate_details_updated(page)

    # validate cancel button closes dialog box
    page.get_by_role("button", name="Update").click()
    dialog.get_by_role("button", name="Cancel").click()
    expect(dialog).not_to_be_visible()

    # validate no changes message
    page.get_by_role("button", name="Update").click()
    dialog.get_by_role("button", name="Confirm").click()
    expect(dialog).not_to_be_visible()
    # validate alert message text
    alert_message = page.locator('div[role="alert"] li')
    expect(alert_message).to_have_text(message_no_changes)
