let activefood;
async function dosamenuLoad() {
  userdata = await eel.userdata()();
  console.log();
  document.querySelector(".acc-name").innerText = userdata.name;
  document.querySelector("#ploc").innerText = userdata.ploc;
  const weirdcon = document.querySelector("#weird");
  const nonvegcont = document.querySelector("#non-veg");
  const vegcon = document.querySelector("#veg");
  const dosamenu = await eel.dosamenu()();
  const weird = dosamenu[0];
  const nonveg = dosamenu[1];
  const veg = dosamenu[2];
  weird.forEach((dosa) => {
    const ht = `<div class="dosa" onclick='selectdosa(this)'>
          <span class="dosa-name">${dosa.name}</span>
          <span class="dosa-price ">$${dosa.price}</span>

        </button>`;
    weirdcon.insertAdjacentHTML("beforeend", ht);
  });
  nonveg.forEach((dosa) => {
    const ht = `<div class="dosa" onclick='selectdosa(this)'>
          <span class="dosa-name">${dosa.name}</span>
          <span class="dosa-price ">$${dosa.price}</span>

        </div>`;
    nonvegcont.insertAdjacentHTML("beforeend", ht);
  });
  veg.forEach((dosa) => {
    const ht = `<div class="dosa" onclick='selectdosa(this)'>
          <span class="dosa-name">${dosa.name}</span>
          <span class="dosa-price ">$${dosa.price}</span>

        </div>`;
    vegcon.insertAdjacentHTML("beforeend", ht);
  });
}

async function loadFlight() {
  const flight = await eel.bookedFlight()();
  const html = `<div class="flight">
                <span class="flight-dest">${flight.from}</span>
                <div class="flight-take-off-icon"></div>
                <hr class="custom-hr">
                <div class="flight-bk">
                  <div class="flight-inf">
                  
                  
                    <div class="flight-dt">
                      <span class="flight-date">${flight.date}</span>
                              <span class="flight-date flight-time">${flight.time}</span>

        <span class="flight-time">$${flight.price}</span>
        <span class="flight-date flight-time">${flight.duration}</span>
                  </div>
                  
                  
                </div>
                </div>
                
                <hr class="custom-hr">
                <div class="flight-take-in-icon"></div>
                <span class="flight-dest">${flight.to}</span>
                </div>`;
  document.querySelector(".ticket").insertAdjacentHTML("afterbegin", html);
}

document.addEventListener("DOMContentLoaded", loadFlight());

document.addEventListener("DOMContentLoaded", dosamenuLoad());

function showmenu(e) {
  document.querySelector(".menu").classList.remove("hid");
  document.querySelector(".overlay").classList.remove("hid");
  document.querySelector(".overlay").style.opacity = 100;
  activefood = e;
}

function hidemenu() {
  document.querySelector(".menu").classList.add("hid");
  document.querySelector(".overlay").classList.add("hid");
}

function selectdosa(r) {
  activefood.innerText = r.innerText;
  hidemenu();
}

function addform() {
  html = ` <div class="passenger">
                      <h1 class="passenger-head">Passport details</h1>
                      <div class="passenger-cont">
                        <div class="login-inf">
                          <span>Title</span>
                          <select class="login-text" >
                            <option value="">Select</option>

                              <option value="Mr">Mr</option>
                              <option value="Mrs">Mrs</option>
                              <option value="Ms">Ms</option>
                              <option value="Miss">Miss</option>

                          </select>
                        </div>
                        <div class="login-inf">
                          <span>First Name</span>
                          <input class="login-text" id="username" type="text" name="" id="" />
                        </div>
                        <div class="login-inf">
                          <span>Last Name</span>
                          <input class="login-text" id="lasname" type="text" name="" id="" />
                        </div>
                       
                      </div>
                      <div class="passenger-cont">
                        <div class="login-inf">
                          <span>Age group</span>
                          <select class="login-text" >
                            <option value="">Select</option>
                              <option value="Child">Child (0 - 13) 50% fare</option>
                              <option value="Adult">Adult (14 - 60)</option>
                              <option value="Senior Citizen">Senior Citizen (60+) 80% fare</option>
                          </select>
                        </div>
                        <div class="login-inf">
                          <span>Nationality</span>
                          <select class="login-text" >
                            <option value="">Select</option>
                            <option value="afghan">Afghan</option>
                            <option value="albanian">Albanian</option>
                            <option value="algerian">Algerian</option>
                            <option value="american">American</option>
                            <option value="argentine">Argentine</option>
                            <option value="australian">Australian</option>
                            <option value="austrian">Austrian</option>
                            <option value="bangladeshi">Bangladeshi</option>
                            <option value="belgian">Belgian</option>
                            <option value="brazilian">Brazilian</option>
                            <option value="british">British</option>
                            <option value="canadian">Canadian</option>
                            <option value="chinese">Chinese</option>
                            <option value="danish">Danish</option>
                            <option value="egyptian">Egyptian</option>
                            <option value="french">French</option>
                            <option value="german">German</option>
                            <option value="indian">Indian</option>
                            <option value="indonesian">Indonesian</option>
                            <option value="iranian">Iranian</option>
                          </select>
                        </div>
                      </div>
                        <h1 class="passenger-head">Contact Details</h1>
                        <div class="passenger-cont">
                          <div class="login-inf">
                            <span>Email</span>
                            <input class="login-text" id="email" type="email" name="" id="" />
                          </div>
                          <div class="login-inf">
                            <span>Contact Number</span>
                            <input class="login-text" id="pho" type="tel" name="" id="" />
                          </div>
                        </div>
                        <h1 class="passenger-head">Extras</h1>
<div class="passenger-cont">
  <div class="login-inf">
    <span>Food Choice</span>
    <button class="login-text btn" onclick="showmenu(this)" >Show Menu</button>
  </div>
  <div class="login-inf">
    <span>Seat</span>
    <button class="login-text ste" onclick="showseat(this)" >Seating plan</button>
  </div>
  <div class="login-inf">
    <span>Baggage</span>
    <select class="login-text" >

        <option value="def">10Kg</option>
        <option value="premium">20Kg [+2% fare]</option>
        <option value="premium plus">40Kg [+4% fare]</option>

    </select>
  </div>
</div>
                         
                    </div>`;
  document.querySelector("#passengers").insertAdjacentHTML("beforebegin", html);
}

