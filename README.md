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
git clone git@github.com:layanenu/trybe-futebol-clube.git
```

Entre no diretório do projeto: 
```bash
cd trybe-futebol-clube
```
  
Entre no diretório app:
```bash
cd app
```
  
Suba a orquestração de containers:
```bash
docker-compose up --build -d
```
  
A aplicação poderá ser acessada através de: <br />
<br />
Front-end: 
```bash
localhost:3000
```

Back-end: 
```bash
localhost:3001
```
  
Credenciais para o login: <br />
<br />
Login: 
```bash
admin@admin.com
```
Senha: 
```bash
secret_admin
```
</details>

REQUISITOS

Fluxo 1: Teams (Times)
1 - Desenvolva em /app/backend/src/database nas pastas correspondentes, uma migration e um model para a tabela de times
2 - (TDD) Desenvolva testes que cubram no mínimo 5 por cento dos arquivos em /app/backend/src, com um mínimo de 7 linhas cobertas
3 - Desenvolva o endpoint /teams no back-end de forma que ele possa retornar todos os times corretamente
4 - (TDD) Desenvolva testes que cubram no mínimo 10 por cento dos arquivos em /app/backend/src, com um mínimo de 19 linhas cobertas
5 - Desenvolva o endpoint /teams/:id no back-end de forma que ele possa retornar dados de um time específico

Fluxo 2: Users e Login (Pessoas Usuárias e Credenciais de acesso)
6 - Desenvolva em /app/backend/src/database nas pastas correspondentes, uma migration e um model para a tabela de pessoas usuárias
7 - (TDD) Desenvolva testes que cubram no mínimo 15 por cento dos arquivos em /app/backend/src, com um mínimo de 25 linhas cobertas
8 - Desenvolva o endpoint /login no back-end de maneira que ele permita o acesso com dados válidos no front-end
9 - (TDD) Desenvolva testes que cubram no mínimo 20 por cento dos arquivos em /app/backend/src, com um mínimo de 35 linhas cobertas
10 - Desenvolva o endpoint /login no back-end de maneira que ele não permita o acesso com um email não cadastrado ou senha incorreta no front-end
11 - (TDD) Desenvolva testes que cubram no mínimo 30 por cento dos arquivos em /app/backend/src, com um mínimo de 45 linhas cobertas
12 - Desenvolva um middleware de validação para o token, verificando se ele é válido, e desenvolva o endpoint /login/role no back-end de maneira que ele retorne os dados corretamente no front-end

Fluxo 3: Matches (Partidas)
13 - Desenvolva em /app/backend/src/database nas pastas correspondentes, uma migration e um model para a tabela de partidas
14 - (TDD) Desenvolva testes que cubram no mínimo 45 por cento dos arquivos em /app/backend/src, com um mínimo de 70 linhas cobertas
15 - Desenvolva o endpoint /matches de forma que os dados apareçam corretamente na tela de partidas no front-end
16 - Desenvolva o endpoint /matches de forma que seja possível filtrar somente as partidas em andamento, e também filtrar somente as partidas finalizadas, na tela de partidas do front-end
17 - Desenvolva o endpoint /matches/:id/finish de modo que seja possível finalizar uma partida no banco de dados
18 - Desenvolva o endpoint /matches/:id de forma que seja possível atualizar partidas em andamento
19 - (TDD) Desenvolva testes que cubram no mínimo 60 por cento dos arquivos em /app/backend/src, com um mínimo de 80 linhas cobertas
20 - Desenvolva o endpoint /matches de modo que seja possível cadastrar uma nova partida em andamento no banco de dados
21 - Desenvolva o endpoint /matches de forma que não seja possível inserir uma partida com times iguais nem com um time que não existe na tabela de times

Fluxo 4: Leaderboards (Placares)
