# 📱 Como abrir o site Dudota Doces no tablet Android

## 📦 O que você recebeu

Um arquivo ZIP chamado **`dudota_pwa.zip`** com todo o site.

---

## ⚠️ IMPORTANTE

**NÃO abra o `index.html` diretamente!** As fotos dos produtos não aparecerão.

Você precisa usar um **servidor HTTP** (é mais fácil do que parece!).

---

## ✅ Passo a passo

### 1. Extraia o ZIP

- No tablet, use o app **"Arquivos"** (Files) do Google ou **"RAR"**
- Toque no `dudota_pwa.zip`
- Extraia para uma pasta (ex: `Download/dudota_pwa/`)

### 2. Instale um app servidor

Vá na **Play Store** e instale um destes apps (todos gratuitos):

| App | Link da Play Store |
|-----|-------------------|
| **Simple HTTP Server** | https://play.google.com/store/apps/details?id=com.tristanwiley.simplehttpserver |
| **Web Server** | https://play.google.com/store/apps/details?id=com.borbely.android_web_server |
| **KSWEB** | https://play.google.com/store/apps/details?id=ru.kslabs.ksweb |

> 💡 Recomendamos o **"Simple HTTP Server"** — é o mais fácil de usar.

### 3. Configure o servidor

1. Abra o app **Simple HTTP Server**
2. Toque em **"Select folder"** (Selecionar pasta)
3. Navegue até a pasta `dudota_pwa/` que você extraiu
4. Toque em **"Start"** (Iniciar)
5. O app mostrará um endereço como: `http://192.168.1.10:8080`

### 4. Abra no navegador

1. Abra o **Chrome** no tablet
2. Digite o endereço que o app mostrou (ex: `http://192.168.1.10:8080`)
3. Pronto! O site aparecerá com todas as fotos!

---

## 🚀 Instalar como app (opcional)

Depois que o site abrir no Chrome:
1. Toque no menu (⋮) no canto superior direito
2. Selecione **"Adicionar à tela inicial"**
3. O ícone da Dudota Doces aparecerá na tela inicial do tablet
4. Da próxima vez, abra direto pelo ícone — funciona offline!

---

## ❓ Problemas?

**As fotos não aparecem?**
→ Certifique-se de que selecionou a pasta `dudota_pwa/` (não a pasta `assets/` dentro dela).

**O app não inicia?**
→ Tente outro app da lista acima. O **KSWEB** funciona em quase todos os tablets.

**Não consigo extrair o ZIP?**
→ Instale o app **"RAR"** da Play Store — ele extrai qualquer ZIP.

---

## 📂 O que tem dentro da pasta

```
dudota_pwa/
├── index.html      ← Página principal (produtos)
├── carrinho.html   ← Carrinho de compras
├── cart.js         ← Lógica do carrinho
├── manifest.json   ← Configuração do app
├── sw.js           ← Cache offline
└── assets/         ← Fotos dos produtos e ícones
```

---

**Dudota Doces — Tradição há mais de 40 anos! 🍬**