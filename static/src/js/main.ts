const navButton = document.querySelector('#nav-button') as HTMLButtonElement
const navMenu = document.querySelector('nav')?.firstElementChild as HTMLElement
const body = document.querySelector('body') as HTMLElement
const accountMenu = document.querySelector('#account-menu') as HTMLElement
const accountSubmenu = document.querySelector('#account-submenu') as HTMLElement
const logoutButtons = document.querySelectorAll(
  '.button-logout'
) as NodeListOf<HTMLButtonElement>
const dialogLogout = document.querySelector(
  'dialog#logout'
) as HTMLDialogElement
const dialogCancelBtn = dialogLogout.querySelector(
  'button'
) as HTMLButtonElement
const djangoFlashmessage = document.querySelector('[role="alert"]') as HTMLDivElement;
const accountAria = accountMenu.getAttribute('aria-expanded')


navButton.addEventListener('click', showMobileMenu)

// reset the mobile menu to its original state
function resetNavMenuState() {
  navButton.setAttribute('aria-expanded', 'false')
  navMenu.classList.remove('fixed')
  navMenu.classList.add('hidden')
  navMenu.style.width = '0'
  body.classList.remove('overflow-y-hidden')
}

// Display the mobile menu and change the aria attributes
async function showMobileMenu() {
  const navAria = navButton.getAttribute('aria-expanded')

  if (navAria === 'false') {
    navButton.setAttribute('aria-expanded', 'true')
    navMenu.classList.remove('hidden')
    navMenu.classList.add('fixed')

    await new Promise((resolve) => setTimeout(resolve, 200))
    navMenu.style.width = '80%'
    body.classList.add('overflow-y-hidden')
  } else {
    resetNavMenuState()
  }
  closeMenuOnLargeScreen()
}

// close the mobile menu when the window is resized to over 640px
function closeMenuOnLargeScreen() {
  window.addEventListener('resize', () => {
    if (
      window.innerWidth > 640 &&
      navButton.getAttribute('aria-expanded') === 'true'
    ) {
      resetNavMenuState()
    }
  })
}

// Display the account submenu and change the aria attributes
if (window.innerWidth > 768 && accountMenu) {
  accountMenu.addEventListener('mouseenter', showAccountSubMenu)
  // Hide the account submenu after 350ms
  accountSubmenu.addEventListener('mouseleave', () => {
    setTimeout(() => {
      accountSubmenu.classList.add('hidden')
      accountMenu.setAttribute('aria-expanded', 'false')
    }, 350)
  })
}

// Display the account submenu and assign aria attributes on large screens
function showAccountSubMenu() {
  if (!!accountAria) {
    accountMenu.setAttribute('aria-expanded', 'true')
    accountSubmenu.classList.remove('hidden')
  }
}

// Hide django flash django flash messages after 5 seconds
if (djangoFlashmessage) {
  setTimeout(() => {
    djangoFlashmessage.classList.add('hidden')
  }, 3500)
}

// show the dialog box when the logout button is clicked
logoutButtons.forEach((button) => {
  button.addEventListener('click', () => dialogLogout.showModal())
})

// close the dialog box when the cancel button is clicked
dialogCancelBtn.addEventListener('click', () => dialogLogout.close())


export {}
