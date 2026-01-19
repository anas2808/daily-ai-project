/**
 * Pomodoro Timer
 * A simple timer application based on the Pomodoro Technique.
 * It alternates between work sessions and short break sessions.
 * 
 * Author: Senior JavaScript Developer
 * Date: 2023
 */

// Constants for the timer durations
const WORK_DURATION = 25 * 60; // 25 minutes in seconds
const BREAK_DURATION = 5 * 60; // 5 minutes in seconds
const SECOND = 1000; // 1 second in milliseconds

// State variables
let isRunning = false;
let isWorkSession = true;
let timeRemaining = WORK_DURATION;
let timerInterval;

/**
 * Formats a time in seconds to a MM:SS string.
 * @param {number} seconds - The time in seconds.
 * @returns {string} The formatted time string.
 */
function formatTime(seconds) {
  const minutes = Math.floor(seconds / 60);
  const secs = seconds % 60;
  return `${minutes < 10 ? '0' : ''}${minutes}:${secs < 10 ? '0' : ''}${secs}`;
}

/**
 * Updates the countdown display on the UI.
 */
function updateDisplay() {
  const displayElement = document.getElementById('timer-display');
  displayElement.textContent = formatTime(timeRemaining);
}

/**
 * Toggles between starting and stopping the timer.
 */
function toggleTimer() {
  if (isRunning) {
    stopTimer();
  } else {
    startTimer();
  }
}

/**
 * Starts the timer countdown.
 */
function startTimer() {
  if (!isRunning) {
    isRunning = true;
    timerInterval = setInterval(countdown, SECOND);
  }
}

/**
 * Stops the timer countdown.
 */
function stopTimer() {
  if (isRunning) {
    clearInterval(timerInterval);
    isRunning = false;
  }
}

/**
 * Resets the timer to the initial state based on the current session type.
 */
function resetTimer() {
  stopTimer();
  timeRemaining = isWorkSession ? WORK_DURATION : BREAK_DURATION;
  updateDisplay();
}

/**
 * Handles the timer countdown logic.
 */
function countdown() {
  if (timeRemaining > 0) {
    timeRemaining--;
    updateDisplay();
  } else {
    switchSession();
  }
}

/**
 * Switches between work and break sessions.
 */
function switchSession() {
  stopTimer();
  isWorkSession = !isWorkSession;
  timeRemaining = isWorkSession ? WORK_DURATION : BREAK_DURATION;
  updateDisplay();
  // Optionally, you can alert the user or play a sound here
}

/**
 * Attaches event listeners to the UI buttons.
 */
function setupEventListeners() {
  document.getElementById('start-stop-button').addEventListener('click', toggleTimer);
  document.getElementById('reset-button').addEventListener('click', resetTimer);
}

/**
 * Initializes the Pomodoro Timer application.
 */
function initPomodoroTimer() {
  updateDisplay();
  setupEventListeners();
}

// Main execution block
document.addEventListener('DOMContentLoaded', initPomodoroTimer);