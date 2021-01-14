<template>
  <div>
    <button @click="toggleDisabled()">Click me</button>

    <input type="text" :disabled="disabled" />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'HelloWorld',
  data: () => ({
    disabled: true,
  }),
  methods: {
    toggleDisabled(): void {
      this.disabled = !this.disabled
    },
  },
})
</script>
