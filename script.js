// script.js
let points = 0;
let clickValue = 1;
let autoClickers = 0;

// DOM Elements
const pointsDisplay = document.getElementById('points');
const clickButton = document.getElementById('click-button');
const upgradeButton = document.getElementById('upgrade-button');
const autoClickerButton = document.getElementById('auto-clicker-button');
const clickValueDisplay = document.getElementById('click-value');
const autoClickersDisplay = document.getElementById('auto-clickers');

// Update display function
function updateDisplay() {
    pointsDisplay.textContent = `Points: ${points}`;
    clickValueDisplay.textContent = clickValue;
    autoClickersDisplay.textContent = autoClickers;
}

// Click event
clickButton.addEventListener('click', () => {
    points += clickValue;
    updateDisplay();
});

// Upgrade Click Button
upgradeButton.addEventListener('click', () => {
    if (points >= 10) {
        points -= 10;
        clickValue += 1;
        updateDisplay();
    } else {
        alert("Not enough points to upgrade!");
    }
});

// Auto Clicker Button
autoClickerButton.addEventListener('click', () => {
    if (points >= 50) {
        points -= 50;
        autoClickers += 1;
        updateDisplay();
    } else {
        alert("Not enough points to buy an auto-clicker!");
    }
});

// Auto-clicker function
function autoClicker() {
    if (autoClickers > 0) {
        points += autoClickers;
        updateDisplay();
    }
}

// Start auto-clicker interval
setInterval(autoClicker, 1000);

// Initialize display
updateDisplay();
