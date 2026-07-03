# ⚽ Gols da Copa 2026

Site desenvolvido para exibir os melhores gols da Copa do Mundo 2026, organizados por fase do torneio.

## 🌐 Sobre o Projeto

O **Gols da Copa** nasceu da ideia de reunir em um só lugar os gols mais marcantes da Copa do Mundo 2026, permitindo que o usuário navegue facilmente entre as fases do torneio e assista aos melhores momentos diretamente pelo YouTube.

## 🚀 Funcionalidades

- Exibição de vídeos do YouTube organizados por fase
- Navegação entre fases: Grupos, 16 avos, Oitavas, Quartas, Semifinal e Final
- Busca por seleção em tempo real
- Layout responsivo com menu lateral
- Espaços reservados para anúncios

## 🛠️ Tecnologias Utilizadas

### Frontend

- **Vue 3** — framework principal com Composition API e `<script setup>`
- **Vuetify 3** — biblioteca de componentes UI
- **Vue Router** — navegação entre páginas

### Backend / Automação

- **Python** — script de automação para busca de vídeos
- **yt-dlp** — biblioteca para busca de vídeos no YouTube
- **JSON** — armazenamento dos dados dos vídeos

### Deploy

- **GitHub** — versionamento do código
- **Netlify** — hospedagem do site

## 📁 Estrutura do Projeto

gols-da-copa/
├── public/
│ ├── bola.gif # Animação da bola no navbar
│ └── favicon.png # Ícone da aba
├── src/
│ ├── components/
│ │ ├── LayoutDefault.vue # Layout principal com navbar e menu
│ │ └── CardLayout.vue # Card de exibição de cada vídeo
│ ├── pages/
│ │ ├── HomePage.vue
│ │ ├── SixteenFinal.vue
│ │ ├── EightFinal.vue
│ │ ├── FourFinal.vue
│ │ ├── SemiFinal.vue
│ │ └── Final.vue
│ ├── data/
│ │ ├── videos.json # Vídeos da fase de grupos
│ │ ├── videosSixteen.json # Vídeos dos 16 avos
│ │ ├── videosEightFinal.json # Vídeos das oitavas
│ │ ├── videosFourFinal.json # Vídeos das quartas
│ │ ├── videosSemiFinal.json # Vídeos da semifinal
│ │ └── videosFinal.json # Vídeos da final
│ └── router/
│ └── index.js # Configuração das rotas
├── scripts/
│ └── buscar_videos.py # Script Python de automação
└── index.html # Metadados e SEO

## 🤖 Script de Automação

O script `buscar_videos.py` busca automaticamente vídeos no YouTube usando hashtags relacionadas à Copa do Mundo e salva os resultados em `videos.json`. Ele foi desenvolvido com as seguintes funcionalidades:

- Busca por hashtags configuráveis
- Evita duplicatas verificando o `videoId` antes de salvar
- Preserva os vídeos já existentes no JSON, adicionando apenas os novos
- Contador de IDs incremental para novos vídeos

## ▶️ Como Rodar o Projeto

### Site

```bash
npm install
npm run dev
```

### Script de busca de vídeos

```bash
pip install yt-dlp
python scripts/buscar_videos.py
```

## 👨‍💻 Author

https://github.com/Victor-Sobral
https://www.linkedin.com/in/victor-sobral-871b76199/
