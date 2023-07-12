<template>
  <div class="container">

    <div class="cabecalho">
      <h4>
          Os seguintes arquivos contêm informações sobre os itens
          (buraco, remendo, trinca, placa, drenagem), agrupados por quilometragem e rodovia.
      </h4>
    </div>

    <div class="full-download">
      <label>Baixe o arquivo CSV completo
        <button class="button-download" @click="onClickFullDownload()">Download</button>
      </label>
    </div>

    <div class="download-by-highway">
      <label>Baixe o arquivo CSV por rodovia
        <input type="number" placeholder="Digite o nº da rodovia" @change="handleChange">
      </label>
      <button class="button-download" @click="onClickByHighway()">Download</button>
    </div>

    <div class="cabecalho-indicence">
      <h4>
          Este campo permite consultar qual quilômetro possui maior incidência de determinado item
      </h4>
    </div>

    <div class="download-higher-incidence-km">
      <label>Digite o item pelo qual deseja filtrar
        <select @change="handleChangeItem">
          <option value="buraco">Buraco</option>
          <option value="remendo">Remendo</option>
          <option value="trinca">Trinca</option>
          <option value="placa">Placa</option>
          <option value="drenagem">Drenagem</option>
        </select>
      </label>
      <button class="button-download" @click="onClickHigherIncidence()">Pesquisar</button>
    </div>

    <div v-if="mostItem">
      O quilômetro {{ mostItem?.km }} da rodovia
      {{ mostItem?.highway }} registra a maior incidência de
      {{ item }}, com um total de
      {{ mostItem[item] }} ocorrências.
    </div>

    <div class="container-links">
      <router-link to="/">
        <button class="back-to-home">Voltar para a página inicial</button>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'DownloadContent',
  data() {
    return {
      options: [],
      highway: '',
      item: 'buraco',
      mostItem: null,
    };
  },
  methods: {
    onClickFullDownload() {
      axios({
        url: 'http://localhost:8882/result/report',
        method: 'GET',
        responseType: 'blob',
      }).then((response) => {
        const fileUrl = window.URL.createObjectURL(new Blob([response.data]));
        const fileLink = document.createElement('a');
        fileLink.href = fileUrl;
        fileLink.setAttribute('download', 'dados.csv');
        document.body.appendChild(fileLink);

        fileLink.click();
      });
    },

    handleChange(event) {
      this.highway = event.target.value;
    },

    handleChangeItem(event) {
      console.log(event.target.value);
      this.item = event.target.value;
    },

    onClickHigherIncidence() {
      console.log(this.item);
      if (this.item && this.item !== '') {
        axios({
          url: `http://localhost:8882/result/item?item=${this.item}`,
          method: 'GET',
        }).then((response) => {
          if (response?.data) {
            this.mostItem = response.data;
          }
        });
      }
    },

    onClickByHighway() {
      if (this.highway && this.highway !== '') {
        axios({
          url: `http://localhost:8882/result/report?highway=${this.highway}`,
          method: 'GET',
          responseType: 'blob',
        }).then((response) => {
          const fileUrl = window.URL.createObjectURL(new Blob([response.data]));
          const fileLink = document.createElement('a');
          fileLink.href = fileUrl;
          fileLink.setAttribute('download', `dados_${this.highway}.csv`);
          document.body.appendChild(fileLink);

          fileLink.click();
        });
      }
    },
  },
};
</script>

<style scoped>

  h4 {
    font-size: 20px;
  }

  button{
    transition: 0.2s opacity;
  }

  button:hover {
    opacity: 0.8;
  }

  input{
    /* background-color: aqua; */
    width: 150px;
    height: 25px;
  }

  select {
    width: 150px;
    height: 25px;
  }
  .container {
    background-color: white;
    display: block;
    justify-content: center;
    width: 1000px;
    height: 400px;
    /* background-color: violet; */
    padding: 20px 20px 20px 20px;
  }

  .cabecalho{
    /* background-color: aqua; */
    padding-bottom: 20px;
  }

  .full-download{
    padding-bottom: 20px;
    /* align-items: center; */
    /* justify-content: flex-start; */
    /* display: flex; */
    font-size: 20px;
    /* background-color: yellow; */
  }

  .button-download {
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

  .download-by-highway{
    /* padding: 20px 0px 20px 20px; */
    /* align-items: center; */
    /* justify-content: flex-start; */
    /* display: flex; */
    font-size: 20px;
    /* background-color: burlywood; */
    padding-bottom: 20px;

  }

  .cabecalho-indicence{
    /* background-color: chocolate; */
    padding-bottom: 20px;

  }

  .download-higher-incidence-km{
    /* background-color: cadetblue; */
    font-size: 20px;

  }

  .container-links{
    justify-content: flex-end;
    display: flex;
    /* padding-right: 20px; */
    /* background-color: yellowgreen; */
  }
  .back-to-home{
    background-color: #E5E5E5;
    width: 150px;
    height: 50px;
    font-size: 15px;
    border-radius: 10px;
    border: 0;
  }

</style>
