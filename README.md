<strong>Teste técnico LabTrans :vertical_traffic_light: </strong>

<strong>:wavy_dash: Sobre</strong>

Essa aplicação foi desenvolvida como requisito da segunda fase do processo seletivo do Laboratório de Transportes e Logística (LabTrans/UFSC). 
A aplicação é uma estrutura fullstack projetada para receber e manipular dados de um levantamento de uma rodovia, os quais são extraídos utilizando visão computacional.

<details>
  <summary><strong> :bulb: Tecnologias utilizadas </strong></summary><br />

  * Python
  * Peewee
  * Tornado
  * SQLite
  * Vue.js
  * Anaconda

</details>

<strong>:wavy_dash: Layout</strong>

<details>
<summary><strong> :computer: Rodando na sua máquina</strong></summary><br />

:warning: Certifique-se de ter o Python e o PIP (gerenciador de pacotes) instalados no seu computador. No meu ambiente utilizei o Python3.

Clone o repositório:
```bash
git clone https://github.com/layanenu/teste-labtrans.git
```

Entre no diretório do projeto: 
```bash
cd teste-labtrans
```

1️⃣ <strong>BACKEND</strong>

Entre no diretório do backend: 
```bash
cd backend
```

Crie um ambiente virtual para isolar as dependências da aplicação (opcional): 
```bash
python3 -m venv venv
```
ou 

```bash
python -m venv venv
```

Ative o ambiente virtual:
* macOS/Linux:
```bash
source venv/bin/activate
```
* Windows:
```bash
venv\Scripts\activate
```

Instale as dependências do projeto: 
```bash
pip install -r requirements.txt
```

2️⃣ <strong>BANCO DE DADOS</strong>

:warning: Certifique-se de ter o SQLite instalado no seu ambiente. Você pode baixá-lo em https://sqlite.org/download.html.

:eight_spoked_asterisk: <strong>Primeira opção</strong>

Para executar o banco de dados existente utilize o seguinte comando: 
```bash
sqlite3 base.db < init.sql
```

:eight_spoked_asterisk: <strong>Segunda opção</strong>

* Instale o `DB Browser for SQLite`. Você pode baixá-lo em https://sqlitebrowser.org/.
* Clique em `Open Database`
* Procure a pasta do repositório clonado e abre o arquivo `base.db`
* Execute a query existente no arquivo `init.sql` que está contido na pasta `backend`

Após a configuração do banco execute o Backend:
```bash
python3 index.py
```
ou
```bash
python index.py
```

3️⃣: <strong>FRONTEND</strong>

Após a conclusão da etapas etapas anteriores, abra um novo terminal e navegue para o diretório backend:
```bash
cd backend
```

Entre na pasta views:
```bash
cd views
```

Entre na pasta frontend
```bash
cd frontend
```

Instale as dependências do projeto:
```bash
npm install
```

Execute a aplicação:
```bash
npm run dev
```

A aplicação pode ser acessada no seu navegador através do link:
```bash
http://127.0.0.1:5173/
```

</details>
