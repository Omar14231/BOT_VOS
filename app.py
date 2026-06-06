from flask import Flask, request
import threading
import bot as discord_bot

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    username = data.get('username')
    is_near = data.get('is_near')
    discord_bot.bot.loop.create_task(discord_bot.update_member_state(username, is_near))
    return "Success", 200

if __name__ == "__main__":
    # تشغيل البوت والسيرفر معاً
    threading.Thread(target=lambda: discord_bot.bot.run(os.environ.get('DISCORD_TOKEN'))).start()
    app.run(host='0.0.0.0', port=10000)
