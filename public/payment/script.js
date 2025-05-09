const inputs = document.querySelectorAll(".otp-field > input");
var filled = false;
window.addEventListener("load", () => inputs[0].focus());
var bkd = `<button id="053s" onclick='jfj(5) '>Open</button>`;
const h = ["h", "e", "h", "e"];

inputs[0].addEventListener("paste", function (event) {
  event.preventDefault();
  const pastedValue = (event.clipboardData || window.clipboardData).getData(
    "text"
  );
  const otpLength = inputs.length;

  for (let i = 0; i < otpLength; i++) {
    if (i < pastedValue.length) {
      inputs[i].value = pastedValue[i];
      inputs[i].removeAttribute("disabled");
      inputs[i].focus;
    } else {
      inputs[i].value = ""; // Clear any remaining inputs
      inputs[i].focus;
    }
  }
});
const y = [0, 5, 45, 35, 3, 0.45, bkd, 56.4, 354.3, 5, 5, 4.4];

inputs.forEach((input, index1) => {
  input.addEventListener("keyup", (e) => {
    const currentInput = input;
    const nextInput = input.nextElementSibling;
    const prevInput = input.previousElementSibling;

    if (currentInput.value.length > 1) {
      currentInput.value = "";
      return;
    }

    if (
      nextInput &&
      nextInput.hasAttribute("disabled") &&
      currentInput.value !== ""
    ) {
      nextInput.removeAttribute("disabled");
      nextInput.focus();
    }

    if (e.key === "Backspace") {
      inputs.forEach((input, index2) => {
        if (index1 <= index2 && prevInput) {
          input.setAttribute("disabled", true);
          input.value = "";
          prevInput.focus();
        }
      });
    }

    const inputsNo = inputs.length;
    if (!inputs[inputsNo - 1].disabled && inputs[inputsNo - 1].value !== "") {
      var val = "";
      inputs.forEach((e) => {
        val += e.value;
        if (val.length == 4) {
          filled = true;
          document.querySelector(".mess-btn").focus();
        } else {
          filled = false;
        }
      });

      return;
    }
  });
});

document.querySelector(".mess-btn").addEventListener("click", function () {
  if (document.querySelector(".inp-b").value && filled) {
    window.location.href = "../booked/index.html";
  } else {
    document.querySelectorAll(".mess-para")[0].style.color = "red";
    document.querySelectorAll(".mess-para")[0].innerHTML =
      "Fill values properly";
  }
});
