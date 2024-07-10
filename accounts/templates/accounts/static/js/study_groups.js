document.addEventListener('DOMContentLoaded', function() {
    const generateLinkBtn = document.getElementById('generate-link-btn');
    const copyLinkBtn = document.getElementById('copy-link-btn');
    const invitationLinkInput = document.getElementById('invitation-link');

    generateLinkBtn.addEventListener('click', function() {
        // Here you can generate the link dynamically
        // For demonstration purposes, let's generate a dummy link
        const groupLink = generateGroupLink(); // Replace with your actual link generation logic

        // Display the generated link in the input field
        invitationLinkInput.value = groupLink;
    });

    copyLinkBtn.addEventListener('click', function() {
        // Copy the link when the Copy Link button is clicked
        invitationLinkInput.select();
        document.execCommand('copy');
        alert('Link copied to clipboard!');
    });

    function generateGroupLink() {
        // Replace with your actual logic to generate the invitation link
        // For example, you can generate a unique link based on the group ID or any other criteria
        return 'https://example.com/group-invitation'; // Dummy link for demonstration
    }
});
