/**
 * TipCalculator Class
 * Handles the calculation of tips based on user inputs.
 */
class TipCalculator {
  /**
   * Calculate the tip amount.
   * @param {number} billAmount - The total bill amount.
   * @param {number} tipPercentage - The desired tip percentage.
   * @returns {number} - Calculated tip amount.
   */
  calculateTip(billAmount, tipPercentage) {
    if (typeof billAmount !== 'number' || typeof tipPercentage !== 'number') {
      throw new Error('Invalid input: Inputs must be numbers');
    }
    if (billAmount < 0 || tipPercentage < 0) {
      throw new Error('Invalid input: Numbers must be non-negative');
    }
    return billAmount * (tipPercentage / 100);
  }

  /**
   * Calculate the total amount (bill + tip).
   * @param {number} billAmount - The total bill amount.
   * @param {number} tipAmount - The calculated tip amount.
   * @returns {number} - Total amount to be paid.
   */
  calculateTotal(billAmount, tipAmount) {
    return billAmount + tipAmount;
  }
}

/**
 * Main execution block.
 * Handles user inputs and outputs the calculated tip and total amounts.
 */
(function main() {
  try {
    const billInput = prompt('Enter the bill amount:');
    const tipInput = prompt('Enter the tip percentage:');

    // Parse inputs as floats
    const billAmount = parseFloat(billInput);
    const tipPercentage = parseFloat(tipInput);

    const tipCalculator = new TipCalculator();

    // Calculate tip and total amounts
    const tipAmount = tipCalculator.calculateTip(billAmount, tipPercentage);
    const totalAmount = tipCalculator.calculateTotal(billAmount, tipAmount);

    // Output results
    console.log(`Bill Amount: $${billAmount.toFixed(2)}`);
    console.log(`Tip Percentage: ${tipPercentage.toFixed(2)}%`);
    console.log(`Tip Amount: $${tipAmount.toFixed(2)}`);
    console.log(`Total Amount: $${totalAmount.toFixed(2)}`);
  } catch (error) {
    console.error('Error:', error.message);
  }
})();