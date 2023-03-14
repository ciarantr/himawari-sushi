// cancel booking buttons
const cancelBookingBtns = document.querySelectorAll(
  '.booking-cancel'
) as NodeListOf<HTMLButtonElement>

// add event listener to the cancel booking buttons
cancelBookingBtns.forEach((button) => {
  button.addEventListener('click', () =>
    bookingConfirmModal(button as HTMLButtonElement)
  )
})

function bookingConfirmModal(button: HTMLButtonElement) {
  // create a dialog DOM element if it doesn't exist
  let dialogCancelBooking = document.querySelector(
    'dialog.edit-booking-dialog'
  ) as HTMLDialogElement

  if (dialogCancelBooking == null) {
    dialogCancelBooking = document.createElement('dialog')
    dialogCancelBooking.classList.add('edit-booking-dialog')
  }

  // get the booking id from the button used to identify the booking to be cancelled
  const bookingId = button.getAttribute('data-booking-id')

  // add content to the dialog box
  dialogCancelBooking.innerHTML = `
      <h2 class='text-2xl font-bold'>Cancel Booking</h2>
      <p class='text-gray-500'>Are you sure you want to cancel this booking?</p>
      <div class='flex justify-between items-center w-full mt-4'>
        <button class='hover:underline'>Cancel</button>
        <a  href='/booking/delete/${bookingId}/' class='block hover:underline hover:text-red-500'>Confirm</a>
      </div>
    `

  document.body.appendChild(dialogCancelBooking)

  const cancelBtn = dialogCancelBooking.querySelector(
    'button'
  ) as HTMLButtonElement

  cancelBtn.addEventListener('click', () => dialogCancelBooking.close())

  // show the dialog modal
  dialogCancelBooking.showModal()

}

export {}
