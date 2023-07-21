// counter coding
let counts = setInterval(updated, 600);
let upto = 0;
function updated() {
    var count = document.getElementById("counts1");
    count.innerHTML = ++upto;
    if (upto == 5) {
        clearInterval(counts);
    }
}
let counts1 = setInterval(updated1, 120);
let upto1 = 0;
function updated1() {
    var count1 = document.getElementById("counts2");
    count1.innerHTML = ++upto1;
    if (upto1 == 15) {
        clearInterval(counts1);
    }
}
let counts2 = setInterval(updated2, 30);
let upto2 = 0;
function updated2() {
    var count2 = document.getElementById("counts3");
    count2.innerHTML = ++upto2;
    if (upto2 == 350) {
        clearInterval(counts2);
    }
}