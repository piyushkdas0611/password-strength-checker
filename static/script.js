document.getElementById("btn").addEventListener("click", () => {
  var password = document.getElementById("password").value;
  fetch("/check_password_strength", {
    method: "POST",
    body: new URLSearchParams({ password: password }),
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
  })
    .then((response) => response.json())
    .then((data) => {
      var resultElement = document.getElementById("result");
      resultElement.innerHTML = data.is_strong
        ? "Password is strong!"
        : "Password is weak. Please improve it.";
    });
});
