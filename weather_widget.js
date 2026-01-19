// Weather Widget - A JavaScript application to display the current weather of a specified city
// This application retrieves weather data from a public API and displays it on the webpage.

// Constants
const API_KEY = 'your_api_key_here'; // Replace with your actual API key from OpenWeatherMap
const WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather';

// DOM Elements
const cityInput = document.querySelector('#city-input');
const weatherDisplay = document.querySelector('#weather-display');
const errorDisplay = document.querySelector('#error-display');

// Function to fetch weather data
async function fetchWeather(city) {
    try {
        const response = await fetch(`${WEATHER_API_URL}?q=${city}&appid=${API_KEY}&units=metric`);
        
        if (!response.ok) {
            throw new Error('City not found');
        }

        const data = await response.json();
        displayWeather(data);
    } catch (error) {
        displayError(error.message);
    }
}

// Function to display weather data
function displayWeather(data) {
    const { name, main, weather } = data;
    weatherDisplay.innerHTML = `
        <h2>Weather in ${name}</h2>
        <p>Temperature: ${main.temp} °C</p>
        <p>Weather: ${weather[0].description}</p>
    `;
    errorDisplay.textContent = ''; // Clear any previous errors
}

// Function to display error messages
function displayError(message) {
    errorDisplay.textContent = `Error: ${message}`;
    weatherDisplay.innerHTML = ''; // Clear any previous weather data
}

// Function to handle form submission
function handleFormSubmit(event) {
    event.preventDefault();
    const city = cityInput.value.trim();
    if (city) {
        fetchWeather(city);
    } else {
        displayError('Please enter a city name');
    }
}

// Main execution block
function main() {
    const form = document.querySelector('#weather-form');
    form.addEventListener('submit', handleFormSubmit);
}

// Initialize the application
document.addEventListener('DOMContentLoaded', main);