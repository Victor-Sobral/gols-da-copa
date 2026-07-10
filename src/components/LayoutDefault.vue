<script setup>
import CardLayout from './CardLayout.vue'

// Recebe a lista de vídeos como prop, vinda da página que usa esse layout
// Cada página (Home, SixteenFinal, EightFinal...) vai passar seu próprio JSON
const props = defineProps({
  videos: Array,
})

// Variável que guarda o texto digitado na busca
const buscarSelecao = ref('')

// Filtra os vídeos com base no texto digitado
// Usa props.videos ao invés de videos, já que agora vem de fora do componente
const videosBuscados = computed(() => {
  // Se a busca estiver vazia, retorna todos os vídeos recebidos via prop
  if (!buscarSelecao.value) {
    return props.videos
  }
  // Se tiver busca, filtra pelo título que contém o texto digitado
  return props.videos.filter((video) =>
    video.titulo.toLowerCase().includes(buscarSelecao.value.toLowerCase()),
  )
})

//Controle se o drawer esta aberto ou fehado
const drawer = ref(true)

const anuncios = [
  { imagem: '/anuncio-1.png', link: 'https://link.amazon/B0i9FOU6v' },
  { imagem: '/anuncio-2.jpeg', link: 'https://link.amazon/B02wzcIiN' },
  { imagem: '/anuncio-3.jpeg', link: 'https://link.amazon/B09vh3y4f' },
]
</script>

<template>
  <div
    style="
      height: 100vh;
      width: 100vw;
      display: flex;
      justify-content: center;
      flex-direction: column;
    "
  >
    <v-layout class="rounded rounded-md border" full-width style="height: 100vh">
      <v-app-bar style="background-color: #000000">
        <!-- Botão amburger visível só no mobile -->
        <v-app-bar-nav-icon
          style="color: #ffd700; z-index: 999; position: relative"
          @click.stop="drawer = !drawer"
        >
        </v-app-bar-nav-icon>
        <div
          style="
            position: absolute;
            left: 0;
            right: 0;
            display: flex;
            justify-content: center;
            align-items: center;
          "
        >
          <span style="color: #ffd700; font-size: 2.4rem; font-weight: bold; letter-spacing: 3px">
            G
          </span>
          <img src="/bola.gif" alt="o" style="height: 48px; width: 48px; margin: 0 -10px" />
          <span style="color: #ffd700; font-size: 2.4rem; font-weight: bold; letter-spacing: 3px">
            LS DA COPA
          </span>
        </div>
      </v-app-bar>
      <v-navigation-drawer v-model="drawer" style="background-color: #000000">
        <v-divider style="border-color: #ffd700; margin-bottom: 8px"></v-divider>
        <v-list>
          <v-list-item
            style="color: #ffd700"
            class="text-center"
            title="Fase de Grupos"
            to="/"
            link
          ></v-list-item>
          <v-list-item
            class="text-center"
            title="16 avós de final"
            to="/sixteenFinal"
            link
            style="color: #ffd700"
          ></v-list-item>
          <v-list-item
            class="text-center"
            title="Oitavas de final"
            to="/eightFinal"
            link
            style="color: #ffd700"
          ></v-list-item>
          <v-list-item
            class="text-center"
            title="Quartas de final"
            to="/fourFinal"
            link
            style="color: #ffd700"
          ></v-list-item>
          <v-list-item
            class="text-center"
            title="Semi-final"
            to="/semiFinal"
            link
            style="color: #ffd700"
          ></v-list-item>
          <v-list-item
            class="text-center"
            title="Final"
            to="/final"
            link
            style="color: #ffd700"
          ></v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-main>
        <div class="w-100 mx-auto" style="max-width: 1000px; padding: 20px; text-align: justify">
          <p class="font-weight-semibold">
            NOTAS DO DEV: O objetivo inicial do projeto era catalogar os gols da Copa do Mundo FIFA
            2026. No entanto, devido a restrições de direitos de transmissão não previstas no
            planejamento, a meta foi concluída apenas parcialmente. Ainda assim, optei por seguir em
            frente utilizando os vídeos disponíveis e livres de direitos autorais, com o intuito de
            finalizar o projeto e demonstrar minhas capacidades como desenvolvedor. Espero que quem
            passar por aqui aproveite o trabalho desenvolvido. Obrigado!
          </p>
          <p class="font-weight-white">Atualizações:</p>
          <p>10/07/2026 - Disponível primeiro jogo das quartas de final FRANÇA 2 X 0 MARROCOS.</p>
          <p>07/07/2026 - REVISADOS - Jogos até o dia 19/06.</p>
        </div>
        <div class="w-100 mx-auto" style="max-width: 1000px; padding: 20px">
          <v-text-field
            v-model="buscarSelecao"
            label="Buscar por seleção"
            placeholder="Coloque o nome da seleção que vc procura!"
            variant="outlined"
            pretend-inner-icon="mdi-magnify"
            clearable
            class="mb-6"
          />
          <!-- v-for percorre os vídeos filtrados e exibe cada um em um CardLayout -->
          <div v-for="(video, index) in videosBuscados" :key="video.id">
            <CardLayout
              :titulo="video.titulo"
              :subtitulo="video.subtitulo"
              :videoId="video.videoId"
            />
            <!-- espaço para ad / Rotação circular: garante que volta ao primeiro anuncio depois do último -->
            <div class="ad-area">
              <a
                :href="anuncios[index % 3].link"
                target="blank"
                style="width: 100%; height: 100%; display: block"
              >
                <img
                  :src="anuncios[index % 3].imagem"
                  alt="Anúncio Amazon"
                  style="width: 100%; height: 90px; object-fit: contain; display: block"
                />
              </a>
            </div>
          </div>
        </div>
      </v-main>
    </v-layout>
  </div>
</template>

<style scoped>
.ad-area {
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: lightgray;
  margin: 20px 0;
  border: 2px dashed #ccc;
  color: #666;
  font-weight: bold;
  font-size: 14px;
}
</style>
