/**
 * Dark Mode Toggle
 * This program toggles between light and dark mode for a webpage.
 * It uses localStorage to persist the user's preference across sessions.
 */

// Function to toggle the dark mode
function toggleDarkMode() {
    try {
        // Access the current state from the document's class list
        const isDarkMode = document.body.classList.toggle('dark-mode');
        
        // Store the user's preference in localStorage
        localStorage.setItem('darkMode', isDarkMode ? 'enabled' : 'disabled');
    } catch (error) {
        console.error("Error toggling dark mode: ", error);
    }
}

// Function to initialize dark mode based on stored preference
function initializeDarkMode() {
    try {
        // Retrieve user's preference from localStorage
        const darkModePreference = localStorage.getItem('darkMode');
        
        // Set the initial mode based on the stored preference
        if (darkModePreference === 'enabled') {
            document.body.classList.add('dark-mode');
        } else {
            document.body.classList.remove('dark-mode');
        }
    } catch (error) {
        console.error("Error initializing dark mode: ", error);
    }
}

// Main execution block
document.addEventListener('DOMContentLoaded', () => {
    // Initialize dark mode on page load
    initializeDarkMode();

    // Set up the event listener for the toggle button
    const darkModeToggleButton = document.getElementById('darkModeToggle');
    if (darkModeToggleButton) {
        darkModeToggleButton.addEventListener('click', toggleDarkMode);
    } else {
        console.error("Dark mode toggle button not found");
    }
});



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dark Mode Toggle</title>
    <style>
        /* Basic styles for light and dark mode */
        body {
            transition: background-color 0.5s, color 0.5s;
        }
        body.dark-mode {
            background-color: #121212;
            color: #ffffff;
        }
    </style>
</head>
<body>
    <button id="darkModeToggle">Toggle Dark Mode</button>
    <script src="darkModeToggle.js"></script>
</body>
</html>