async function bookpassengers() {
  const passengers = document.querySelectorAll(".passenger");
  const passengerDetails = [];

  passengers.forEach((passenger) => {
    const title = passenger.querySelector("select").value;
    var food = passenger.querySelector(".btn").innerText;
    food = food.split("\n$");
    food[1] = Number(food[1]);
    const firstName = passenger.querySelector("input#username").value;
    const lastName = passenger.querySelector("input#lasname").value;
    const ageGroup = passenger.querySelectorAll("select")[1].value;
    const email = passenger.querySelector("input#email").value;
    const nationality = passenger.querySelectorAll("select")[2].value;
    const bgg = passenger.querySelectorAll("select")[3].value;
    const pho = passenger.querySelector("#pho").value;
    var seat = passenger.querySelector(".ste").innerText;
    if (
      firstName == "" ||
      title == "Select" ||
      food == "Menu" ||
      ageGroup == "Select"
    ) {
      alert("Please enter data properly");
    }
    //👉👉👉👉👉this is ur new passenger details mr.aman
    passengerDetails.push({
      title: title,
      firstName: firstName + " " + lastName,
      ageGroup: ageGroup,
      food: food,
      email: email,
      national: nationality,
      phone: pho,
      seat: seat,
      bgg: bgg,
    });
  });
  const totoalPrice = await eel.ticket(passengerDetails)();

  if (totoalPrice != "all good") {
    alert("Form not filled properly");
  }
  eel.saveTicket()();
  window.location.href = "../booked/index.html";
  return passengerDetails;
}

function showseat(e) {
  document.querySelector(".seats-cont").classList.remove("hid");
  document.querySelector(".overlay.seatings").classList.remove("hid");
  document.querySelector(".overlay.seatings").style.opacity = 100;
  activefood = e;
}

function hideseat() {
  document.querySelector(".seats-cont").classList.add("hid");
  document.querySelector(".overlay.seatings").classList.add("hid");
}

function addseat(a) {
  console.log(a.innerHTML);
}

const column = ["A", "B"];
let l = 1;
let k = 0;
async function updateseate() {
  return await eel.checkon_seats()();
}
let seats = updateseate();

document.querySelectorAll(".seat").forEach((seat) => {
  seat.innerHTML = column[k] + l;
  l = k == 1 ? l + 1 : l;
  k = k == 0 ? 1 : 0;

  seats.then((done) => {
    done.forEach((fof) => {
      if (fof[0] == seat.innerHTML) {
        seat.classList.add("bkd");
      }
    });
  });

  seat.addEventListener("click", async function () {
    activefood.innerHTML = seat.classList.contains("bkd")
      ? "seating plan"
      : seat.innerHTML;
    eel.seatchange(seat.innerHTML)();
    updateseate().then((q) => {
      if (q.length != seats.length) {
        document.querySelectorAll(".seat").forEach((o) => {
          console.log([o.innerHTML], q);
          q.forEach((qu) => {
            if (qu == o.innerHTML) {
              o.classList.add("bkd");
              if (activefood.innerHTML != "seating plan") {
                hideseat();
              }
            }
          });
        });
      }
    });
  });
});
