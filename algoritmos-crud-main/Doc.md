# Documentação do Projeto: Gerenciador de Tarefas com Custo

## Descrição Geral

Este projeto é um gerenciador de tarefas simples em Python, que permite criar, listar, buscar, atualizar e deletar tarefas. Cada tarefa possui um título, uma descrição e um custo (positivo para ganhos e negativo para perdas). O programa é executado via terminal e utiliza um menu interativo para navegação.

## Estrutura dos Arquivos

- `app.py`: Arquivo principal, responsável pela interface com o usuário e pelo fluxo do programa.
- `crud.py`: Contém as funções de manipulação (CRUD) das tarefas.

## Como Funciona o Programa

1. Ao executar o `app.py`, o usuário visualiza um menu com opções para criar, listar, buscar, atualizar ou deletar tarefas.
2. As tarefas são armazenadas em uma lista de dicionários na memória, onde cada dicionário representa uma tarefa.
3. O ID de cada tarefa corresponde ao seu índice na lista.
4. As operações CRUD são realizadas por funções no arquivo `crud.py`.

## Funções do Arquivo `crud.py`

- [Clique aqui para ver o fluxograma das funções.](./Fluxograms/README.md)

### `adicionarTarefa(tarefa: dict)`

Adiciona uma nova tarefa à lista de tarefas.

- **Parâmetros:**
  - `tarefa` (dict): Dicionário com as chaves 'titulo', 'desc', 'custo', 'data' e 'repeat'.
    - `titulo` (str): Título da tarefa.
    - `desc` (str): Descrição da tarefa.
    - `custo` (float): Valor positivo para ganhos e negativo para perdas.
    - `data` (str): Data da tarefa (formato AAAA-MM-DD).
    - `repeat` (int):
        - `-1`: Tarefa repetida todos os dias.
        - `0`: Tarefa executada apenas na data.
        - Outro valor: tarefa repetida a cada X dias a partir da data.
- **Retorno:** Nenhum.

### `buscarTarefa(buscaParametros: dict) -> list[dict]`

Busca tarefas que correspondam aos parâmetros fornecidos.

- **Parâmetros:**
  - `buscaParametros` (dict): Dicionário com os campos a serem buscados (ex: {'titulo': 'Exemplo', 'data': '2025-05-22', 'repeat': 30}).
- **Retorno:** Lista de IDs (índices) das tarefas que correspondem à busca.

### `buscarTarefaID(id: int) -> dict`

Retorna a tarefa correspondente ao ID informado.

- **Parâmetros:**
  - `id` (int): Índice da tarefa na lista.
- **Retorno:** Dicionário da tarefa ou dicionário vazio se não existir.

### `listarTarefas() -> list[dict]`

Retorna a lista completa de tarefas, cada uma contendo os campos 'titulo', 'desc', 'custo', 'data' e 'repeat'.

- **Parâmetros:** Nenhum.
- **Retorno:** Lista de dicionários das tarefas.

### `deletarTarefaID(tarefaID: int)`

Remove a tarefa do índice informado.

- **Parâmetros:**
  - `tarefaID` (int): Índice da tarefa a ser removida.
- **Retorno:** Nenhum.

### `atualizarTarefa(tarefaID: int, novaTarefa: dict)`

Atualiza a tarefa do índice informado com novos dados.

- **Parâmetros:**
  - `tarefaID` (int): Índice da tarefa a ser atualizada.
  - `novaTarefa` (dict): Dicionário com os novos dados da tarefa.
- **Retorno:** Nenhum.

## Funções do Arquivo `app.py`

### `adcionarTarefa()`

Solicita ao usuário os dados de uma nova tarefa e a adiciona à lista.

### `listarTarefas()`

Exibe todas as tarefas cadastradas.

### `buscarTarefa()`

Permite buscar tarefas por ID ou por parâmetros (título, descrição, custo, data, repeat).

### `atualizarTarefa()`

Permite atualizar os dados de uma tarefa existente, incluindo data e repeat.

### `deletarTarefa()`

Permite remover uma tarefa pelo ID.

### `imprimirMenu()`

Exibe o menu principal do programa.

## Observações

- O programa não salva as tarefas em arquivo, ou seja, ao encerrar a execução, todas as tarefas são perdidas.
- O ID das tarefas pode mudar após exclusões, pois é baseado no índice da lista.

## Exemplo de Uso

1. Execute o arquivo `app.py`.
2. Escolha uma opção do menu digitando o número correspondente.
3. Siga as instruções exibidas no terminal para cada operação.

---
