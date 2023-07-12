<template>
  <div>
    <a href="/"><img alt="logo-labtrans" id="logo" src="../assets/logo-labtrans.png"></a>
  </div>
</template>

<script>
export default {
  name: 'LogoContent',
};
</script>

<style scoped>
  div{
    background-color: white;
    width: 100%;
    height: 100px;
    align-items: center;
    display: flex;
    justify-content: center;
    padding-top: 30px;
  }

  #logo{
    width: 300px;
  }
</style>
