/**
 * Drum Kit Application
 * This application allows users to play different drum sounds by clicking on buttons or pressing specific keys.
 * Each button on the screen corresponds to a drum sound and a specific keyboard key.
 */

// Function to play the sound based on the key pressed or button clicked
function playSound(key) {
    const audio = document.querySelector(`audio[data-key="${key}"]`);
    const button = document.querySelector(`.drum[data-key="${key}"]`);
    
    if (!audio) return; // If there's no audio for the key, exit the function

    audio.currentTime = 0; // Rewind to the start to allow rapid succession playback
    audio.play();
    
    button.classList.add('playing'); // Add visual feedback when the sound plays

    // Remove the visual feedback after the transition ends
    button.addEventListener('transitionend', function() {
        button.classList.remove('playing');
    });
}

// Event listener for keydown events
function handleKeydown(event) {
    playSound(event.key.toLowerCase());
}

// Event listener for button clicks
function handleButtonClick(event) {
    playSound(event.target.getAttribute('data-key'));
}

// Main execution block
document.addEventListener('DOMContentLoaded', () => {
    // Add event listener for keydown events
    window.addEventListener('keydown', handleKeydown);

    // Add event listeners to each drum button
    const drumButtons = document.querySelectorAll('.drum');
    drumButtons.forEach(button => {
        button.addEventListener('click', handleButtonClick);
    });
});

/* Sample HTML structure to be used with this script:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Drum Kit</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="drum-kit">
        <button class="drum" data-key="a">A</button>
        <button class="drum" data-key="s">S</button>
        <button class="drum" data-key="d">D</button>
        <button class="drum" data-key="f">F</button>
        <!-- Add more buttons as needed -->
    </div>
    <audio data-key="a" src="sounds/clap.wav"></audio>
    <audio data-key="s" src="sounds/hihat.wav"></audio>
    <audio data-key="d" src="sounds/kick.wav"></audio>
    <audio data-key="f" src="sounds/openhat.wav"></audio>
    <!-- Add more audio elements as needed -->
    <script src="script.js"></script>
</body>
</html>

Sample CSS (styles.css) for button styling and playing effect:
body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #282c34;
}

.drum-kit {
    display: flex;
}

.drum {
    margin: 0 5px;
    padding: 20px 40px;
    border: none;
    border-radius: 5px;
    background-color: #61dafb;
    color: white;
    font-size: 24px;
    cursor: pointer;
    transition: all 0.1s;
}

.drum.playing {
    transform: scale(1.1);
    background-color: #21a1f1;
}
*/