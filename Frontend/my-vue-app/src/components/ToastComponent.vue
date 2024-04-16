<template>
  <transition name="fade">
    <div v-if="isVisible" class="toast" :style="{ backgroundColor: toastColor }">
      {{ displayMessage }}
    </div>
  </transition>
</template>

<script>
export default {
  props: ['message'],
  data() {
    return {
      isVisible: false,
      toastColor: 'black',
      displayMessage: ''
    };
  },
  methods: {
    showToast(duration = 3000, type = 'success', message) {
      this.displayMessage = message;
      this.toastColor = type === 'success' ? 'green' : 'red';
      this.isVisible = true;
      setTimeout(() => {
        this.isVisible = false;
      }, duration);
    }
  }
}
</script>

<style scoped>
.toast {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  color: white;
  padding: 10px;
  border-radius: 5px;
  animation: fade 0.5s;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */
{
  opacity: 0;
}
</style>
