const today = new Date().toISOString().split("T")[0];

// Set the min attribute of the date input to today's date
document.getElementById("date").setAttribute("min", today);
async function showflights() {
  const from = document.querySelector("#from").value;
  const to = document.querySelector("#to").value;
  const trip = document.querySelector("#trip").value;
  const date = document.querySelector("#date").value;

  const flightdata = await eel.searchflight(from, to, date)();
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

document.getElementById("date").addEventListener("change", function () {
  const inputDate = new Date(this.value);
  if (!isNaN(inputDate)) {
    const options = { weekday: "long", day: "2-digit", month: "long" };
    const formattedDate = inputDate.toLocaleDateString("en-GB", options);
  }
});
