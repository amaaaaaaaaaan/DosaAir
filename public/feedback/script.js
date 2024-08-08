document.addEventListener("DOMContentLoaded", function () {
  var navbarHeight = document.querySelector(".head").offsetHeight;
  document.querySelector(".cont").style.marginTop = navbarHeight + "px";
});

function eraseFeeds() {
  try {
    document.querySelectorAll(".ticket-passenger").forEach((t) => {
      t.classList.add("hid");
    });
  } catch {
    console.error("nah bro");
  }
}

async function updateFeeds() {
  const feeds = await eel.getfeedback()();
  console.log(feeds);
  feeds.forEach((feed) => {
    html = ` <div class="ticket-passenger flight flight-marg ">
        
        <h2 class="price-cont">${feed[0]}<br> <p class="price" >${feed[1]}</p></h2>
          </div>`;
    document
      .querySelector("#startkaro")
      .insertAdjacentHTML("beforebegin", html);
  });
  window.scrollTo(0, document.body.scrollHeight);
  document.querySelector(".feeds").value = "";
}

document.addEventListener("DOMContentLoaded", updateFeeds());

document.querySelector(".feeds-btn").addEventListener("click", function () {
  const inb = document.querySelector(".feeds");
  console.log(document.querySelector(".feeds").value);

  eel.writefeedback(document.querySelector(".feeds").value)();
  eraseFeeds();
  updateFeeds();
});

document.addEventListener("keydown", function (e) {
  if (
    document.activeElement == document.querySelector(".feeds") &&
    e.key == "Enter"
  ) {
    eel.writefeedback(document.querySelector(".feeds").value)();
    eraseFeeds();
    updateFeeds();
  }
});
