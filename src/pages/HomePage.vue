<script setup>
import LayoutDefault from '@/components/LayoutDefault.vue'
// Importa o JSON da fase de grupos para passar ao LayoutDefault
import videos from '@/data/videos.json'
</script>

<template>
  <main>
    <!-- Passa a lista de vídeos como prop para o LayoutDefault -->
    <LayoutDefault :videos="videos" />
  </main>
</template>
