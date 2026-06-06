import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

user_map = {
    "waled10991": 1420884699869614140,
    "hhjjkkllpppp098": 1306034100544737461,
    "Aakrv62": 1477040012951289916,
    "iihhx24": 1506731132794830889
}

async def update_member_state(username, is_near):
    guild = bot.get_guild(1512647340803096706)
    if not guild: return
    uid = user_map.get(username)
    member = guild.get_member(uid)
    if member and member.voice:
        await member.edit(mute=not is_near, deafen=not is_near)

# تشغيل البوت باستخدام المفتاح (DISCORD_TOKEN) الموجود في Render
if __name__ == "__main__":
    bot.run(os.environ.get('DISCORD_TOKEN'))
