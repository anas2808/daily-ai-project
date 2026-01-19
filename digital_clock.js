// Function to add leading zeros to numbers less than 10
function formatNumber(number) {
    return number < 10 ? '0' + number : number;
}

// Function to update the digital clock display
function updateClock() {
    try {
        const currentTime = new Date();

        // Extract hours, minutes, and seconds from the current time
        const hours = currentTime.getHours();
        const minutes = currentTime.getMinutes();
        const seconds = currentTime.getSeconds();

        // Format time components with leading zeros if needed
        const formattedHours = formatNumber(hours);
        const formattedMinutes = formatNumber(minutes);
        const formattedSeconds = formatNumber(seconds);

        // Get the clock display element by its ID
        const clockDisplayElement = document.getElementById('clockDisplay');
        if (!clockDisplayElement) {
            throw new Error('Clock display element not found.');
        }

        // Update the display element's text content with the formatted time
        clockDisplayElement.textContent = `${formattedHours}:${formattedMinutes}:${formattedSeconds}`;
    } catch (error) {
        console.error('Error updating clock:', error.message);
    }
}

// Main function to initialize and start the digital clock
function startDigitalClock() {
    try {
        // Ensure the DOM is fully loaded before attempting to access elements
        document.addEventListener('DOMContentLoaded', () => {
            // Set an interval to update the clock every second
            setInterval(updateClock, 1000);
        });
    } catch (error) {
        console.error('Error starting digital clock:', error.message);
    }
}

// Main execution block
startDigitalClock();



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Clock</title>
    <style>
        /* Basic styling for the clock display */
        #clockDisplay {
            font-size: 2em;
            font-family: 'Courier New', Courier, monospace;
            text-align: center;
            margin-top: 20%;
        }
    </style>
</head>
<body>
    <!-- Clock display element -->
    <div id="clockDisplay">00:00:00</div>

    <!-- Link to the JavaScript file -->
    <script src="path_to_your_script.js"></script>
</body>
</html>