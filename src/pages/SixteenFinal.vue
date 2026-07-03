<script setup>
import LayoutDefault from '@/components/LayoutDefault.vue'
// Importa o JSON específico dos jogos das oitavas de final
import videos from '@/data/videosSixteen.json'
</script>

<template>
  <main>
    <!-- Passa a lista de vídeos como prop para o LayoutDefault -->
    <LayoutDefault :videos="videos" />
  </main>
</template>
