// Length of our timers
// 25 minutes, 5 minutes, 10 minutes
var pomodoroInterval = 1500000;
var shortBreakInterval = 300000;
var longBreakInterval = 900000;

var moveOn = false; // If we want to move on to breaks automatically
var running = false; // If a timer is currrently running

// Pieces of text
var completedText = "You are finished!";
var shortBreakText = "Short break is over.";
var longBreakText = "Long break is over.";

// Nice format function
// first, checks if it isn't implemented yet
if (!String.prototype.format) {
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) { 
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}

function updateTimer(timer, remaining) {
	remaining -= 1000;
	var minutes = Math.floor(remaining / 60000);
	var seconds = Math.floor((remaining - minutes * 60000) / 1000);

	if (minutes >= 1) {
		text = "{0} minutes and {1} seconds remaining".format(minutes, seconds);
	} else {
		text = "{0} seconds remaining".format(seconds);
	}
	
	timer.innerHTML = text;
	return remaining;
}

function runTimer(interval, doneText) {
	if (!running) {
		console.log("Starting timer...");
		running = true;

		var start = new Date;
		var bell = document.getElementById("bell");
		var timer = document.getElementById("timer");
		
		// Update the text initially
		// Start with 1 sec. extra because updateTimer subtracts a sec.
		var timeLeft = updateTimer(timer, interval + 1000);

		// Every second update the timer
		updater = setInterval(function () {
			timeLeft = updateTimer(timer, timeLeft)
		}, 1000);
		
		// Display finished message and play bell after interval is complete
		finished = setInterval(function() {
			console.log(doneText);
			bell.play();
			timer.innerHTML = doneText;
			running = false;
			clearInterval(updater);
			clearInterval(finished);
		}, interval);
	}
}
