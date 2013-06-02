// Length of our timers
// 25 minutes, 5 minutes, 10 minutes
pomodoroInterval = 1500000;
shortBreakInterval = 300000;
longBreakInterval = 900000;

moveOn = false; // If we want to move on to breaks automatically

// Pieces of text
completedText = "You are finished!";
shortBreakText = "Short break is over.";
longBreakText = "Long break is over.";

function runTimer(interval, doneText) {
	var start = new Date;
	var bell = document.getElementById("bell");
	var timer = document.getElementById("timer");

	// Every second update the timer
	setInterval(function() {
		remaining = new Date - start;
		minutes = remaining / 60000;
		seconds = remaining / 1000;

		if (minutes >= 1) {
			text = "{0} minutes and {1} seconds remaining".format(minutes, seconds);
		} else {
			text = "{1} seconds remaining".format(seconds);
		}
		
		timer.innerHTML = text;
	}, 1000);
	
	setInterval(function() {
		bell.play();
		timer.innerHTML = doneText;
	}, interval);
}
