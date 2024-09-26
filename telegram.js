

    <script>
    document.addEventListener('DOMContentLoaded', () => {
        // Initialize the Telegram Web App
        const tg = window.Telegram.WebApp;
        tg.ready();
        tg.expand(); // Expand the Web App to the full screen

        // Initial game setup
        let points = 0;
        let points = parseInt(localStorage.getItem('points')) || 0;
        // Update points display
        const updatePointsDisplay = () => {
            document.getElementById('points').innerText = `Points: ${points}`;
        };

        // Button click handler
        document.getElementById('click-button').addEventListener('click', () => {
            points++;
            updatePointsDisplay();
            localStorage.setItem('points', points);

        });

        // Send points back to Telegram when clicking the "Send Points" button
        document.getElementById('send-points').addEventListener('click', () => {
            tg.sendData(JSON.stringify({ points })); // Send points as JSON to the bot
            alert("Points sent to Telegram!");
        });

        // Receive data from Telegram Web App (if needed)
        tg.onEvent('mainButtonClicked', () => {
            tg.sendData(JSON.stringify({ points }));
        });

        // Show Main Button on Telegram UI
        tg.MainButton.text = "Send Points";
        tg.MainButton.show();
        window.Telegram.WebApp.ready();
    
    </script>
