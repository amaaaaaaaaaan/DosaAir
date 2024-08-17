document.addEventListener("DOMContentLoaded", function () {
  var navbarHeight = document.querySelector(".head").offsetHeight;
  document.querySelector(".cont").style.marginTop = navbarHeight + "px";
});

async function destup() {
  const dests = await eel.getTop()();
  console.log(dests);
  dests.forEach((e) => {
    htl = `          <div class="dest-cont" onclick='sell("${e.name}","${e.air}")'>
<div class="dest-desc">
          <span class="dest-name">${e.name}</span>
          <span class="dest-air">${e.air}</span>
        </div>
        <img onclick='sell(${e.name},${e.air})' src="../dest-data/images/${e.name}.png" alt="" class="dest-img">
      </div></div>`;
    document.querySelector(".dest-main").insertAdjacentHTML("afterbegin", htl);
  });
}

destup();

function sell(k, j) {
  window.location.href = `../dest-detail/index.html?dest=${k}&air=${j}`;
}
