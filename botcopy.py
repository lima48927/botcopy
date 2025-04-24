
from telethon.sync import TelegramClient, events
import re

# Dados do bot
api_id = SUA_API_ID
api_hash = 'SUA_API_HASH'
bot_username = 'lima48927'  # Seu bot
grupo_origem = -2691858749
grupo_destino = -2126433918
link_customizado = "https://stke.me/l/436/761"

# Conecta ao cliente do Telegram (usando o usuário do bot)
client = TelegramClient(bot_username, api_id, api_hash)

# Função para substituir todos os links
def substituir_links(texto):
    return re.sub(r'https?://\S+', link_customizado, texto)

@client.on(events.NewMessage(chats=grupo_origem))
async def copiar_mensagem(event):
    if event.message.message:
        nova_mensagem = substituir_links(event.message.message)
        await client.send_message(grupo_destino, nova_mensagem)

# Inicia o bot
print("Bot rodando...")
client.start()
client.run_until_disconnected()
