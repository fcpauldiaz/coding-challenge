<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Tweet/>
  </div>
</template>

<script>
import Tweet from './components/Tweet.vue'

export default {
  name: 'app',
  components: {
    Tweet
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
