const {
  makeWASocket,
  useMultiFileAuthState,
  DisconnectReason,
  downloadMediaMessage,
  fetchLatestBaileysVersion
} = require('@whiskeysockets/baileys');

const express = require('express');
const fs = require('fs');
const path = require('path');
const mime = require('mime-types');
const axios = require('axios');
const qrcode = require('qrcode-terminal');
const FormData = require('form-data');

const app = express();
app.use(express.json());

const PORT = 3000;

// Altere a base da API externa aqui
const API_BASE = 'https://sua-api.com/upload';

let sock;

async function startSock() {
  const { version } = await fetchLatestBaileysVersion();
  const { state, saveCreds } = await useMultiFileAuthState('session');

  sock = makeWASocket({
    version,
    auth: state,
    printQRInTerminal: false
  });

  sock.ev.on('creds.update', saveCreds);

  sock.ev.on('connection.update', (update) => {
    const { connection, lastDisconnect, qr } = update;

    if (qr) {
      console.log('\n🔐 Escaneie o QR code abaixo com o WhatsApp:');
      qrcode.generate(qr, { small: true });
    }

    if (connection === 'close') {
      const shouldReconnect = lastDisconnect?.error?.output?.statusCode !== DisconnectReason.loggedOut;
      if (shouldReconnect) startSock();
    } else if (connection === 'open') {
      console.log('✅ Conectado ao WhatsApp!');
    }
  });

  sock.ev.on('messages.upsert', async ({ messages, type }) => {
    if (type !== 'notify') return;

    for (const msg of messages) {
      const from = msg.key.remoteJid;

      if (!from.endsWith('@g.us') || !msg.message?.imageMessage) continue;

      try {
        const buffer = await downloadMediaMessage(msg, 'buffer', {}, { logger: sock.logger });
        const extension = mime.extension(msg.message.imageMessage.mimetype);
        const filename = `${Date.now()}.${extension}`;
        const filepath = path.join(__dirname, 'downloads', filename);
        fs.writeFileSync(filepath, buffer);

        console.log(`📸 Imagem recebida do grupo ${from}: ${filename}`);

        // Envia imagem binária com groupId na URL
        await enviarImagemParaAPI(from, buffer, filename);
      } catch (err) {
        console.error('❌ Erro ao processar imagem:', err);
      }
    }
  });
}

// Envia imagem como multipart/form-data com groupId na URL
async function enviarImagemParaAPI(groupId, imageBuffer, filename) {
  const form = new FormData();
  form.append('file', imageBuffer, filename);

  const url = `${API_BASE}?groupId=${encodeURIComponent(groupId)}`;
  console.log(groupId);

  try {
    const response = await axios.post(url, form, {
      headers: form.getHeaders()
    });

    console.log(`🚀 Imagem enviada para API com sucesso! (${response.status})`);
  } catch (err) {
    console.error('❌ Erro ao enviar imagem para API:', err.message);
  }
}

// Rota para enviar mensagens de texto para grupos
app.post('/send', async (req, res) => {
  const { groupId, message } = req.body;

  if (!groupId || !message) {
    return res.status(400).json({ error: 'groupId e message são obrigatórios.' });
  }

  try {
    await sock.sendMessage(groupId, { text: message });
    console.log(`📤 Mensagem enviada para ${groupId}`);
    res.json({ success: true });
  } catch (err) {
    console.error('❌ Erro ao enviar mensagem:', err);
    res.status(500).json({ error: 'Falha ao enviar mensagem.' });
  }
});

app.listen(PORT, () => {
  console.log(`🌐 Servidor rodando: http://localhost:${PORT}`);
  startSock();
});
