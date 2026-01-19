/**
 * BMI Calculator
 * This program calculates the Body Mass Index (BMI) based on user input
 * for weight (in kilograms) and height (in meters).
 */

// Function to calculate BMI
function calculateBMI(weight, height) {
    // Validate input
    if (typeof weight !== 'number' || typeof height !== 'number') {
        throw new Error('Invalid input: Weight and height should be numbers.');
    }

    if (weight <= 0 || height <= 0) {
        throw new Error('Invalid input: Weight and height must be greater than zero.');
    }

    // BMI calculation
    const bmi = weight / (height * height);

    // Return the calculated BMI
    return bmi.toFixed(2);
}

// Function to determine BMI classification
function getBMIClassification(bmi) {
    // Validate BMI
    if (typeof bmi !== 'number' || bmi <= 0) {
        throw new Error('Invalid BMI value.');
    }

    // Determine the BMI classification
    if (bmi < 18.5) {
        return 'Underweight';
    } else if (bmi < 24.9) {
        return 'Normal weight';
    } else if (bmi < 29.9) {
        return 'Overweight';
    } else {
        return 'Obesity';
    }
}

// Main execution block
(function main() {
    try {
        // Example input values
        const weightInKg = 70; // User-provided weight in kilograms
        const heightInMeters = 1.75; // User-provided height in meters

        // Calculate BMI
        const bmi = parseFloat(calculateBMI(weightInKg, heightInMeters));

        // Get BMI classification
        const classification = getBMIClassification(bmi);

        // Output the results
        console.log(`Your BMI is: ${bmi}`);
        console.log(`BMI Classification: ${classification}`);
    } catch (error) {
        // Handle any errors that occur during the BMI calculation
        console.error('Error:', error.message);
    }
})();