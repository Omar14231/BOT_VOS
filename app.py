from flask import Flask, request
import threading
import bot as discord_bot
import asyncio

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    username = data.get('username')
    is_near = data.get('is_near')
    
    # تنفيذ الأمر
    discord_bot.bot.loop.create_task(discord_bot.update_member_state(username, is_near))
    return "Success", 200

def run_bot():
    discord_bot.bot.run('YOUR_BOT_TOKEN_HERE')

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=10000)

