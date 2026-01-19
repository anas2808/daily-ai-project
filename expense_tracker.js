// Expense Tracker Application

/**
 * Expense class to create expense objects
 */
class Expense {
    constructor(id, description, amount, date) {
        this.id = id;
        this.description = description;
        this.amount = amount;
        this.date = date;
    }
}

/**
 * ExpenseTracker class to manage expenses
 */
class ExpenseTracker {
    constructor() {
        this.expenses = [];
    }

    /**
     * Add a new expense
     * @param {string} description - Description of the expense
     * @param {number} amount - Amount of the expense
     * @param {Date} date - Date of the expense
     */
    addExpense(description, amount, date = new Date()) {
        try {
            if (typeof description !== 'string' || typeof amount !== 'number') {
                throw new Error('Invalid input types');
            }
            const id = this.expenses.length ? this.expenses[this.expenses.length - 1].id + 1 : 1;
            const newExpense = new Expense(id, description, amount, date);
            this.expenses.push(newExpense);
            console.log('Expense added successfully');
        } catch (error) {
            console.error('Error adding expense:', error.message);
        }
    }

    /**
     * Remove an expense by ID
     * @param {number} id - ID of the expense to remove
     */
    removeExpense(id) {
        try {
            const initialLength = this.expenses.length;
            this.expenses = this.expenses.filter(expense => expense.id !== id);
            if (this.expenses.length === initialLength) {
                throw new Error('Expense not found');
            }
            console.log('Expense removed successfully');
        } catch (error) {
            console.error('Error removing expense:', error.message);
        }
    }

    /**
     * Display all expenses
     */
    displayExpenses() {
        try {
            if (this.expenses.length === 0) {
                console.log('No expenses to display');
                return;
            }
            console.log('Current Expenses:');
            this.expenses.forEach(expense => {
                console.log(`ID: ${expense.id}, Description: ${expense.description}, Amount: $${expense.amount}, Date: ${expense.date}`);
            });
        } catch (error) {
            console.error('Error displaying expenses:', error.message);
        }
    }

    /**
     * Calculate total expense amount
     * @returns {number} Total amount of all expenses
     */
    calculateTotal() {
        try {
            const total = this.expenses.reduce((acc, curr) => acc + curr.amount, 0);
            console.log(`Total Expenses: $${total}`);
            return total;
        } catch (error) {
            console.error('Error calculating total expenses:', error.message);
        }
    }
}

/**
 * Main execution block
 */
(function main() {
    const expenseTracker = new ExpenseTracker();
    
    expenseTracker.addExpense('Groceries', 50);
    expenseTracker.addExpense('Movie Tickets', 30);
    
    expenseTracker.displayExpenses();
    expenseTracker.calculateTotal();
    
    expenseTracker.removeExpense(1);
    expenseTracker.displayExpenses();
    expenseTracker.calculateTotal();
})();