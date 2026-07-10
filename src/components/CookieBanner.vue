<script setup>
/* Controla se o banner esta visível*/
const mostrarBanner = ref(false)

/*Ao carregar a página, verifica se o usuário já aceitou os cookies*/
onMounted(() => {
  const cookiesAceitos = localStorage.getItem('cookiesAceitos')
  if (!cookiesAceitos) {
    mostrarBanner.value = true
  }
})

/*Se o usúario aceitar, salvar no localStorage e esconde o banner*/
const aceitarCookies = () => {
  localStorage.setItem('cookiesAceitos', 'true')
  mostrarBanner.value = false
}
</script>

<template>
  <div v-if="mostrarBanner" class="cookie-banner">
    <p>
      🍪 Usamos cookies para melhorar sua experiência e exibir anúncios relevantes. Ao continuar
      navegando, você concorda com nossa política de privacidade.
    </p>
    <button @click="aceitarCookies" class="cookie-btn">Aceitar e continuar</button>
  </div>
</template>

<style scoped>
.cookie-banner {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: #1a1a1a;
  color: #ffffff;
  padding: 16px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  z-index: 9999;
  border-top: 2px solid #ffd700;
}

.cookie-banner p {
  margin: 0;
  font-size: 0.9rem;
  flex: 1;
}

.cookie-btn {
  background-color: #ffd700;
  color: #000000;
  border: none;
  padding: 10px 20px;
  font-weight: bold;
  border-radius: 4px;
  cursor: pointer;
  white-space: nowrap;
}

.cookie-btn:hover {
  background-color: #e6c200;
}
</style>
