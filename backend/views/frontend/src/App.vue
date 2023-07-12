<template>
  <div>
    <Logo />
    <router-view/>
  </div>

</template>

<script>
import './styles/global.css';
import Logo from './components/Logo.vue';

export default {
  name: 'App',
  components: {
    Logo,
  },
};
</script>
