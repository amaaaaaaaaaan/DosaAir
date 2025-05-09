async function updateUserData() {
  userdata = await eel.userdata()();
  console.log();
  document.querySelector(".acc-name").innerText = userdata.name;
  document.querySelector("#ploc").innerText = userdata.ploc;
  const smartRoutes = await eel.smartRoutes()();
  if (smartRoutes) {
    document.querySelector(".waiting").classList.add("hid");
  }
  console.log(smartRoutes);
  if (smartRoutes.length == 0) {
    htm = ` <div  class="flight">
        <h1 class="waiting-ms waiting-smart">Sorry SmartRoutes couldn't be initiated</h1>
                  </div>
      </div>`;
    document.querySelector("#startkaro").insertAdjacentHTML("beforebegin", htm);
  }
  smartRoutes.forEach((flight) => {
    const htm = `<div class="flight" >
    <span class='fno' style='display:none'>${flight.Fno}</span>
<div class="flight-dest-cont">
            <span class="flight-date flight-time" style='text-align:left'>${flight.from}</span>
            <span class="flight-dest">${flight.FromDest}</span>

          </div>          <div class="flight-take-off-icon"></div>
          <hr class="custom-hr">
          <div class="flight-bk">
            <div class="flight-inf dw">
            
            
              <div class="flight-dt">
                <span class="flight-date">${flight.date}</span>
                           <span class="flight-date flight-time">${flight.time}</span>      
  <span class="flight-time">$${flight.Price}</span>
  <span class="flight-date flight-time">${flight.duration}</span>
    <span class="booking_id" style="display:none">${flight.booking_id}</span>

            </div>
            
            
          </div>
          <button class="flight-booking" onclick="book(this)">BOOK</button>
          </div>
          
          <hr class="custom-hr">
          <div class="flight-take-in-icon"></div>
<div class="flight-dest-cont">
            <span class="flight-date flight-time">${flight.to}</span>
            <span class="flight-dest">${flight.ToDest}</span>

          </div>           </div>`;
    document.querySelector("#startkaro").insertAdjacentHTML("beforebegin", htm);
  });
}

document.addEventListener("DOMContentLoaded", function () {
  updateUserData();
});

function book(e) {
  const flightContainer = e.closest(".flight");

  const dateElement = flightContainer.querySelector(".flight-dt .flight-date");
  const timeElement = flightContainer.querySelector(".flight-dt .flight-time");
  const fnoelement = flightContainer.querySelector(".fno");
  const booking_id = flightContainer.querySelector(".booking_id").textContent;
  if (dateElement && timeElement) {
    const date = dateElement.textContent;
    const time = timeElement.textContent;
    const fno = fnoelement.textContent;
    const flightDetails = {
      fno: fno,
      date: date,
      time: time,
      booking_id: booking_id,
    };

    eel.bookFlight(flightDetails)();
    window.location.href = "bookings/index.html";
    // this object contains booking data 🐈
    return flightDetails;
  } else {
    console.error(
      "Date or time element not found within the flight container."
    );
  }
}

document.querySelector(".acc-log-btn").addEventListener("click", function () {
  window.location.href = "login.html";
});

document.querySelector(".acc-log").addEventListener("mouseover", function () {
  document.querySelector(".acc-log-btn").style.opacity = 100;
  document.querySelector(".acc-log-btn").style.opacity = "25px";
  document.querySelector(".acc-log-btn").style.display = "inherit";
});

document.querySelector(".acc-log").addEventListener("mouseout", function () {
  document.querySelector(".acc-log-btn").style.opacity = 0;
  // document.querySelector(".acc-log-btn").style.height = "0px";
  document.querySelector(".acc-log-btn").style.display = "none";
});
