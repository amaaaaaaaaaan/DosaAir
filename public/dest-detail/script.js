document.addEventListener("DOMContentLoaded", function () {
  var navbarHeight = document.querySelector(".head").offsetHeight;
  document.querySelector(".cont").style.marginTop = navbarHeight + "px";
});
let l;
document.addEventListener("DOMContentLoaded", function () {
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  l = { name: urlParams.get("dest"), air: urlParams.get("air") };
  document.querySelector(".dest-bg").src = `../dest-data/images/${l.name}.png`;
  document.querySelector(".dest-head").innerHTML = l.name;
  document.querySelector(".air").innerHTML = l.air;
  showflights(l.name);
});

async function showflights(qw) {
  const from = "Sharjah";
  const to = qw;
  const trip = "one";
  const today = new Date();
  const year = today.getFullYear();
  const month = String(today.getMonth() + 1).padStart(2, "0"); // Months are zero-based, so add 1
  const day = String(today.getDate()).padStart(2, "0");

  const l = `${year}-${month}-${day}`;
  const date = l;
  let flightdata;
  if (trip == "one") {
    flightdata = await eel.searchflight(from, to, date)();
  } else if (trip == "round") {
    const date2 = document.querySelector("#date2").value;
    flightdata = await eel.searchroundflight(from, to, date, date2)();
  }

  console.log(flightdata);
  if (flightdata.length == 0) {
    htm = ` <div  class="flight">
        <h1 class="waiting-ms waiting-smart">Sorry no flights matching</h1>
                  </div>
      </div>`;
    document.querySelectorAll(".flight").forEach((o, i) => {
      console.log(i);

      if (i == 0) {
        return;
      }
      console.log(-i);
      o.classList.add("hid");
    });
    document.querySelector("#startkaro").insertAdjacentHTML("beforebegin", htm);
  } else {
    flightdata.forEach((flight) => {
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
      document.querySelectorAll(".flight").forEach((o, i) => {
        console.log(i);

        if (i == 0) {
          return;
        }
        console.log(-i);
        o.classList.add("hid");
      });
      document
        .querySelector("#startkaro")
        .insertAdjacentHTML("beforebegin", htm);
    });
  }
}

function book(e) {
  const flightContainer = e.closest(".flight");

  const dateElement = flightContainer.querySelector(".flight-dt .flight-date");
  const timeElement = flightContainer.querySelector(".flight-dt .flight-time");
  const fnoelement = flightContainer.querySelector(".fno");

  if (dateElement && timeElement) {
    const date = dateElement.textContent;
    const time = timeElement.textContent;
    const fno = fnoelement.textContent;
    const flightDetails = {
      fno: fno,
      date: date,
      time: time,
      booking_id: flightContainer.querySelector(".booking_id").textContent,
    };

    eel.bookFlight(flightDetails)();
    window.location.href = "../bookings/index.html";
    // this object contains booking data 🐈
    return flightDetails;
  } else {
    console.error(
      "Date or time element not found within the flight container."
    );
  }
}

document.addEventListener("DOMContentLoaded", async function () {
  const desc = await eel.destDesc(l.name)();
  document.querySelector(".dest-desc").innerHTML = desc;
});

async function updateUserData() {
  userdata = await eel.userdata()();
  console.log();
  document.querySelector(".acc-name").innerText = userdata.name;
  document.querySelector("#ploc").innerText = userdata.ploc;
}

document.addEventListener("DOMContentLoaded", function () {
  updateUserData();
});
