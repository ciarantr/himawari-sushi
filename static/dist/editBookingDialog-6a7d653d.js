const t=document.querySelectorAll(".booking-cancel");t.forEach(o=>{o.addEventListener("click",()=>l(o))});function l(o){let e=document.querySelector("dialog.edit-booking-dialog");e==null&&(e=document.createElement("dialog"),e.classList.add("edit-booking-dialog"));const n=o.getAttribute("data-booking-id");e.innerHTML=`
      <h2 class='text-2xl font-bold'>Cancel Booking</h2>
      <p class='text-gray-500'>Are you sure you want to cancel this booking?</p>
      <div class='flex justify-between items-center w-full mt-4'>
        <button class='hover:underline'>Cancel</button>
        <a  href='/booking/delete/${n}/' class='block hover:underline hover:text-red-500'>Confirm</a>
      </div>
    `,document.body.appendChild(e),e.querySelector("button").addEventListener("click",()=>e.close()),e.showModal()}
