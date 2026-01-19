// Countdown Timer Program

/**
 * Countdown Timer class that allows setting a timer duration
 * and provides start, pause, and reset functionalities.
 * It also updates the display every second.
 */
class CountdownTimer {
    constructor(duration, displayElement) {
        this.duration = duration; // Duration in seconds
        this.remainingTime = duration;
        this.displayElement = displayElement;
        this.timerInterval = null;
    }

    /**
     * Starts the countdown timer.
     */
    start() {
        if (this.timerInterval) return; // Prevent multiple intervals
        
        this.timerInterval = setInterval(() => {
            this.remainingTime -= 1;
            this.updateDisplay();

            if (this.remainingTime <= 0) {
                clearInterval(this.timerInterval);
                this.timerInterval = null;
                this.remainingTime = 0;
                this.updateDisplay();
                alert("Time's up!");
            }
        }, 1000);
    }

    /**
     * Pauses the countdown timer.
     */
    pause() {
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
            this.timerInterval = null;
        }
    }

    /**
     * Resets the countdown timer to its initial duration.
     */
    reset() {
        this.pause();
        this.remainingTime = this.duration;
        this.updateDisplay();
    }

    /**
     * Updates the countdown display.
     */
    updateDisplay() {
        const minutes = Math.floor(this.remainingTime / 60);
        const seconds = this.remainingTime % 60;
        this.displayElement.textContent = `${this.formatTime(minutes)}:${this.formatTime(seconds)}`;
    }

    /**
     * Formats time to ensure double-digit display.
     * @param {number} time - The time component to format.
     * @returns {string} - Formatted time with leading zero if necessary.
     */
    formatTime(time) {
        return time < 10 ? `0${time}` : time;
    }
}

/**
 * Main execution block when DOM is fully loaded.
 */
document.addEventListener('DOMContentLoaded', () => {
    const displayElement = document.querySelector('#timer-display');
    const startButton = document.querySelector('#start-button');
    const pauseButton = document.querySelector('#pause-button');
    const resetButton = document.querySelector('#reset-button');

    // Initial duration is set to 5 minutes (300 seconds)
    const timer = new CountdownTimer(300, displayElement);

    startButton.addEventListener('click', () => timer.start());
    pauseButton.addEventListener('click', () => timer.pause());
    resetButton.addEventListener('click', () => timer.reset());

    timer.updateDisplay(); // Initial display update
});



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
    <style>
        #timer-display {
            font-size: 48px;
            margin-bottom: 20px;
        }
        button {
            font-size: 24px;
        }
    </style>
</head>
<body>
    <div id="timer-display">05:00</div>
    <button id="start-button">Start</button>
    <button id="pause-button">Pause</button>
    <button id="reset-button">Reset</button>
    <script src="countdown-timer.js"></script>
</body>
</html>