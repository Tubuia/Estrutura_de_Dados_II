# Caderno do Estudante
# Projeto ConectaUDF: redes sociais com grafos
**Disciplina:** Algoritmos / Matemática Discreta / Ciência de Dados

## 1. O desafio
Você faz parte da equipe que analisa a rede social fictícia **ConectaUDF**. Sua missão é representar as amizades em um grafo, realizar cálculos e usar Python para interpretar a estrutura da rede.

## 2. Conceitos essenciais
- **Vértice (ou nó):** representa um usuário.
- **Aresta:** representa uma amizade entre dois usuários.
- **Grau:** quantidade de conexões diretas de um usuário.
- **Caminho:** sequência de usuários em que cada par consecutivo está conectado.
- **Densidade:** proporção entre as amizades existentes e todas as amizades possíveis.

Neste projeto, a amizade é recíproca. Portanto, usamos um **grafo não direcionado**.

## 3. Conheça os usuários
| Código | Usuário |
|---|---|
| A | Ana |
| B | Bruno |
| C | Carla |
| D | Diego |
| E | Elisa |
| F | Felipe |
| G | Arthur |
| H | João |
| I | Esdraz |
| J | Douglas |

As amizades são:
1. Ana — Bruno
2. Ana — Carla
3. Bruno — Carla
4. Bruno — Diego
5. Carla — Elisa
6. Diego — Elisa
7. Diego — Felipe
8. Elisa — Felipe

## 4. Passo a passo: desenhe o grafo
1. Desenhe seis círculos, um para cada usuário.
2. Escreva o nome de cada pessoa dentro do círculo.
3. Para cada amizade da lista, desenhe uma linha entre os dois usuários.
4. Não desenhe duas linhas para a mesma amizade.
5. Confira se todas as oito amizades aparecem.

