<template>
  <div>
    <button @click="toggleDisabled">Click me</button>

    <label for="user-name-2">Enter your username</label>
    <input
      id="user-name-2"
      type="text"
      :disabled="disabled"
      v-model="username"
    />

    <p>Hello {{ username }}!</p>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'HelloWorld',
  data: () => ({
    disabled: true,
    username: '',
  }),
  methods: {
    toggleDisabled(): void {
      this.disabled = !this.disabled
    },
  },
})
</script>
