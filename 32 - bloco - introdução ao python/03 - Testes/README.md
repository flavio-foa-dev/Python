# Teste em python
### o que vamos aprender
Hoje aprederemos como testar  de forma automatizada nossos programas, verificando se para determinada entrada de dados o resultado foi o esperado.

Como os erros podem acontecer, vamos testa-los tambem.
Além disso, ainda aprederemos a subistituir  componentes para facilitar teste que envolvam recursos externos.

### Você sera Capaz de:
- Escrever testes automatizados utilizando a linguagem **Python**;
- verificar a ocorrencia de erros esperados utilizando testes automatizados:
- Criar contexto para execução de testes automatizados;
- modificar compónemtes do software para evitar a utilização de recursos externos.

### Por que isso é importante?

Testes são importantes na automação do funcionamento correto de um algoritimo, com o proposito de evitar que erros se propagem ate a pessoa usuária final. È importante ressaltar que testes automatizados **não evitam bugs**, porem ajudam a previni-los.

em empresas, geralmente, quando voĉe  entrega uma tarefa, ela deve passar por testes automatizados, valiudando que o requesito foi satisfeito.
  um cçodigo sem testes e um código ruim. Não importa quão bem ele foi escrito
  .
# Testes automatizados
Quem nunca arrumou um problema  em um codigo  e acabou fazendo-o deixar de funcionar para outro cenário? ou ficou horas testando as mais diversas condições para um  algoritimo e no meio do caminho teve de mexer no codigo e recomeçar tudo novamente 😁

Atraves de testes automatizados, a pessoa desenvolvedora é capaz de identificar mais facilmente um bug ou verificar que alteração do codigo do nao afetaram o comportamento esperado do sistema.

Em nosso curso utilizamos a boblioteca `pytest` um framework que facilita a escrita de testes simpoles, mas capaz de testar funcionalidades complexas em aplicação e bibliotecas

⚠️ Lembre-se de intalar a biblioteca somente no ambiente virtual do seu projeto
a instalação é feita através do `pip` utilizando co commando
`python3 -m pip install pytest`
e podemos verificar utilizando o comando:
`python3 -m pytest --version`
A saida esperada é similar a apresentada abaixo
`This is pytest version 5.3.0, imported from /home/cassiobotaro/projects/gerenciador-tarefas/.venv/lib/python3.8/site-packages/pytest.py`

📝 Que tal vermos um exemplo?
codigo.py

```
def is_odd(number):
    'Retorna True se um número é ímpar, senão False.'
    return number % 2 != 0
```
  test_codigo.py

```
from codigo import is_odd


def test_is_odd_when_number_is_odd_returns_true():
    'Para um número ímpar a função deve retornar o valor True'
    assert is_odd(3) is True


def test_is_odd_when_number_is_even_returns_false():
    'Para um número par a função deve retornar o valor False'
    assert is_odd(2) is False
```

Notem que o nome do arquivo de testes possui o prefixo `test__`, assim como a definição das funções de testes. isto é necessario para que seus testes sejam descobertos pela ferramenta.

Uma função de testes é similar a qualquer outra, porem tem o proposito de verificar se o resultado obitido foi o mesmo do esperado. No codigo isto pode ser visto atraves da utilização da palavra reservada `assert`.

O comando `assert`. funciona da seguinte maneira: caso a expressão recebida seja verdadeira(avaliada como true), nada acontec, porém caso seja falsa(avaliada como falsa),uma exceção do tipo`AssertionError` e lançada. A `pytest` captur O ERRO e tentaapresentar uma comparação entre o esperado e o recebido da melhor maneira possivel.
Vamos rodar nossos testes e ver o resultado? Vamos utilizar o comando:

```
python3 -m pytest
```
  💡Experimente modificar estes testes para uma falha e veja o resultado.