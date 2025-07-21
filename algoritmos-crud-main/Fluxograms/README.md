# Fluxogramas do programa

## Observação

Todos fluxogramas serão das funções encontradas no arquivo [crud.py](../crud.py).
O arquivo [app.py](../app.py) contém somente instruções de prints e inputs. Algumas de suas funções chamam as funções de `crud.py` para manipular as tarefas, mas essas funções não manipulam elas por si mesmas. São mais detalhes de controle do loop do programa e visualização das informações.

### Variável `tarefas`

- É uma lista de dicionários que contém cada informação das tarefas. Ela se econtra definida no topo do código.

```mermaid
flowchart TD
    A(["Início"]) --> B["tarefas = list[dict]"] --> C(["Fim"])
```

### adicionarTarefa(tarefa: dict)

```mermaid
flowchart TD
    A(["Início"]) --> Input@{shape: manual-input, label: "tarefa (dict)"}
    Input --> B["tarefas.append(tarefa) (obs: append adiciona ao final da lista)"]
    B --> C(["Fim"])
```

### buscarTarefa(buscaParametros: dict)

```mermaid
flowchart TD
    A(["Início"]) --> Input@{shape: manual-input, label: "buscaParametros (dict)"}
    Input --> B["indices = []"]
    B --> C["i = 0"]
    C --> D@{shape: hexagon, label: "i < len(tarefas)\n  (obs: len retorna o tamanho da lista)"}
    D -- Sim --> E["tarefa = tarefas[i]"]
    E --> F{"Para toda chave e valor de buscaParametros, tarefa[chave] == valor de buscaParametro?"}
    F -- Sim --> G["indices.append(i) (obs: append adiciona ao final da lista)"]
    F -- Não --> I
    G --> I["i = i + 1"]
    D -- Não --> J{"indices está vazio?"}
    J -- Não --> K["return indices"]
    J -- Sim --> L["return [] (lista vazia)"]
    K --> M(["Fim"])
    L --> M
```

### buscarTarefaID(id: int)

```mermaid
flowchart TD
    A(["Início"]) --> Input@{shape: manual-input, label: "id (int)"}
    Input --> B{"id > len(tarefas) (obs: len retorna o tamanho da lista)"}
    B -- Sim --> C["return []"]
    B -- Não --> D["return tarefas[id]"]
    C --> E(["Fim"])
    D --> E
```

### listarTarefas()

```mermaid
flowchart TD
    A(["Início"]) --> B["return tarefas"]
    B --> C(["Fim"])
```

### deletarTarefaID(tarefaID: int)

```mermaid
flowchart TD
    A(["Início"]) --> Input@{shape: manual-input, label: "tarefaID (int)"}
    Input --> B["tarefas.pop(tarefaID) (obs: pop remove pelo índice)"]
    B --> C(["Fim"])
```

### atualizarTarefa(tarefaID: int, novaTarefa: dict)

```mermaid
flowchart TD
    A(["Início"]) --> Input1@{shape: manual-input, label: "tarefaID (int)"}
    Input1 --> Input2@{shape: manual-input, label: "novaTarefa (dict)"}
    Input2 --> B["tarefas[tarefaID] = novaTarefa"]
    B --> C(["Fim"])
```
