/**
 * Rock Paper Scissors Game
 * This program simulates a simple Rock Paper Scissors game between a player and the computer.
 * The computer's choice is randomized, and the player's choice is input via prompt.
 * The program continues to play rounds until the player decides to quit.
 */

// Function to get a random choice for the computer
function getComputerChoice() {
    const choices = ['rock', 'paper', 'scissors'];
    const randomIndex = Math.floor(Math.random() * choices.length);
    return choices[randomIndex];
}

// Function to determine the winner of a round
function determineWinner(playerChoice, computerChoice) {
    if (playerChoice === computerChoice) {
        return 'It\'s a tie!';
    }
    if (
        (playerChoice === 'rock' && computerChoice === 'scissors') ||
        (playerChoice === 'scissors' && computerChoice === 'paper') ||
        (playerChoice === 'paper' && computerChoice === 'rock')
    ) {
        return 'You win!';
    }
    return 'Computer wins!';
}

// Function to validate the player's input
function isValidChoice(choice) {
    const validChoices = ['rock', 'paper', 'scissors'];
    return validChoices.includes(choice.toLowerCase());
}

// Main execution block
(function playGame() {
    let playAgain = true;

    while (playAgain) {
        const playerChoice = prompt("Enter your choice (rock, paper, scissors):").toLowerCase();

        if (!isValidChoice(playerChoice)) {
            alert("Invalid choice. Please enter rock, paper, or scissors.");
            continue;
        }

        const computerChoice = getComputerChoice();
        const result = determineWinner(playerChoice, computerChoice);

        alert(`You chose: ${playerChoice}\nComputer chose: ${computerChoice}\n${result}`);

        playAgain = confirm("Do you want to play again?");
    }

    alert("Thank you for playing Rock Paper Scissors!");
})();