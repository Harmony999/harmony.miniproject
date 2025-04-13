document.addEventListener("DOMContentLoaded", function () {
    console.log("games.js loaded! ✅");
let balloon = document.getElementById("balloon");
if (balloon) {
        console.log("Balloon button found! 🎈");
balloon.addEventListener("click", function () {
            console.log("Balloon clicked! 💥");
 balloon.style.display = "none"; //this hides the balloon
            alert("Boom! 🎈 You popped the balloon!");
        });
   } else {
        console.error("Balloon button not found! ❌");
    }
});