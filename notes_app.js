// Notes Application

// Note class to create note instances
class Note {
    /**
     * Constructs a new Note.
     * @param {string} title - The title of the note.
     * @param {string} content - The content of the note.
     */
    constructor(title, content) {
        this.id = Note.generateId();
        this.title = title;
        this.content = content;
        this.createdAt = new Date();
    }

    /**
     * Generates a unique identifier for each note.
     * @returns {string} A unique ID.
     */
    static generateId() {
        return '_' + Math.random().toString(36).substr(2, 9);
    }
}

// NoteManager class to manage notes
class NoteManager {
    constructor() {
        this.notes = [];
    }

    /**
     * Adds a new note to the notes list.
     * @param {Note} note - The note to add.
     */
    addNote(note) {
        if (!(note instanceof Note)) {
            throw new Error('Invalid note object');
        }
        this.notes.push(note);
    }

    /**
     * Deletes a note by its ID.
     * @param {string} noteId - The ID of the note to delete.
     */
    deleteNote(noteId) {
        this.notes = this.notes.filter(note => note.id !== noteId);
    }

    /**
     * Finds a note by its ID.
     * @param {string} noteId - The ID of the note to find.
     * @returns {Note|null} The found note or null if not found.
     */
    findNoteById(noteId) {
        return this.notes.find(note => note.id === noteId) || null;
    }

    /**
     * Updates a note by its ID.
     * @param {string} noteId - The ID of the note to update.
     * @param {string} newTitle - The new title of the note.
     * @param {string} newContent - The new content of the note.
     */
    updateNote(noteId, newTitle, newContent) {
        const note = this.findNoteById(noteId);
        if (!note) {
            throw new Error('Note not found');
        }
        note.title = newTitle;
        note.content = newContent;
    }

    /**
     * Lists all notes.
     * @returns {Note[]} An array of notes.
     */
    listNotes() {
        return this.notes;
    }
}

// Main execution block
(function() {
    try {
        const manager = new NoteManager();

        // Create a new note
        const note1 = new Note('Meeting Notes', 'Discuss project status and next steps.');
        manager.addNote(note1);

        // Add another note
        const note2 = new Note('Shopping List', 'Eggs, Milk, Bread');
        manager.addNote(note2);

        // List all notes
        console.log('All Notes:', manager.listNotes());

        // Update a note
        manager.updateNote(note1.id, 'Updated Meeting Notes', 'Updated discussion points.');
        console.log('Note after update:', manager.findNoteById(note1.id));

        // Delete a note
        manager.deleteNote(note2.id);
        console.log('All Notes after deletion:', manager.listNotes());

    } catch (error) {
        console.error('An error occurred:', error.message);
    }
})();