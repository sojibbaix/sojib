from telethon import TelegramClient, events, Button
import re
import os
import asyncio

# ==== TELEGRAM API ====
api_id = int(os.environ.get('API_ID', 24054229))
api_hash = os.environ.get('API_HASH', 'a71e93c0c3a78314c6eecf82110e58c5')

# ==== CHANNEL / GROUP SETUP ====
file_source = -1003182380938# File Channel
file_forward_to = -1003170435513     # Your Channel
otp_source = -1002833675066# OTP Group
otp_forward_to = -1003142908885      # Your OTP Group

# ==== CUSTOM LINKS ====
your_group_link = "https://t.me/tempsojib"
your_channel_link = "https://t.me/allnambar"

# Initialize client
client = TelegramClient('user_forward_session', api_id, api_hash)

print("🚀 Starting Telegram Forwarding Bot...")

# ✅ 1. FILE FORWARDING (with caption cleaned)
@client.on(events.NewMessage(chats=file_source))
async def forward_file(event):
    try:
        if event.file:
            caption = event.raw_text or ""
            # Remove unwanted links/usernames and "OTP : JOIN HERE"
            lines = caption.splitlines()
            cleaned_lines = [
                re.sub(r'(@\w+|https?://t\.me/\S+|t\.me/\S+|telegram\.me/\S+)', '', line)
                for line in lines
                if "OTP : JOIN HERE" not in line
            ]
            cleaned_caption = "\n".join(cleaned_lines).strip()
            # Replace old username with new one
            cleaned_caption = cleaned_caption.replace("@Rifat103300", "@MUNNABHAI_BD")
            
            await client.send_file(
                file_forward_to,
                file=event.media,
                caption=cleaned_caption,
                buttons=[Button.url("🔐 OTP Group Join Here", your_group_link)]
            )
            print("✅ File forwarded successfully!")
    except Exception as e:
        print(f"❌ Error in file forwarding: {e}")

# ✅ 2. OTP FORWARDING (only if contains 4-8 digit code)
@client.on(events.NewMessage(chats=otp_source))
async def forward_otp(event):
    try:
        text = event.raw_text
        # Replace old username with new one
        text = text.replace("@BANGLAHAS", "@DaRcK_SaHaNuR")
        if re.search(r'\b(\d{4,8})\b', text):
            await client.send_message(
                otp_forward_to,
                message=text,
                buttons=[Button.url("📢 Main Channel", your_channel_link)]
            )
            print("✅ OTP forwarded successfully!")
    except Exception as e:
        print(f"❌ Error in OTP forwarding: {e}")

async def main():
    await client.start()
    print("✅ Forwarding system is running...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
