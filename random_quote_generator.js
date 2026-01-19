// Random Quote Generator

// Array of quote objects, each containing a quote and its author
const quotes = [
    { quote: "The greatest glory in living lies not in never falling, but in rising every time we fall.", author: "Nelson Mandela" },
    { quote: "The way to get started is to quit talking and begin doing.", author: "Walt Disney" },
    { quote: "Your time is limited, so don't waste it living someone else's life.", author: "Steve Jobs" },
    { quote: "If life were predictable it would cease to be life, and be without flavor.", author: "Eleanor Roosevelt" },
    { quote: "If you look at what you have in life, you'll always have more.", author: "Oprah Winfrey" },
    { quote: "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.", author: "James Cameron" },
    { quote: "Life is what happens when you're busy making other plans.", author: "John Lennon" }
];

/**
 * Function to generate a random integer between min (inclusive) and max (exclusive)
 * @param {number} min - The minimum value (inclusive)
 * @param {number} max - The maximum value (exclusive)
 * @returns {number} - A random integer
 */
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

/**
 * Function to get a random quote
 * @returns {Object} - An object containing a random quote and its author
 */
function getRandomQuote() {
    try {
        // Get a random index from quotes array
        const randomIndex = getRandomInt(0, quotes.length);
        // Return the quote at the random index
        return quotes[randomIndex];
    } catch (error) {
        console.error("Error fetching the random quote:", error);
        // Return an empty quote object in case of error
        return { quote: "Error fetching quote", author: "" };
    }
}

/**
 * Function to display a random quote
 */
function displayRandomQuote() {
    const randomQuote = getRandomQuote();
    console.log(`"${randomQuote.quote}" - ${randomQuote.author}`);
}

// Main execution block
(function main() {
    try {
        // Display a random quote
        displayRandomQuote();
    } catch (error) {
        console.error("Error executing the main function:", error);
    }
})();