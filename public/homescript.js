async function updateUserData() {
  userdata = await eel.userdata()();
  console.log();
  document.querySelector(".acc-name").innerText = userdata.name;
  document.querySelector("#ploc").innerText = userdata.ploc;
  const smartRoutes = await eel.smartRoutes()();
  console.log(smartRoutes);
  smartRoutes.forEach((flight) => {
    const htm = `<div class="flight">
          <span class="flight-dest">${flight.FromDest}</span>
          <div class="flight-take-off-icon"></div>
          <hr class="custom-hr">
          <div class="flight-bk">
            <div class="flight-inf dw">
            
            
              <div class="flight-dt">
                <span class="flight-date">Monday 20 May</span>
  <span class="flight-time">$${flight.Price}</span>
  <span class="flight-date flight-time">4H 24Mins</span>
            </div>
            
            
          </div>
          <button class="flight-booking">BOOK</button>
          </div>
          
          <hr class="custom-hr">
          <div class="flight-take-in-icon"></div>
          <span class="flight-dest">${flight.ToDest}</span>
          </div>`;
    document.querySelector("#startkaro").insertAdjacentHTML("afterend", htm);
  });
}

document.onload(updateUserData());
