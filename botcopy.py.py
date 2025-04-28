
from telethon import TelegramClient, events

# Suas credenciais
api_id = 24060062
api_hash = '91f380f5c8fa3586729b24e76a66d667'

# Nome do arquivo de sessão
session_name = 'meu_usuario'

# Cria o cliente
client = TelegramClient(session_name, api_id, api_hash)

# IDs
grupo_origem = -1002691858749  # ID do grupo de origem (ajustar se necessário)
grupo_destino = -1002126433918  # ID do grupo de destino

@client.on(events.NewMessage(chats=grupo_origem))
async def handler(event):
    texto = event.message.message

    # Substituir links
    texto = texto.replace('https://', 'https://stke.me/l/436/761 ')

    # Envia para o grupo de destino
    await client.send_message(grupo_destino, texto)

async def main():
    print("Bot rodando...")
    await client.run_until_disconnected()

# Executa
client.start()
client.loop.run_until_complete(main())
