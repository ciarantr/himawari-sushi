// FIXME: formDataArray should replace only text content of dialog box if dom element already exists

const form = document.querySelector('form') as HTMLFormElement
const formId: string = form.id
const submitBtn = form.querySelector('input[type="submit"]') as HTMLInputElement

const createDialogText = (key: string, value: string) => {
  const dialog = document.querySelector(
    '#dialog-information'
  ) as HTMLDialogElement

  const divEl = document.createElement('div')
  divEl.innerHTML = `
        <span class='text-lg font-bold'>${key}</span>
        <span class='text-lg'>${value}</span>
      `
  // Append divEl to dialog box
  dialog.appendChild(divEl)
}

function CreateDialogFormData() {
  // get form data
  const formData = new FormData(form)
  const formLabels = form.querySelectorAll('label')

  // remove csrf token from formData
  formData.delete('csrfmiddlewaretoken')

  // convert FormData to array
  const formDataArray = Array.from(formData.entries()) as [string, string][]

  // add form data to dialog box
  formDataArray.forEach((element, index) => {
    if (form.id === 'booking-form') {
      // Format date and time for booking form
      if (element[0] === 'booking_date') {
        // Format date
        const formattedDate = new Date(element[1]).toLocaleDateString('en-GB', {
          year: 'numeric',
          month: 'long',
          day: 'numeric',
        })

        createDialogText(formLabels[index].innerText, formattedDate)
      } else if (element[0] === 'booking_time') {
        // Format time
        const time = element[1].split(':')
        const hour = time[0]
        const minute = time[1]
        const ampm = Number(hour) >= 12 ? 'pm' : 'am'
        const newTime = `${hour}:${minute} ${ampm}`
        createDialogText(formLabels[index].innerText, newTime)
      } else {
        createDialogText(formLabels[index].innerText, element[1])
      }
    } else {
      createDialogText(formLabels[index].innerText, element[1])
    }
  })
}

function CreateDialogBox() {
  let dialog = document.querySelector('#dialog') as HTMLDialogElement
  if (dialog == null) {
    dialog = document.createElement('dialog')
    dialog.id = 'dialog'
  }

  const dialogHeadings: { [key: string]: string } = {
    'booking-form': 'Booking Details',
    'customer-form': 'Profile Details',
  }

  // Get dialog heading from dialogHeadings object in typescript
  const dialogHeading = dialogHeadings[formId] ?? 'Confirm Details'

  dialog.innerHTML = `
        <h2 class='text-2xl font-bold'>${dialogHeading}</h2>
        <p class='text-lg'>Please confirm details are correct</p>
        <div id='dialog-information' class='mt-8 space-y-2 grid text-left justify-center '></div>
        <div class='grid grid-cols-2 gap-x-2 mt-8'>
          <button class='btn bg-red-500 rounded-md' type='button'>Cancel</button>
          <button class='btn rounded-md' type='submit'>Confirm</button>
        </div>
    `

  dialog ? document.body.appendChild(dialog) : null

  dialog.showModal()
  // Add form data to dialog box
  CreateDialogFormData()

  const dialogCancelBtn = dialog.querySelector(
    'button[type="button"]'
  ) as HTMLButtonElement

  const dialogConfirmBtn = dialog.querySelector(
    'button[type="submit"]'
  ) as HTMLButtonElement

  // Close dialog box
  dialogCancelBtn.addEventListener('click', () => {
    dialog.close()
    submitBtn.disabled = false
  })

  // Submit form
  dialogConfirmBtn.addEventListener('click', () => form.submit())
}

// Add dialog box to DOM on form submit
form.addEventListener('submit', (e) => {
  e.preventDefault()
  submitBtn.disabled = true
  // Create dialog box
  CreateDialogBox()
})

export {}
