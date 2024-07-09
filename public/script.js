async function senduserdata(e) {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const loginconfirm = await eel.getdata(username, password)();
  if (loginconfirm == false) {
    const ms = document.getElementById("logmess");
    console.log(loginconfirm);
    ms.innerText = "Password or Username is wrong";
    ms.classList.add("shake");
    ms.style.animationPlayState = "initial";
  } else {
    window.location.href = "home.html";
    // console.log(eel.userdatapull);
    updateUserData();
  }
}

document.querySelector("#reg").addEventListener("click", function () {
  document.getElementById("login").classList.add("hid");
  document.getElementById("Register").classList.remove("hid");
});

document.getElementById("regbut").addEventListener("click", async function () {
  const username = document.getElementById("regus").value;
  const password = document.getElementById("regpas").value;
  const regconfirm = await eel.regdata(username, password)();
  if (regconfirm == true) {
    window.location.href = "home.html";
  } else {
    alert(regconfirm);
  }
});
