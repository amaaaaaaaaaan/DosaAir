const today = new Date().toISOString().split("T")[0];

// Set the min attribute of the date input to today's date
document.getElementById("date").setAttribute("min", today);
async function showflights() {
  const from = document.querySelector("#from").value;
  const to = document.querySelector("#to").value;
  const trip = document.querySelector("#trip").value;
  const date = document.querySelector("#date").value;
  let flightdata;
  if (trip == "one") {
    flightdata = await eel.searchflight(from, to, date)();
  } else if (trip == "round") {
    const date2 = document.querySelector("#date2").value;
    flightdata = await eel.searchroundflight(from, to, date, date2)();
  }
  document.getElementById("startkaro").innerHTML = "";

  console.log(flightdata);

  if (flightdata.length == 0) {
    htm = ` <div  class="flight">
        <h1 class="waiting-ms waiting-smart">Sorry no flights matching</h1>
                  </div>
      </div>`;
    document.querySelectorAll(".flight").forEach((o, i) => {
      if (i == 0) {
        return;
      }
    });
    document.querySelector("#startkaro").insertAdjacentHTML("afterbegin", htm);
  } else {
    flightdata.forEach((flight) => {
      const htm = `<div class="flight l" >
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
      });
      document
        .querySelector("#startkaro")
        .insertAdjacentHTML("afterbegin", htm);
    });
  }
}

document.getElementById("date").addEventListener("change", function () {
  const inputDate = new Date(this.value);
  if (!isNaN(inputDate)) {
    const options = { weekday: "long", day: "2-digit", month: "long" };
    const formattedDate = inputDate.toLocaleDateString("en-GB", options);
  }
});

document.querySelector("#trip").addEventListener("change", function () {
  if (document.querySelector("#trip").value == "round") {
    document.querySelector("#date2cont").classList.remove("hid");
  } else {
    document.querySelector("#date2cont").classList.add("hid");
  }
});

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

async function updateUserData() {
  userdata = await eel.userdata()();
  console.log();
  document.querySelector(".acc-name").innerText = userdata.name;
  document.querySelector("#ploc").innerText = userdata.ploc;
}

document.addEventListener("DOMContentLoaded", function () {
  updateUserData();
});
