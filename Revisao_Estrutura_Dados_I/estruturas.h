#ifndef ESTRUTURAS_H
#define ESTRUTURAS_H

// 1. DEFINIÇÃO DA STRUCT BASE
typedef struct {
    unsigned long id;    // Transaction ID (limpo)
    char data[11];       // Date (formato DD/MM/AAAA)
    char hora[9];        // Time (formato HH:MM:SS)
    char bandeira[20];   // Type of Card
    char categoria[30];  // Merchant Group
    float valor;         // Amount (limpo)
    int status;          // 0: Pendente, 1: Aprovada, 2: Rejeitada
    int fraud;           // Campo auxiliar para controle interno das regras
} Transacao;

// 2. DEFINIÇÕES DAS ESTRUTURAS LINEARES DINÂMICAS
typedef struct No {
    Transacao dado;
    struct No *proximo;
} No;

typedef struct {
    No *inicio;
    No *fim;
    int tamanho;
} Fila;

typedef struct {
    No *topo;
    int tamanho;
} Pilha;

typedef struct {
    No *inicio;
    int tamanho;
} Lista;

// 3. PROTÓTIPOS DO MÓDULO DE CONVERSÃO (conversor.c)
int converterCSVparaBinario(const char *arquivoCSV, const char *arquivoBinario);
void limparID(const char *idOriginal, unsigned long *idDestino);
void converterData(const char *dataOriginal, char *dataDestino);

// 4. PROTÓTIPOS DO MÓDULO DE ORDENAÇÃO (ordenacao.c)
Transacao* carregarBinarioParaVetor(const char *arquivoBinario, int *totalRegistros);
int compararPorValor(const void *a, const void *b);
int compararPorCronologia(const void *a, const void *b);

// 5. PROTÓTIPOS DAS ESTRUTURAS LINEARES (estruturas_lineares.c)
void inicializarEstruturas(Fila *f, Pilha *p, Lista *l);
void enfileirar(Fila *f, Transacao t);
void empilhar(Pilha *p, Transacao t);
int desempilhar(Pilha *p, Transacao *tRetorno);
void inserirLista(Lista *l, Transacao t);
void liberarMemoriaEstruturas(Fila *f, Pilha *p, Lista *l);

#endif