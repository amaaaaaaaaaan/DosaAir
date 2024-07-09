let activefood;
async function dosamenuLoad() {
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
          <span class="dosa-price ">₹${dosa.price}</span>

        </button>`;
    weirdcon.insertAdjacentHTML("beforeend", ht);
  });
  nonveg.forEach((dosa) => {
    const ht = `<div class="dosa" onclick='selectdosa(this)'>
          <span class="dosa-name">${dosa.name}</span>
          <span class="dosa-price ">₹${dosa.price}</span>

        </div>`;
    nonvegcont.insertAdjacentHTML("beforeend", ht);
  });
  veg.forEach((dosa) => {
    const ht = `<div class="dosa" onclick='selectdosa(this)'>
          <span class="dosa-name">${dosa.name}</span>
          <span class="dosa-price ">₹${dosa.price}</span>

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
  html = `<div class="passenger">
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
                            <span>Food Choice</span>
                            <button class="login-text btn" onclick="showmenu(this)" >Menu</button>
                          </div>
                          <div class="login-inf">
                            <span>Age group</span>
                            <select class="login-text" >
                              <option value="">Select</option>
                                <option value="child">Child (0 - 13)</option>
                                <option value="adult">Adult (14 - 60)</option>
                                <option value="old">Senior Citizen (60+)</option>

                            </select>
                          </div>
                    </div>`;
  document.querySelector("#passengers").insertAdjacentHTML("beforebegin", html);
}

function bookpassengers() {
  const passengers = document.querySelectorAll(".passenger");
  const passengerDetails = [];

  passengers.forEach((passenger) => {
    const title = passenger.querySelector("select").value;
    var food = passenger.querySelector(".btn").innerText;
    food = food.split("\n₹");
    food[1] = Number(food[1]);
    const firstName = passenger.querySelector("input#username").value;
    const ageGroup = passenger.querySelectorAll("select")[1].value;

    passengerDetails.push({
      title: title,
      firstName: firstName,
      ageGroup: ageGroup,
      food: food,
    });
  });
  console.log(passengerDetails);
  return passengerDetails;
}
