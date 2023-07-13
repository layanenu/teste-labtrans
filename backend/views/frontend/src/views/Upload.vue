<template>
  <div class="container">

    <div class="container-file-input">
      <label for="file-upload" class="file-input">Clique no botão abaixo para escolher um arquivo
        <input id="file-upload" type="file" accept=".csv" name="arquivo" @change="onFileSelected">
      </label>
      <button class="button-upload" @click="onUpload">Upload</button>

    </div>

    <div class="container-links">
      <p v-if="uploadSuccess" class="success-message">Criado com sucesso!</p>
      <p v-if="uploadError" class="error-message">Erro ao fazer o upload: {{ uploadError }}</p>
      <router-link to="/download">
        <button class="go-download">Ir para a página de download</button>
      </router-link>
      <router-link to="/">
        <button class="back-to-home">Voltar para a página inicial</button>
      </router-link>

    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UploadContent',
  data() {
    return {
      selectedFile: null,
      uploadSuccess: false,
      uploadError: null,
    };
  },
  methods: {
    onFileSelected(event) {
      const [file] = event.target.files;
      this.selectedFile = file;
    },
    onUpload() {
      if (this.selectedFile) {
        const fd = new FormData();
        fd.append('file', this.selectedFile, this.selectedFile.name);
        axios.post('http://localhost:8882/result', fd)
          .then((res) => {
            console.log(res);
            this.uploadSuccess = true;
            this.selectedFile = null;
            const fileInput = document.getElementById('file-upload');
            fileInput.value = '';
          }).catch((error) => {
            this.uploadError = error.message;
            this.selectedFile = null;
            const fileInput = document.getElementById('file-upload');
            fileInput.value = '';
            // Define a mensagem de erro
          });
      }
    },
  },
};
</script>

<style scoped>
  .container {
    background-color: white;
    display: block;
    justify-content: center;
    width: 700px;
    height: 200px;
  }

  .error-message{
    margin-top: 20px;
    color: red;
    font-weight: bold;
    display: block;
    width: 70%;
    padding-left: 30px;
  }
  .success-message{
    margin-top: 20px;
    color: #759E0A;
    font-weight: bold;
    display: block;
    width: 70%;
    padding-left: 30px;
  }
  .button-upload {
    margin: 0 10px;
    width: 150px;
    height: 40px;
    font-size: 20px;
    background-color: #759E0A;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    border: 0;
  }

  button{
    transition: 0.2s opacity;
  }

  button:hover {
    opacity: 0.8;
  }

  .container-file-input{
    padding: 50px 30px 40px 30px;
    align-items: center;
    justify-content: center;
    display: flex;
    /* background-color: black; */
  }

  #file-upload{
    font-size: 20px;
  }

  .container-links{
    justify-content: flex-end;
    display: flex;
    padding-right: 20px;
  }

  .back-to-home{
    background-color: #E5E5E5;
    margin: 0 5px;
    width: 150px;
    height: 50px;
    font-size: 15px;
    border-radius: 10px;
    border: 0;
  }

  .go-download{
    background-color: #E5E5E5;
    margin: 0 5px;
    width: 150px;
    height: 50px;
    font-size: 15px;
    border-radius: 10px;
    border: 0;
  }

</style>
