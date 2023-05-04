from datetime import date, timedelta
from playwright.sync_api import Page, expect

# URLs
booking_url = 'booking/create/'
profile_bookings = 'profile/dashboard/my-bookings/'
login_url = 'login/'
home_page = 'http://127.0.0.1:8000/'

# User credentials
name = 'testuser'
email = 'text@gmail.com'
password = 'testpassword@@'

# Booking details

# today's date plus 1 day in python
tomorrows_date = date.today() + timedelta(days=1)
# booking time
initial_booking_time = '14:00'
# booking placements
initial_booking_placements = '2'
# booking message
initial_booking_message = 'I would like to book a table for 2 people'
# convert date to format for form input
initial_booking_date_form_input = tomorrows_date.strftime("%Y-%m-%d")
# convert date to format for dialog
initial_booking_date_dialog = tomorrows_date.strftime("%d %B %Y")
# convert date to format for profile page
initial_booking_date_profile = tomorrows_date.strftime("%d/%m/%Y")

# booking alert message success
booking_success_message = \
    f"Thank you for booking with us, {name}! " \
    f" We will be in touch shortly to confirm your booking."

# booking alert message edit success
booking_edit_success_message = \
    f"Your booking has been successfully updated"

# booking alert message delete success
booking_delete_success_message = \
    f"Your booking has been successfully deleted"

# booking already exists message
booking_exists_message = \
    "You have already booked for this date, please choose another date."

new_booking_date = date.today() + timedelta(days=2)
new_booking_time = '15:00'
new_booking_placements = '4'
new_booking_message = 'I would like to book a table for 4 people'
new_booking_date_form_input = new_booking_date.strftime("%Y-%m-%d")
new_booking_date_dialog = new_booking_date.strftime("%d %B %Y")
new_booking_date_profile = new_booking_date.strftime("%d/%m/%Y")


def signin_user(page):
    """
    Sign in user
    """

    page.goto(home_page + login_url)
    page.fill('input[name="username"]', name)
    page.fill('input[name="password"]', password)
    page.click('text="Sign in"')
    page.wait_for_load_state('domcontentloaded')


def create_booking(page):
    """
    Make a booking

    1. Login user
    2. Go to booking page
    3. Submit booking form
    """
    # go to booking page & fill in the booking form & submit
    signin_user(page)
    page.goto(home_page + booking_url)
    page.wait_for_load_state('domcontentloaded')
    page.fill('input[name="booking_date"]', initial_booking_date_form_input)
    page.fill('input[name="booking_time"]', initial_booking_time)
    page.fill('input[name="placements"]', initial_booking_placements)
    page.fill('textarea[name="message"]', initial_booking_message)
    page.locator('input[type="submit"]').click()


def validate_booking_dialog(page, booking_date, booking_time,
                            booking_placements, booking_message):
    """
    Validate booking details
    """

    # locate dialog information div
    dialog_information = page.locator('div[id="dialog-information"]')

    # validate dialog booking date dialog text
    booking_date_dialog_date = \
        dialog_information.locator('div').first.locator('span').first
    expect(booking_date_dialog_date).to_have_text("Booking Date:")

    # validate dialog booking date
    booking_date_dialog_date = \
        dialog_information.locator('div').first.locator('span').last
    expect(booking_date_dialog_date).to_have_text(booking_date)

    # validate booking time dialog text
    booking_time_dialog_time = \
        dialog_information.locator('div').nth(1).locator('span').first
    expect(booking_time_dialog_time).to_have_text("Booking Time:")

    # validate booking time
    booking_time_dialog_time = \
        dialog_information.locator('div').nth(1).locator('span')
    expect(booking_time_dialog_time.last).to_have_text(booking_time + " pm")

    # validate dialog placements dialog text
    booking_placements_dialog_placements = \
        dialog_information.locator('div').nth(2).locator('span').first
    expect(booking_placements_dialog_placements) \
        .to_have_text("Number of Placements:")

    # validate dialog placements
    booking_placements_dialog_placements = \
        dialog_information.locator('div').nth(2).locator('span').last
    expect(
        booking_placements_dialog_placements).to_have_text(booking_placements)

    # validate dialog message dialog text
    booking_message_dialog_message = \
        dialog_information.locator('div').nth(3).locator('span').first
    expect(booking_message_dialog_message).to_have_text("Message:")

    # validate dialog message
    booking_message_dialog_message = \
        dialog_information.locator('div').nth(3).locator('span').last
    expect(booking_message_dialog_message).to_have_text(booking_message)


def validate_booking_confirmation_details(page, booking_date, booking_time,
                                          booking_placements, booking_message):
    """
    Validate booking details
    """
    # locate dialog datalist element
    description_list = page.locator('dl').first

    # check if booking confirmed is no
    customer_booking_status = description_list.locator('dd').first
    expect(customer_booking_status).to_have_text("No")

    # check if booking date is correct
    customer_booking_date = description_list.locator('dd').nth(1)
    expect(customer_booking_date).to_have_text(booking_date)

    # check if booking time is correct
    customer_booking_time = description_list.locator('dd').nth(2)
    expect(customer_booking_time).to_have_text(booking_time)

    # check if booking placements is correct
    customer_booking_placements = description_list.locator('dd').nth(3)
    expect(customer_booking_placements).to_have_text(booking_placements)
    # check if booking message is correct
    customer_booking_message = description_list.locator('dd').nth(4)
    expect(customer_booking_message).to_have_text(booking_message or "None")


def validate_booking_success_message(page, message):
    alert_message = page.locator('div[role="alert"] li')
    expect(alert_message).to_have_text(message)


