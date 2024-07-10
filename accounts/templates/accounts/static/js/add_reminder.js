// add_reminder.js

document.addEventListener("DOMContentLoaded", function() {
    const addReminderForm = document.getElementById("add-reminder-form");

    addReminderForm.addEventListener("submit", function(event) {
        event.preventDefault();
        
        // Simulated data submission (replace with actual handling logic)
        const title = document.getElementById("reminder-title").value;
        const date = document.getElementById("reminder-date").value;
        const time = document.getElementById("reminder-time").value;
        const description = document.getElementById("reminder-description").value;
        const importance = document.getElementById("reminder-importance").value;

        console.log("Submitted Reminder:");
        console.log("Title:", title);
        console.log("Date:", date);
        console.log("Time:", time);
        console.log("Description:", description);
        console.log("Importance:", importance);

        // Reset form fields (optional)
        addReminderForm.reset();
    });
});