![Grafo](https://graphonline.top/tmp/saved/ib/ibFVUYpGRZorgINH.png)

## 5. Passo a passo: calcule o grau
Conte quantas linhas chegam a cada círculo. Registre o resultado.

| Usuário | Amigos diretos | Grau |
|---|---|---:|
| Ana | 4 | 4 |
| Bruno | 4 | 4 |
| Carla | 4 | 4 |
| Diego | 4 | 4 |
| Elisa | 4 | 4 |
| Felipe | 3 | 3 |
| Arthur | 6 | 6 |
| João | 5 | 5 |
| Esdraz | 4 | 4 |
| Douglas | 4 | 4 |

**Pergunta 1:** quem tem mais conexões diretas?  
**Resposta:** Arthur

## 6. Passo a passo: calcule o número de amizades
Some todos os graus. Como cada amizade conecta dois usuários, cada aresta é contada duas vezes.

**Fórmula:**  
`Número de arestas = soma dos graus ÷ 2`

1. Soma dos graus: 42
2. Divida por 2: 42 ÷ 2 = 21
3. Quantas amizades existem no grafo? 21

## 7. Passo a passo: calcule a densidade
A densidade compara as amizades existentes com o total de amizades possíveis.

Para um grafo simples não direcionado:

`D = 2 × E / (V × (V − 1))`

Em que:
- `D` = densidade;
- `E` = número de arestas;
- `V` = número de vértices.

Substitua os valores:
`D = 2 × 21 / (10 × (10 − 1))`

Resultado decimal: 2,14  
Resultado percentual: 214 %

**Interprete:** a rede tem poucas ou muitas das conexões possíveis? Explique com suas palavras.

**Resposta:** A rede tem muitas conexões, já que ela tem o dobro de conexões do que o numero de usuarios

## 8. Passo a passo: represente o grafo em Python
A lista de adjacência registra, para cada usuário, os nomes de seus amigos. Digite o código em Python (por exemplo, no Google Colab ou em outro ambiente disponível).

```python
rede = {
    "Ana": ["Bruno", "Carla",'Arthur', 'Douglas'],
    "Bruno": ["Ana", "Carla", "Diego",'Arthur'],
    "Carla": ["Ana", "Bruno", "Elisa",'Arthur'],
    "Diego": ["Bruno", "Elisa", "Felipe", 'João'],
    "Elisa": ["Carla", "Diego", "Felipe", 'João'],
    "Felipe": ["Diego", "Elisa", 'Esdras'],
    'Arthur': ['Ana', 'Bruno', 'Carla', 'João', 'Esdras', 'Douglas'],
    'João': ['Arthur', 'Diego', 'Elisa', 'Esdras', 'Douglas'],
    'Esdras': ['Arthur', 'João', 'Felipe', 'Douglas'],
    'Douglas': ['João', 'Ana', 'Esdras', 'Arthur']
}

# Quantidade de usuarios
n = len(rede)

# Calcule o grau de cada usuario
for usuario, amigos in rede.items():
    print(usuario, "tem", len(amigos), "conexoes")

# A soma dos graus conta cada amizade duas vezes
soma_graus = sum(len(amigos) for amigos in rede.values())
arestas = soma_graus // 2

print("Total de usuarios:", n)
print("Total de amizades:", arestas)

# Densidade do grafo
densidade = (2 * arestas) / (n * (n - 1))
print(f"Densidade: {densidade:.2%}")
```

### Saída do Código Executado: https://github.com/Tubuia/Estrutura_de_Dados_II/blob/main/Grafo/Grafo_Analise_Rede_Social.ipynb  
```
Ana tem 4 conexoes
Bruno tem 4 conexoes
Carla tem 4 conexoes
Diego tem 4 conexoes
Elisa tem 4 conexoes
Felipe tem 3 conexoes
Arthur tem 6 conexoes
João tem 5 conexoes
Esdras tem 4 conexoes
Douglas tem 4 conexoes
Total de usuarios: 10
Total de amizades: 21
Densidade: 46.67%
```

### Entenda o código
1. `rede` guarda os usuários e suas listas de amigos.
2. `len(rede)` conta os usuários.
3. `len(amigos)` calcula o grau de cada usuário.
4. `sum(...)` soma os graus.
5. `// 2` divide a soma por dois para contar cada amizade uma única vez.
6. A fórmula final calcula a densidade.

## 9. Passo a passo: encontre um caminho
Encontre um caminho de Ana até Felipe. Cada passagem por uma linha corresponde a uma aresta.

Exemplo de registro:
`Ana → Bruno → Diego → Felipe`

- Quantas arestas há no caminho?
- Você encontrou outro caminho com a mesma quantidade de arestas? Qual?

**Resposta:**  
1 - há 3 arestas no caminho  
2 - Sim. Ana → Arthur → Esdraz → Felipe  

## 10. Desafio em grupo
Amplie a rede social:
1. Adicione pelo menos quatro usuários fictícios.
2. Crie no mínimo cinco novas amizades.
3. Atualize a lista de adjacência no Python.
4. Recalcule os graus, o total de arestas e a densidade.
5. Compare a densidade antes e depois da ampliação.
6. Identifique os usuários com mais conexões.
7. Explique como a rede poderia recomendar uma nova amizade.

## 11. Entrega
Entregue:
- desenho do grafo;
- tabela com os graus;
- cálculos de arestas e densidade;
- código Python executável;
- respostas às perguntas e breve conclusão.

## 12. Pergunta de reflexão
Duas pessoas ainda não são amigas, mas têm três amigos em comum. Como essa informação poderia ser usada para sugerir uma nova conexão? Quais cuidados de privacidade devem ser considerados ao analisar redes sociais?  

**Resposta:**  
Três amigos em comum podem indicar que as duas provavelmente pessoas frequentam os mesmos círculos. A rede pode contar os vizinhos compartilhados de cada par e sugerir as conexões com contagem mais alta. Esse princípio é chamado de fechamento triádico ("amigos de amigos").

Cuidados de privacidade ao analisar redes sociais:

- Pedir consentimento e ser transparente sobre o uso dos dados de conexões.
- Evitar sugestões que exponham relações sensíveis.
- Permitir que o usuário opte por não aparecer como sugestão.
- Minimizar e anonimizar os dados nas análises, respeitando leis como a LGPD.

## 13. Conclusão

Representar a rede social ConectaUDF como grafo permitiu medir a rede com poucas fórmulas: o grau mostra quem é mais conectado, a soma dos graus dividida por 2 dá o número de amizades, e a densidade indica quanto da rede possível já existe. A contagem de amigos em comum é uma forma simples e eficaz de recomendar amizades, desde que acompanhada de cuidados com a privacidade.
