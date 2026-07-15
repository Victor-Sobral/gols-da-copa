<script setup>
defineProps({
  titulo: String,
  subtitulo: String,
  videoId: String,
  bloqueado: Boolean,
})
</script>

<template>
  <v-card class="mx-auto" max-width="1200" style="background-color: #bdbdbd">
    <v-layout>
      <v-main>
        <v-container>
          <v-row density="comfortable">
            <v-col cols="12">
              <v-card color="#385F73">
                <v-card-title class="text-headline-small"> {{ titulo }} </v-card-title>

                <v-card-subtitle> {{ subtitulo }} </v-card-subtitle>
              </v-card>
            </v-col>

            <v-col cols="12">
              <v-card color="#1F7087">
                <div class="d-flex flex-no-wrap justify-space-between">
                  <!-- se video esta com bloqueado: true mostra imagem -->
                  <template v-if="bloqueado">
                    <img
                      src="/video-bloqueado.png"
                      alt="Vídel indisponível"
                      style="width: 100%; height: 400px; object-fit: cover"
                    />
                  </template>
                  <template v-else>
                    <iframe
                      width="100%"
                      height="400"
                      :src="`https://www.youtube.com/embed/${videoId}`"
                      title="YouTube video player"
                      frameborder="0"
                      allow="
                        accelerometer;
                        autoplay;
                        clipboard-write;
                        encrypted-media;
                        gyroscope;
                        picture-in-picture;
                      "
                      allowfullscreen
                    ></iframe>
                  </template>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-layout>
  </v-card>
</template>
