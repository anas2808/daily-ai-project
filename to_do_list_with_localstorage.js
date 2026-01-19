/**
 * To-Do List Application
 * This application allows users to add, delete, and persist to-do tasks using LocalStorage.
 */

document.addEventListener('DOMContentLoaded', main);

/**
 * Main execution block for initial setup and event listener attachments.
 */
function main() {
    const form = document.getElementById('todo-form');
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('task-list');

    // Initialize tasks from LocalStorage
    loadTasksFromLocalStorage();

    // Event listener for form submission to add new tasks
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const taskText = taskInput.value.trim();

        if (taskText) {
            addTask(taskText);
            taskInput.value = ''; // Clear input field
        } else {
            alert('Please enter a task.');
        }
    });

    // Event delegation for deleting tasks
    taskList.addEventListener('click', function(event) {
        if (event.target.classList.contains('delete-task')) {
            const taskItem = event.target.parentElement;
            deleteTask(taskItem);
        }
    });
}

/**
 * Add a task to the list and LocalStorage.
 * @param {string} taskText - The text of the task to be added.
 */
function addTask(taskText) {
    const taskList = document.getElementById('task-list');
    const taskItem = document.createElement('li');
    taskItem.className = 'task-item';
    taskItem.textContent = taskText;

    // Create delete button
    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-task';
    deleteBtn.textContent = 'Delete';
    taskItem.appendChild(deleteBtn);

    // Append task to the list
    taskList.appendChild(taskItem);
    
    // Persist to LocalStorage
    saveTaskToLocalStorage(taskText);
}

/**
 * Delete a task from the list and LocalStorage.
 * @param {HTMLElement} taskItem - The list item element containing the task to be deleted.
 */
function deleteTask(taskItem) {
    if (confirm('Are you sure you want to delete this task?')) {
        taskItem.remove();
        removeTaskFromLocalStorage(taskItem.textContent.replace('Delete', '').trim());
    }
}

/**
 * Load all tasks from LocalStorage and display them in the list.
 */
function loadTasksFromLocalStorage() {
    const tasks = getTasksFromLocalStorage();
    tasks.forEach(taskText => addTask(taskText));
}

/**
 * Retrieve tasks from LocalStorage.
 * @returns {Array<string>} An array of task strings.
 */
function getTasksFromLocalStorage() {
    const tasks = localStorage.getItem('tasks');
    return tasks ? JSON.parse(tasks) : [];
}

/**
 * Save a new task to LocalStorage.
 * @param {string} taskText - The text of the task to be saved.
 */
function saveTaskToLocalStorage(taskText) {
    const tasks = getTasksFromLocalStorage();
    tasks.push(taskText);
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

/**
 * Remove a task from LocalStorage.
 * @param {string} taskText - The text of the task to be removed.
 */
function removeTaskFromLocalStorage(taskText) {
    let tasks = getTasksFromLocalStorage();
    tasks = tasks.filter(task => task !== taskText);
    localStorage.setItem('tasks', JSON.stringify(tasks));
}