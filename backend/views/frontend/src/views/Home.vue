<template>
  <div>
    <router-link to="/upload">
      <button>Upload CSV</button>
    </router-link>
    <router-link to="/download">
      <button>Download CSV</button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'HomeContent',
};
</script>

<style scoped>
  div{
    background-color: white;
    display: flex;
    justify-content: center;
    width: 700px;
    height: 200px;
    align-items: center;
  }

  button{
    margin: 0 10px;
    width: 200px;
    height: 50px;
    font-size: 20px;
    background-color: #759E0A;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    border: 0;
    transition: 0.2s opacity;
  }

  button:hover {
    opacity: 0.8;
  }

</style>
