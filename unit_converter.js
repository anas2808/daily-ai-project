// Unit Converter Program

/**
 * Converts a given value from one unit to another.
 * Supports conversion for length, weight, and temperature.
 */

/**
 * Convert length units between meters, kilometers, and miles.
 * @param {number} value - The value to convert.
 * @param {string} fromUnit - The original unit of the value.
 * @param {string} toUnit - The unit to convert the value to.
 * @returns {number} - The converted value.
 * @throws Will throw an error if units are not supported.
 */
function convertLength(value, fromUnit, toUnit) {
    const conversionRates = {
        'meters': 1,
        'kilometers': 0.001,
        'miles': 0.000621371
    };

    if (!conversionRates[fromUnit] || !conversionRates[toUnit]) {
        throw new Error('Unsupported length unit');
    }

    return value * (conversionRates[toUnit] / conversionRates[fromUnit]);
}

/**
 * Convert weight units between grams, kilograms, and pounds.
 * @param {number} value - The value to convert.
 * @param {string} fromUnit - The original unit of the value.
 * @param {string} toUnit - The unit to convert the value to.
 * @returns {number} - The converted value.
 * @throws Will throw an error if units are not supported.
 */
function convertWeight(value, fromUnit, toUnit) {
    const conversionRates = {
        'grams': 1,
        'kilograms': 0.001,
        'pounds': 0.00220462
    };

    if (!conversionRates[fromUnit] || !conversionRates[toUnit]) {
        throw new Error('Unsupported weight unit');
    }

    return value * (conversionRates[toUnit] / conversionRates[fromUnit]);
}

/**
 * Convert temperature units between Celsius, Fahrenheit, and Kelvin.
 * @param {number} value - The value to convert.
 * @param {string} fromUnit - The original unit of the value.
 * @param {string} toUnit - The unit to convert the value to.
 * @returns {number} - The converted value.
 * @throws Will throw an error if units are not supported.
 */
function convertTemperature(value, fromUnit, toUnit) {
    if (fromUnit === 'Celsius') {
        if (toUnit === 'Fahrenheit') {
            return (value * 9/5) + 32;
        } else if (toUnit === 'Kelvin') {
            return value + 273.15;
        }
    } else if (fromUnit === 'Fahrenheit') {
        if (toUnit === 'Celsius') {
            return (value - 32) * 5/9;
        } else if (toUnit === 'Kelvin') {
            return (value - 32) * 5/9 + 273.15;
        }
    } else if (fromUnit === 'Kelvin') {
        if (toUnit === 'Celsius') {
            return value - 273.15;
        } else if (toUnit === 'Fahrenheit') {
            return (value - 273.15) * 9/5 + 32;
        }
    }
    throw new Error('Unsupported temperature unit');
}

/**
 * Main execution block
 */
(function() {
    try {
        // Sample usage:
        console.log('Length Conversion: 1000 meters to kilometers:', convertLength(1000, 'meters', 'kilometers'));
        console.log('Weight Conversion: 500 grams to pounds:', convertWeight(500, 'grams', 'pounds'));
        console.log('Temperature Conversion: 100 Celsius to Fahrenheit:', convertTemperature(100, 'Celsius', 'Fahrenheit'));
    } catch (error) {
        console.error('Conversion Error:', error.message);
    }
})();