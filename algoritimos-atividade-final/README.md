# Algoritmos - Atividade Final

- Aluno: Kauã Felipe Martins
- Professor: Anderson Paulo Avila Santos
- Curso: Ciência de Dados e IA
- Data: 21/07/2025

---

## Relátorio e detalhes

Estruturei cada código dos exercícios de forma organizada, começando pela leitura das entradas, seguido pelo processamento dos dados conforme o enunciado, e finalizando com a saída formatada. Em cada exercício, separei claramente as etapas de entrada, lógica e saída, facilitando a compreensão e manutenção do código.

No último exercício, utilizei uma matriz de soma de prefixo bidimensional para otimizar o cálculo de somas em submatrizes. Para implementar essa solução, precisei pesquisar e entender melhor como funciona a soma de prefixo em duas dimensões, garantindo que o acesso às somas fosse eficiente e correto. Essa abordagem demonstra minha preocupação com desempenho e domínio de técnicas avançadas de programação.

# Enunciados

## 1. Roleta da Sorte

Simule uma roleta que sorteia prêmios únicos (por ID), girando conforme a força aplicada. Se cair em prêmio já sorteado, gira novamente com força reduzida até encontrar um prêmio não sorteado.

**Entradas**
- n: quantidade de prêmios
- n linhas: cada uma com `ID Nome` do prêmio
- k: quantidade de sorteios (k ≤ n)
- k números: forças aplicadas em cada giro

**Saída**
- IDs e nomes dos prêmios sorteados, formato `ID-Nome`, separados por espaço.
- Ou: `"Não foi possível realizar o sorteio"`

**Exemplo**
Entrada
```
5
101 Carro
102 Viagem
103 Celular
104 Notebook
105 Relógio
3
3 5 2
```
Saída
```
103-Celular 102-Viagem 104-Notebook
```

---

## 2. Organizando Agenda da Semana

Otimize uma agenda semanal de 5 dias úteis, cada um com 10 horários. Permite adicionar ou remover atividades.

**Entradas**
- 5 linhas: atividades de cada dia (10 horários por linha)
- n: número de alterações
- n linhas: cada uma com `Remover Dia Início Fim` ou `Adicionar Atividade Duração`

**Saída**
- Agenda atualizada após as alterações
- Mensagem se não for possível alocar atividade

**Exemplo**
Entrada
```
Aula Aula Aula Aula Almoço Almoço Livre Reunião Livre Livre
Livre Livre Livre Livre Almoço Almoço Monitoria Monitoria Aula Aula
Aula Aula Aula Aula Almoço Almoço Livre Livre Reunião Livre
Livre Livre Reunião Reunião Almoço Almoço Livre Livre Aula Aula
Monitoria Monitoria Estudo Estudo Almoço Almoço Livre Livre Livre Livre
4
Remover Quarta 8 10
Remover Sexta 16 17
Adicionar Reunião 3
Adicionar Monitoria 5
```
Saída
```
Não foi possível alocar a atividade Monitoria
Horário Segunda Terça Quarta Quinta Sexta
8-9 Aula Reunião Livre Livre Monitoria
9-10 Aula Reunião Livre Livre Monitoria
10-11 Aula Reunião Aula Reunião Estudo
11-12 Aula Livre Aula Reunião Estudo
12-13 Almoço Almoço Almoço Almoço Almoço
13-14 Almoço Almoço Almoço Almoço Almoço
14-15 Livre Monitoria Livre Livre Livre
15-16 Reunião Monitoria Livre Livre Livre
16-17 Livre Aula Reunião Aula Livre
17-18 Livre Aula Livre Aula Livre
```

---

## 3. Agência de Marketing

Selecione influenciadores para campanhas publicitárias, maximizando o alcance e respeitando o orçamento, usando três estratégias.

**Entradas**
- C: orçamento máximo
- N: quantidade de influenciadores
- N linhas: custo, seguido de lista de seguidores separados por vírgula

**Saída**
- Para cada estratégia: custo total e número de seguidores alcançados

**Exemplo**
Entrada
```
200
5
90,5,6,7,8,9,10,11,12,13,14
50,1,2
70,3,4,5,6,7,8,9,10,11,12
80,4,5,6,7,8,9,10,11,12,13,18
60,2,3,4,5,6,7,8,9,10,11,15,20
```
Saída
```
Estratégia Ingênua: 180.0, 14
Estratégia Atual: 180.0, 14
Estratégia Nova: 190.0, 16
```

---

## 4. A Grande Caçada aos Tesouros Perdidos

Encontre o maior número de tesouros ("X") em uma área retangular do mapa, com perímetro máximo P.

**Entradas**
- M N: linhas e colunas do mapa
- M linhas: cada uma com N caracteres ('.' ou 'X')
- P: perímetro máximo permitido

**Saída**
- Número máximo de tesouros capturados

**Exemplo**
Entrada
```
3 5
X . X . X
. X . X .
X . X . X
6
```
Saída
```
1
```