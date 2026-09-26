# Tree Traversal Simulator - Red Black Tree Edition

## 📚 Sobre o Projeto

Este projeto foi desenvolvido para a disciplina de **Estruturas de Dados II**, com o objetivo de transformar um simulador de árvores binárias em uma ferramenta educacional mais completa, incorporando conceitos avançados de estruturas de dados, especialmente **Árvores Rubro-Negras (Red-Black Trees)**.

O projeto parte do simulador original **The Binary Tree Traversal Simulator**, identificado durante a atividade de engenharia reversa proposta na disciplina.

## 🎯 Objetivo

O objetivo principal é oferecer uma experiência de aprendizagem interativa para estudantes de Estruturas de Dados, permitindo visualizar e compreender:

- Árvores Binárias;
- Árvores Binárias de Busca (BST);
- Percursos em árvores;
- Conceitos de balanceamento;
- Propriedades das Árvores Rubro-Negras;
- Rotações e recolorações de nós.

A proposta foi desenvolvida como uma evolução do simulador original, que possuía limitações pedagógicas identificadas durante a análise do grupo.

---

## 🕹️ Sobre o Jogo

O simulador permite a criação visual de árvores através de uma interface gráfica onde o jogador pode posicionar nós e estabelecer suas conexões.

O modelo original foi desenvolvido em C++ e possibilita:

- Inserção de nós identificados por letras;
- Conexão de nós filhos à esquerda e à direita;
- Visualização gráfica da árvore;
- Execução de diferentes percursos de travessia.

![EMBEDDEDIMAGE](https://github.com/user-attachments/assets/2a4ebd18-909a-4adb-a9e0-475571cbac0a) 

---

## 🔍 Problemas Identificados

Durante o estudo do simulador original foram observadas algumas limitações importantes:

### Ausência de explicações teóricas

O simulador demonstra visualmente os algoritmos de travessia, porém não apresenta explicações detalhadas sobre os conceitos envolvidos.

### Falta de balanceamento

A aplicação não verifica se a árvore construída segue propriedades de ordenação ou balanceamento, limitando seu potencial pedagógico.

### Outras limitações observadas

- Entrada irrestrita do usuário;
- Ausência de condição de vitória;
- Ausência de condição de derrota;
- Falta de treinamento guiado;
- Pouca imersão sonora;
- Ausência de explicações sobre os conceitos explorados.

---

## 🚀 Melhorias Propostas

O projeto propõe evoluir o simulador com:

### ✅ Implementação de Árvore Rubro-Negra

A estrutura escolhida para o upgrade foi a **Árvore Rubro-Negra**, baseada em:

- Nós vermelhos e pretos;
- Altura preta;
- Rotações;
- Recoloração automática;
- Balanceamento eficiente.

### ✅ Validação de BST

Os nós passam a possuir uma relação de ordem baseada nas letras utilizadas.

Exemplo:

```text
A < B < C < D < ...****
```

# ▶️ Guia de Execução do Jogo

## 1. Download do Projeto

Faça o download do arquivo compactado disponibilizado a partir do repositório GitHub.

Exemplo:

```text
cpp-data-structures-binary-tree-traversal-simulator.zip
```

Após o download, extraia o conteúdo do arquivo para um diretório de sua preferência.

---

## 2. Abrir a Pasta Principal

Após a extração, será criada a seguinte pasta:

```text
cpp-data-structures-binary-tree-traversal-simulator
```

Ao acessá-la, serão exibidos os seguintes arquivos e diretórios:

```text
cpp-data-structures-binary-tree-traversal-simulator
│
├── .git
├── docs
├── start
├── LICENSE
└── README.md
```

---

## 3. Acessar a Pasta Start

Abra a pasta:

```text
start
```

Dentro dela estará disponível a pasta principal do projeto:

```text
start
│
└── TreeProject
```

---

## 4. Acessar a Pasta TreeProject

Abra a pasta:

```text
TreeProject
```

Você encontrará a seguinte estrutura:

```text
TreeProject
│
├── 3rdParty
├── bin
├── TreeProject
└── TreeProject.sln
```

---

## 5. Acessar a Pasta Bin

Abra a pasta:

```text
bin
```

Nesta pasta encontram-se os recursos necessários para a execução da aplicação, incluindo bibliotecas, arquivos de suporte, assets e o executável principal.

Exemplo:

```text
bin
│
├── assets
├── freetype.dll
├── glew32.dll
├── libFLAC-8.dll
├── libmodplug-1.dll
├── libmpg123-0.dll
├── libogg-0.dll
├── libopus-0.dll
├── libopusfile-0.dll
├── libvorbis-0.dll
├── libvorbisfile-3.dll
├── SDL2.dll
├── SDL2_mixer.dll
├── TreeProject.pdb
├── TreeProjectd.exe
└── TreeProjectd.pdb
```

---

## 6. Executar o Simulador

Localize o executável principal:

```text
TreeProjectd.exe
```

ou, dependendo da versão distribuída:

```text
TreeProjectCD.exe
```

Execute o arquivo clicando duas vezes sobre ele.

Após a execução, o simulador será iniciado automaticamente.

---

## ⚠️ Observações Importantes

- Não mova o arquivo executável para outra pasta.
- Não exclua a pasta `assets`.
- Não remova os arquivos `.dll`.
- Mantenha toda a estrutura original da pasta `bin`.

O executável depende desses arquivos para carregar corretamente os recursos gráficos, bibliotecas de áudio e elementos do jogo.

---

## ✅ Resumo Rápido

```text
1. Baixar o ZIP do projeto

2. Extrair o conteúdo

3. Abrir:
   cpp-data-structures-binary-tree-traversal-simulator

4. Entrar em:
   start

5. Entrar em:
   TreeProject

6. Entrar em:
   bin

7. Executar:
   TreeProjectd.exe
   ou
   TreeProjectCD.exe

8. Utilizar o simulador
```

Após a execução do arquivo `.exe`, o simulador será iniciado e estará pronto para o estudo interativo de Árvores Binárias e Árvores Binárias de Busca (BST).

---

## 👥 Equipe e Créditos

**Disciplina:** Estruturas de Dados II — Ciência da Computação 

* **Esdras Abdir Issacar da Silva Oliveira**
* **Arthur Canton Souza de Paula**
* **João Lucas Ataide de Melo**
* **Douglas Patriota Lopes**

---

# 👤 Autor do projeto original
Athanasios Gourdomichalis - https://github.com/AthanasiosGourdomichalis
