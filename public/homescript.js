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
  smartRoutes.forEach((flight) => {
    const htm = `<div class="flight">
<div class="flight-dest-cont">
            <span class="flight-date flight-time">${flight.from}</span>
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
          <button class="flight-booking">BOOK</button>
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
