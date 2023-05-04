from playwright.sync_api import Page, expect

# URLs
contact_url = 'contact/'
contact_success_url = 'contact/success/'
home_page = 'http://127.0.0.1:8000/'

# User credentials
name = 'testuser'
email = 'test@gmail.com'
phone_number = '123456789'
message = 'test message long enough'


def test_contact_form_success(page: Page):
    """
    Test contact form success

    1. Go to home page
    2. Click on contact link
    3. Check if the user is redirected to contact page
    4. Fill in the form
    5. Click on submit button
    6. Check if the user is redirected to contact success page
    7. Validate heading text h1/h2
    8. Validate contact details

    """
    page.goto(home_page)
    page.get_by_role("link", name="Contact").click()
    page.wait_for_load_state('domcontentloaded')
    expect(page).to_have_url(home_page + contact_url)

    page.fill('input[name="full_name"]', name)
    page.fill('input[name="email"]', email)
    page.fill('input[name="phone_number"]', phone_number)
    page.fill('textarea[name="message"]', message)
    page.locator('input[type="submit"]').click()

    page.wait_for_load_state('domcontentloaded')
    expect(page).to_have_url(home_page + contact_success_url)

    # validate alert message text
    alert_message = page.locator('div[role="alert"] li')
    expect(alert_message).to_have_text(
        "Success! Your message has been sent."
    )

    # validate heading text h1/h2
    h1 = page.locator('h1')
    expect(h1).to_have_text('Thank you for getting in touch,')

    # validate h2 text
    h2 = page.locator('h2').first
    expect(h2).to_have_text('We will get back to you as soon as possible')

    # get div by attribute data-contact-details
    contact_details = page.locator('div[data-contact-details]')
    # validate contact details first dl element
    description_list_one = contact_details.locator('dl').first
    expect(description_list_one).to_have_text(f"Name:{name}")
    # validate contact details second dl element
    description_list_two = contact_details.locator('dl').nth(1)
    expect(description_list_two).to_have_text(f"Email:{email}")
    # validate contact details third dl element
    description_list_three = contact_details.locator('dl').nth(2)
    expect(description_list_three).to_have_text(f"Phone number:{phone_number}")
    # validate contact details fourth dl element
    description_list_four = contact_details.locator('dl').nth(3)
    expect(description_list_four).to_have_text(f"Message:{message}")