def test_booking_success(page: Page):
    """
    Test booking form success

    1. Go to login page
    2. Fill in the login form
    3. Click on login button wait for page to load & go to booking page
    4. Fill in the booking form
    5. Click on book button
    6. check dialog opens and details are correct
    7. click on cancel button & verify dialog closes
    8. click on book button
    9. click on confirm button & check if the user is redirected to booking
    success page
    10. check if booking success alert message is displayed
    11. check if booking details are displayed

    """
    page.set_viewport_size({"width": 1200, "height": 1080})
    create_booking(page)
    # check dialog opens and details are correct
    dialog = page.locator('dialog[id="dialog"]')
    expect(dialog).to_be_visible()
    # validate booking details
    validate_booking_dialog(page, initial_booking_date_dialog,
                            initial_booking_time,
                            initial_booking_placements,
                            initial_booking_message)
    # click on cancel button & verify dialog closes
    dialog.locator('button[type="button"]').click()
    expect(dialog).not_to_be_visible()
    # click on book button
    page.locator('input[type="submit"]').click()
    # click on confirm button & check
    # if the user is redirected to profile bookings

    dialog.locator('button[type="submit"]').click()
    # change booking date by one day if booking date already exists
    page.wait_for_load_state('domcontentloaded')
    if not page.url == home_page + profile_bookings:
        new_book_date = new_booking_date + timedelta(days=1)
        new_book_date_profile = new_book_date.strftime("%Y-%m-%d")
        page.locator('input[name="booking_date"]').fill(
            new_book_date_profile)
        page.locator('input[type="submit"]').click()
        dialog.get_by_role('button', name='Confirm').click()
        page.wait_for_load_state('domcontentloaded')

    # expect(page).to_have_url(home_page + profile_bookings)
    # check if booking details are displayed correctly on profile bookings
    validate_booking_confirmation_details(page, initial_booking_date_profile,
                                          initial_booking_time,
                                          initial_booking_placements,
                                          initial_booking_message)
    # check if booking success alert message is displayed
    validate_booking_success_message(page, booking_success_message)


def test_booking_edit(page: Page):
    """
    Test booking form edit

    1. Go to login page
    2. Fill in the login form
    3. Click on login button wait for page to load
        go to profile bookings page.
    4. Click on edit button
    5. Fill in the booking form with new details
    6. Click on book button
    7. check dialog opens and details are correct & click on confirm button
    8. check details are updated

    """
    page.set_viewport_size({"width": 1200, "height": 1080})
    signin_user(page)
    # go to profile bookings page.
    page.goto(home_page + profile_bookings)
    page.wait_for_load_state('domcontentloaded')

    if page.locator('a').page.get_by_text("Edit booking").count():
        # Click on edit button
        page.locator('a').page.get_by_text("Edit booking").first.click()
        # wait for page to load
        page.wait_for_load_state('domcontentloaded')
        page.locator('input[type="submit"]').click()
    else:
        # Make new booking
        create_booking(page)

    dialog = page.locator('dialog[id="dialog"]')
    dialog.locator('button[type="submit"]').click()
    # Click on edit a tage with Edit booking text
    page.wait_for_load_state('domcontentloaded')
    # Fill in the booking form with new details
    page.locator('input[name="booking_date"]').fill(
        new_booking_date_form_input)
    page.locator('input[name="booking_time"]').fill(new_booking_time)
    page.locator('input[name="placements"]').fill(new_booking_placements)
    page.locator('textarea[name="message"]').fill(new_booking_message)

    # Click on book button
    page.locator('input[type="submit"]').click()
    # check dialog opens and details are correct & click on confirm button
    dialog = page.locator('dialog[id="dialog"]')
    validate_booking_dialog(page, new_booking_date_dialog,
                            new_booking_time,
                            new_booking_placements,
                            new_booking_message
                            )
    dialog.locator('button[type="submit"]').click()
    page.wait_for_load_state('domcontentloaded')
    # check details are updated
    validate_booking_confirmation_details(page, new_booking_date_profile,
                                          new_booking_time,
                                          new_booking_placements,
                                          new_booking_message
                                          )
    # check if booking success alert message is displayed
    validate_booking_success_message(page, booking_edit_success_message)


def test_booking_delete(page: Page):
    """
    Test booking form delete

    1. Go to login page
    2. Fill in the login form
    3. Click on login button wait for page to load
        go to profile bookings page.
    4. Click on delete button
    5. Click on confirm button
    6. check if booking is deleted

    """
    page.set_viewport_size({"width": 1200, "height": 1080})
    signin_user(page)
    # go to profile bookings page.
    page.goto(home_page + profile_bookings)
    page.wait_for_load_state('domcontentloaded')

    if page.locator('a').page.get_by_text("Edit booking").count():
        pass
    else:
        # Make new booking
        create_booking(page)
        dialog = page.locator('dialog[id="dialog"]')
        dialog.locator('button[type="submit"]').click()
        page.wait_for_load_state('domcontentloaded')

    booking_ref_number = \
        page.get_by_text("Booking reference").first.all_inner_texts()[0]
    # Click on cancel button for the booking
    cancel_booking_button = \
        page.get_by_role('button', name='Cancel booking').first
    cancel_booking_button.click()

    dialog = page.locator('dialog[class="edit-booking-dialog"]')
    # validate dialog opens
    expect(dialog).to_be_visible()
    # Click on confirm button
    dialog.get_by_role('button', name='Cancel').click()
    # validate booking dialog is closed
    expect(dialog).not_to_be_visible()

    cancel_booking_button.click()
    dialog.locator('a').get_by_text("Confirm").click()

    # check if booking reference is not removed
    expect(page.get_by_text(booking_ref_number)).not_to_be_visible()
