from telethon.sync import TelegramClient, events
import re

# Dados do bot
api_id = 24060062
api_hash = '91f380f5c8fa3586729b24e76a66d667'
bot_token = '8049772298:AAEZtGExb1DLcxUkjeUmIRLx7pq49if1tTU'
bot_username = 'lima48927'

# IDs dos grupos
grupo_origem = -2691858749
grupo_destino = -2126433918

# Link que vai substituir
link_customizado = 'https://stke.me/l/436/761'

# Conecta o bot
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Função para substituir todos os links
def substituir_links(texto):
    return re.sub(r'https?://\S+', link_customizado, texto)

# Evento de nova mensagem no grupo de origem
@client.on(events.NewMessage(chats=[grupo_origem]))
async def copiar_mensagem(event):
    if event.message.message:
        nova_mensagem = substituir_links(event.message.message)
        await client.send_message(grupo_destino, nova_mensagem)

# Inicia o bot
print("Bot rodando...")
client.run_until_disconnected()
