async function ticketLoad() {
  userdata = await eel.userdata()();
  console.log();
  document.querySelector(".acc-name").innerText = userdata.name;
  document.querySelector("#ploc").innerText = userdata.ploc;
  const ticketsdata = await eel.pullTickets()();
  console.log(ticketsdata);
  ticketsdata.forEach((ticket) => {
    pash = "";
    ticket.passengerdetails.forEach((passenger) => {
      pshtml = ` <div class="passenger">
      <h1 class="passenger-head">Passport details</h1>
      <div class="passenger-cont">
        <div class="login-inf">
          <span>Title</span>
          <span class="login-text" >
          ${passenger.title}
          </span>
        </div>
        <div class="login-inf">
          <span>Name</span>
          <span class="login-text" id="username" type="text" name="" id="" >
          ${passenger.firstName}</span>
        </div>
       
      </div>
      <div class="passenger-cont">
        <div class="login-inf">
<span>Age group</span>
<span class="login-text"> ${passenger.ageGroup} </span>
</div>
</div>
        <div class="login-inf">
          <span>Nationality</span>
          <span class="login-text" >
            ${passenger.national}
          </span>
        </div>
      </div>
<div class="passenger-cont">
<div class="login-inf">
<span>Food Choice</span>
<span class="login-text btn" >${passenger.food[0]}</span>
</div>
<div class="login-inf">
<span>Seat</span>
<span class="login-text ste" >${passenger.seat}</span>
</div>
<div class="login-inf">
<span>Baggage</span>
<span class="login-text" >
${passenger.bgg}
</span>
</div>
</div>
         
    </div>`;
      pash += pshtml;
    });
    htm = `<div class="ticket-passenger flight">
          <div class="flight tto">
            <div class="flight-dest-cont">
              <span class="flight-dest">${ticket.from}</span>
            </div>
            <div class="flight-take-off-icon"></div>
            <hr class="custom-hr" />
            <div class="flight-bk">
              <div class="flight-inf">
                <div class="flight-dt">
                  <span class="flight-date">${ticket.date}</span>
                  <span class="flight-date flight-time">${ticket.time}</span>

                  <span class="flight-time">$${ticket.price}</span>
                  <span class="flight-date flight-time">${ticket.duration}</span>
                </div>
              </div>
            </div>

            <hr class="custom-hr" />
            <div class="flight-take-in-icon"></div>
            <div class="flight-dest-cont">

              <span class="flight-dest">${ticket.to}</span>
            </div>
          </div>
          ${pash}
        
            <h2 style="text-align: right; width: 100%">Total Price : $<span id="totprice">${ticket.totalprice}</span></h2>
            <div id="passengers"></div>
          </div>`;

    document.querySelector("#startkaro").insertAdjacentHTML("afterend", htm);
  });
}

document.addEventListener("DOMContentLoaded", ticketLoad());
