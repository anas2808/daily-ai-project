/**
 * URL Shortener Logic
 * This script provides a simple URL shortening service. It generates short URLs
 * for given long URLs and can also retrieve the original long URL from a short URL.
 */

// Store for URL mappings
const urlDatabase = new Map();

// Characters used for generating short URLs
const characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
const base = characters.length;

/**
 * Generates a short URL key for a given long URL.
 * @param {string} longUrl - The original long URL to be shortened.
 * @returns {string} - A unique short URL key.
 */
function generateShortUrl(longUrl) {
    let shortUrlKey;
    
    // Check if longUrl already has a mapping
    for (let [key, value] of urlDatabase.entries()) {
        if (value === longUrl) {
            return key;
        }
    }

    // Generate a new short URL key
    do {
        shortUrlKey = createRandomKey();
    } while (urlDatabase.has(shortUrlKey));

    // Store the mapping
    urlDatabase.set(shortUrlKey, longUrl);
    return shortUrlKey;
}

/**
 * Creates a random string used as a short URL key.
 * @returns {string} - A random short string.
 */
function createRandomKey() {
    let result = '';
    for (let i = 0; i < 6; i++) {  // 6-character short URL key
        result += characters.charAt(Math.floor(Math.random() * base));
    }
    return result;
}

/**
 * Retrieves the original long URL from a given short URL key.
 * @param {string} shortUrlKey - The short URL key.
 * @returns {string|null} - The original long URL or null if not found.
 */
function getLongUrl(shortUrlKey) {
    if (urlDatabase.has(shortUrlKey)) {
        return urlDatabase.get(shortUrlKey);
    } else {
        throw new Error('Short URL does not exist.');
    }
}

/**
 * Main execution block to demonstrate URL shortening logic.
 */
(function main() {
    try {
        const longUrl = 'https://www.example.com/some/very/long/url';
        const shortUrlKey = generateShortUrl(longUrl);
        console.log(`Short URL Key: ${shortUrlKey}`);
        
        const retrievedLongUrl = getLongUrl(shortUrlKey);
        console.log(`Retrieved Long URL: ${retrievedLongUrl}`);
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
})();