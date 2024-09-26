from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from flask import Flask, jsonify, request

# Initialize the Flask app for additional backend communication
app = Flask(__name__)

# Store user data in memory (In production, consider using a database like SQLite, PostgreSQL, or MongoDB)
users_data = {}

# Replace this with your actual Telegram bot token
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Start command - Initialize the game for the user
def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id not in users_data:
        users_data[user_id] = {"points": 0, "click_value": 1, "auto_clickers": 0}
    
    update.message.reply_text(
        f"Welcome to the Clicker Game!\nYou have {users_data[user_id]['points']} points.\n"
        f"Type /click to gain more points.\nType /shop to upgrade your clicking power."
    )

# Click command - Increases user points
def click(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id in users_data:
        user_data = users_data[user_id]
        user_data["points"] += user_data["click_value"]
        update.message.reply_text(f"You clicked! Total points: {user_data['points']}")
    else:
        update.message.reply_text("Please start the game using /start.")

# Shop command - Presents the user with options to upgrade
def shop(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Upgrade Click (+1) - 10 Points", callback_data='upgrade_click')],
        [InlineKeyboardButton("Buy Auto Clicker - 50 Points", callback_data='buy_auto_clicker')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to the shop:', reply_markup=reply_markup)

# Handles user selection in the shop
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    
    if user_id in users_data:
        user_data = users_data[user_id]
        
        if query.data == 'upgrade_click' and user_data['points'] >= 10:
            user_data['points'] -= 10
            user_data['click_value'] += 1
            query.answer("Click power upgraded!")
            query.edit_message_text(
                text=f"Upgraded! Your click value is now {user_data['click_value']}. Remaining points: {user_data['points']}"
            )
        elif query.data == 'buy_auto_clicker' and user_data['points'] >= 50:
            user_data['points'] -= 50
            user_data['auto_clickers'] += 1
            query.answer("Auto Clicker purchased!")
            query.edit_message_text(
                text=f"Bought an Auto Clicker! You now have {user_data['auto_clickers']}. Remaining points: {user_data['points']}"
            )
        else:
            query.answer("Not enough points!")

# Background auto-clicker functionality
def auto_clicker(context: CallbackContext):
    for user_id, user_data in users_data.items():
        if user_data["auto_clickers"] > 0:
            user_data["points"] += user_data["auto_clickers"]

# Flask endpoint to fetch game data (for possible integration with your HTML game)
@app.route('/game_data', methods=['GET'])
def game_data():
    user_id = request.args.get('user_id')
    if user_id and int(user_id) in users_data:
        return jsonify(users_data[int(user_id)])
    else:
        return jsonify({"error": "User not found"}), 404

# Flask endpoint to save game data from the HTML game (if needed)
@app.route('/update_points', methods=['POST'])
def update_points():
    data = request.json
    user_id = data.get('user_id')
    points = data.get('points')

    if user_id and points and int(user_id) in users_data:
        users_data[int(user_id)]['points'] = points
        return jsonify({"message": "Points updated successfully"}), 200
    return jsonify({"error": "Invalid data"}), 400

# Main function to start the bot and the Flask app
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("click", click))
    dispatcher.add_handler(CommandHandler("shop", shop))
    dispatcher.add_handler(CallbackQueryHandler(button))
    
    # Run the auto-clicker every 10 seconds
    job_queue = updater.job_queue
    job_queue.run_repeating(auto_clicker, interval=10, first=10)

    # Start the Telegram bot
    updater.start_polling()
    
    # Start the Flask app for handling backend requests
    app.run(port=5000)

if __name__ == '__main__':
    main()
