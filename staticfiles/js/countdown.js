var countDownDate = new Date("Jul 15, 2023 15:00:00").getTime();
console.log(countDownDate);

var x = setInterval(function() {

  var now = new Date().getTime();
  var distance = countDownDate - now;

  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  document.getElementById("CountdownDays").innerHTML = days
  document.getElementById("CountdownHours").innerHTML = hours
  document.getElementById("CountdownMinutes").innerHTML = minutes
  document.getElementById("CountdownSeconds").innerHTML = seconds

  if (distance < 0) {
    clearInterval(x);
    // The code below will not work, the .html element with the ID = 'countdown' does not exist
    //document.getElementById("countdown").innerHTML = "Ne-am casatorit!";
  }
}, 1000);