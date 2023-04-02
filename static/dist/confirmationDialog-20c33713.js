const n=document.querySelector("form"),f=n.id,c=n.querySelector('input[type="submit"]'),l=(t,o)=>{const a=document.querySelector("#dialog-information"),e=document.createElement("div");e.innerHTML=`
        <span class='text-lg font-bold'>${t}</span>
        <span class='text-lg'>${o}</span>
      `,a.appendChild(e)};function g(){const t=new FormData(n),o=n.querySelectorAll("label");t.delete("csrfmiddlewaretoken"),Array.from(t.entries()).forEach((e,i)=>{if(n.id==="booking-form")if(e[0]==="booking_date"){const r=new Date(e[1]).toLocaleDateString("en-GB",{year:"numeric",month:"long",day:"numeric"});l(o[i].innerText,r)}else if(e[0]==="booking_time"){const r=e[1].split(":"),s=r[0],d=r[1],m=Number(s)>=12?"pm":"am",u=`${s}:${d} ${m}`;l(o[i].innerText,u)}else l(o[i].innerText,e[1]);else l(o[i].innerText,e[1])})}function b(){let t=document.querySelector("#dialog");t==null&&(t=document.createElement("dialog"),t.id="dialog");const a={"booking-form":"Booking Details","customer-form":"Profile Details"}[f]??"Confirm Details";t.innerHTML=`
        <h2 class='text-2xl font-bold'>${a}</h2>
        <p class='text-lg'>Please confirm details are correct</p>
        <div id='dialog-information' class='mt-8 space-y-2 grid text-left justify-center '></div>
        <div class='grid grid-cols-2 gap-x-2 mt-8'>
          <button class='btn bg-red-500 !text-[#05113f] rounded-md' type='button'>Cancel</button>
          <button class='btn rounded-md' type='submit'>Confirm</button>
        </div>
    `,t&&document.body.appendChild(t),t.showModal(),g();const e=t.querySelector('button[type="button"]'),i=t.querySelector('button[type="submit"]');e.addEventListener("click",()=>{t.close(),c.disabled=!1}),i.addEventListener("click",()=>n.submit())}n.addEventListener("submit",t=>{t.preventDefault(),c.disabled=!0,b()});
