# Reflexao
qual o problema que queremos resolver
Quem quer fazer o que e com o que ?
Quem quer fazer o que e com o que ?


## Pilar Poo
1. crie entidades === Abstração
2. Não preciso saber como funciona  === Encapsulamento
3. rerança
4. poliformismo


## Antes de começar a desenvolver:

1. Clone o repositório

- `git clone https://github.com/tryber/sd-010-b-tech-news.git`.
- Entre na pasta do repositório que você acabou de clonar:
  - `sd-010-b-tech-news`

2. Crie o ambiente virtual para o projeto

- `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências

- `python3 -m pip install -r dev-requirements.txt`

4. Crie uma branch a partir da branch `main`

- Verifique que você está na branch `main`
  - Exemplo: `git branch`
- Se não estiver, mude para a branch `main`
  - Exemplo: `git checkout main`
- Agora crie uma branch à qual você vai submeter os `commits` do seu projeto
  - Você deve criar uma branch no seguinte formato: `nome-github-nome-do-projeto`
  - Exemplo: `git checkout -b exemplo-tech-news`

5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

- Verifique que as mudanças ainda não estão no _stage_
  - Exemplo: `git status` (deve aparecer listada a pasta _exemplo_ em vermelho)
- Adicione o novo arquivo ao _stage_ do Git
  - Exemplo:
    - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
    - `git status` (deve aparecer listado o arquivo _exemplo/README.md_ em verde)
- Faça o `commit` inicial
  - Exemplo:
    - `git commit -m 'iniciando o projeto tech-news'` (fazendo o primeiro commit)
    - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

6. Adicione a sua branch com o novo `commit` ao repositório remoto

- Usando o exemplo anterior: `git push -u origin exemplo-project-name`

7. Crie um novo `Pull Request` _(PR)_



Os quatro pilares em uma frase
Na Programação Orientada a Objetos, você deve criar entidades ( Abstração ) com as mensagens que escuta bem definidas ( Encapsulamento ), podendo especializar comportamentos de entidades ( Herança ) contanto que garanta que a forma de enviar mensagens é consistente ( Polimorfismo )