<script>
    
document.addEventListener('DOMContentLoaded', () => {
    // Initialize the Telegram Web App
    const tg = window.Telegram.WebApp;
    tg.ready();
    tg.expand(); // Expand the Web App to the full screen

    // Initial game setup
    let points = parseInt(localStorage.getItem('points')) || 0; // Get points from local storage

    // Update points display
    const updatePointsDisplay = () => {
        document.getElementById('points').innerText = `Points: ${points}`;
    };

    // Button click handler
    document.getElementById('click-button').addEventListener('click', (event) => {
        points++;
        updatePointsDisplay();
        showFloatingNumber(1, event.clientX, event.clientY); // Show floating number with coordinates
        localStorage.setItem('points', points);
    });

    // Function to show the floating number
    function showFloatingNumber(amount, mouseX, mouseY) {
        const floatingNumber = document.getElementById('floating-number');
        floatingNumber.innerText = `+${amount}`; // Set the text to show the amount
        floatingNumber.style.display = 'block'; // Make the floating number visible

         // Log the mouse coordinates
    console.log(`Floating number shown at (${mouseX}, ${mouseY})`);
        // Position it based on the mouse click coordinates
        floatingNumber.style.left = `${mouseX}px`; // Position it based on mouse X coordinate
        floatingNumber.style.top = `${mouseY - 30}px`; // Position it above the click point

        // Apply animation
        floatingNumber.style.transform = 'translateY(-20px)'; // Move it up
        floatingNumber.style.opacity = '0'; // Fade out

        // Reset the animation after it's done
        setTimeout(() => {
            floatingNumber.style.display = 'none'; // Hide it after the animation
            floatingNumber.style.transform = 'translateY(0)'; // Reset position
            floatingNumber.style.opacity = '1'; // Reset opacity
        }, 500); // Match this duration with the CSS transition duration
    }

    // Load points display on page load
    updatePointsDisplay();
});
</script>
