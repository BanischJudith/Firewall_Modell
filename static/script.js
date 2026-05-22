function meldung() {
    const div1 = document.getElementById("erfolg");
    const div2 = document.getElementById("fehler");
    const imgGreen = document.querySelector(".server");
    const imgRed = document.querySelector(".server");

    if (div2.style.display === "none") {
    div2.style.display = "block";
    div1.style.display = "none";
    imgRed.style.backgroundColor = "var(--fehler)";
    } 
    else {
    div2.style.display = "none";
    div1.style.display = "block";
    imgGreen.style.backgroundColor = "var(--erfolg)";
   }
}
