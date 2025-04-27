from telethon.sync import TelegramClient, events
import re

# Dados do seu app do Telegram
api_id = 24060062
api_hash = '91f380f5c8fa3586729b24e76a66d667'

# Dados do bot
bot_token = '8049772298:AAEZtGExb1DLcxUkjeUmIRLx7pq49if1tTU'
bot_username = 'lima48927'

# IDs dos grupos
grupo_origem = -2691858749
grupo_destino = -2126433918

# Link que vai substituir
link_customizado = 'https://stke.me/l/436/761'

# Cria o cliente para a conta pessoal
user_client = TelegramClient('user_session', api_id, api_hash)

# Cria o cliente para o bot
bot_client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# Função para substituir todos os links
def substituir_links(texto):
    return re.sub(r'https?://\S+', link_customizado, texto)

# Quando uma nova mensagem chegar no grupo de origem
@user_client.on(events.NewMessage(chats=[grupo_origem]))
async def copiar_mensagem(event):
    if event.message.message:
        nova_mensagem = substituir_links(event.message.message)
        await bot_client.send_message(grupo_destino, nova_mensagem)

# Inicia os dois clientes
async def main():
    await user_client.start()
    print("Bot rodando...")
    await user_client.run_until_disconnected()

import asyncio
asyncio.run(main())
