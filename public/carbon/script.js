document.querySelector(".mess-btn").addEventListener("click", function () {
  window.location.href = "../booked/index.html";
});

document.addEventListener("DOMContentLoaded", async function () {
  const carbon = await eel.carboncalc()();
  document.querySelector("#carbs").innerHTML = carbon[0];
  document.querySelector("#plnt").innerHTML = carbon[1];
});
