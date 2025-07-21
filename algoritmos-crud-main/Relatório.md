# Relatório do desenvolvimento

## Escolha do tema

- Gerenciador de Tarefas com Custos: Um tema simples e fácil de ser implementado em um CRUD. Mas que de certa forma seria útil se implementado em uma aplicação mais desenvolvida.

## Desenvolvimento

- Separação em dois arquivos:
    - Um arquivo contendo as funções do CRUD que alteram diretamente os dados, contendo a lista tarefas, uma lista de dict. Cada dict de tarefas corresponde a uma tarefa e seus atributos.
    - Outro arquivo responsável pela visualização do usuário e também os inputs manuais.

- crud.py:  
    - Contém todas as funções necessárias para o gerenciamento e a lista de tarefas, onde é armazenada um dicionário de cada tarefa. Tais quais: adiconar, deletar, buscar, listar e atualizar.
    - Todas funções possuem implementações simples e diretas. Por exemplo, a função adicionarTarefa simplesmente faz um tarefas.append(tarefa), que, em outras palavras, adicionar um elemento tarefa, um dict, na lista tarefas
    - Os ID são os próprio indices de cada elemento em tarefa. Futuramente ou em uma aplicação mais dedicada, o ID podeiria se tornar um atributo direto de cada tarefa.

- app.py:
    - Arquivo que contém a parte de iteração com o usuário.
    - Contém apenas funções (sendo algumas até de mesmo nome que as do arquivo crud) nas quais interagem e mostram informações ao usuário. Ou seja, é um conjunto de prints e inputs que imprimem textos na tela e captura dados digitados.
    - Cada função de gerenciamento, chama a função correspondente no arquivo crud.py.

- Desafios e soluções:  
    Em geral não se teve muitas dificuldades e problemas durante o desenvolvimento.

    - buscarTarefa(buscaParametro: dict): Essa função simplesmente pega cada valor de cada chave de buscaParametro e compara com cada valor da correspondente chave de cada dict na lista de tarefas.  
        ```python
        [i for i, val in enumerate(tarefas) if all(val.get(k) == v for k, v in buscaParametros.items())]
        ```
        - Esse list comprehension faz o que se era desejado. Obviamente, não foi obtido esse resultado rapidamente, mas sim, desenvolvido por partes. 
        - Anteriormente foi separado em fors e ifs para iterar sobre cada chave e valor de buscaParametro e compara-las em outra iteração de cada chave e valor de um dict, que por sua vez está dentro de tarefas que também está sendo iterada para obter cada dict. Então compara-se se todos as chaves e seus valores, de buscaParametros, são iguais às correspondentes chaves e seus valores nas dicts de tarefas. Se sim, guardar o indice do dict em tarefas. Caso contrário, continuar.
        - Após entender o que cada for está fazendo e as comparações sendo realizadas, pode-se então tentar escrever eles em uma list comprehension. O problmea era a parte da comparção de todos os valores e não de apenas um. Foi onde então, obteve-se conhecimento da função all(). Ele retorna True se todos valores de um valor iterável for verdade. Ou seja, foi colocado outro list compehension dentro da função all() e funcionou.

## Considerações e conclusões

- Existem muitos pontos em que o programa pode melhorar. Como verificação dos dados, autenticação, melhoria da visualização de dados (como em repeat, que não transforma o -1 para "todos os dias"), implementar de fato uma verificação da data e adicionar lembretes, remoção automática de tarefas não repetitivas e com data antigas, ente diversos outras funcionalidades que podem ser adicionadas.  
- Obvío que como um modelo inicial em um simples terminal, não seria viável somente continuar seguindo em frente com o desenvolvimento. Seria necessário realizar um salvamento de dados, talvez em um banco de dados, bem como implementar uma interface gráfica direcionada para este tipo de aplicação.  
- Em geral, o programa cumpre com sua função e dá uma visão de como seria uma aplicação baseada em um gerenciamento de tarefas com custos. 