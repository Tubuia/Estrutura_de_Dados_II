//O algoritimo organiza um arquivo CSV com dados baseado na estrutura especificada no "estruturas.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "estruturas.h"

// Aloca memória e carrega todos os registros do arquivo .dat para um vetor
Transacao* carregarBinarioParaVetor(const char *arquivoBinario, int *totalRegistros) {
    FILE *bin = fopen(arquivoBinario, "rb");
    if (!bin) {
        printf("Erro ao abrir o arquivo binario para leitura.\n");
        *totalRegistros = 0;
        return NULL;
    }

    // Descobre o tamanho do arquivo para saber quantos registros existem
    fseek(bin, 0, SEEK_END);
    long tamanhoArquivo = ftell(bin);
    rewind(bin);

    *totalRegistros = tamanhoArquivo / sizeof(Transacao);

    // Aloca memória dinamicamente para o vetor completo (Regra dos 20% da nota)
    Transacao *vetor = (Transacao*) malloc((*totalRegistros) * sizeof(Transacao));
    if (!vetor) {
        printf("Erro de memoria ao alocar o vetor de transacoes.\n");
        fclose(bin);
        return NULL;
    }

    // Lê todos os registros de uma vez só para a memória (Alta Performance)
    fread(vetor, sizeof(Transacao), *totalRegistros, bin);
    fclose(bin);
    
    return vetor;
}

// Critério 1: Por Valor (Ordem Decrescente)
int compararPorValor(const void *a, const void *b) {
    Transacao *tA = (Transacao *)a;
    Transacao *tB = (Transacao *)b;
    
    if (tB->valor > tA->valor) return 1;
    if (tB->valor < tA->valor) return -1;
    return 0;
}

// Critério 2: Por Cronologia (Data + Hora - Ordem Crescente)
int compararPorCronologia(const void *a, const void *b) {
    Transacao *tA = (Transacao *)a;
    Transacao *tB = (Transacao *)b;
    
    char cronoA[23], cronoB[23];
    
    // Transforma "DD/MM/AAAA" + "HH:MM:SS" em "AAAAMMDDHHMMSS" para ordenação perfeita via strcmp
    // tA -> Posições na string: data[6..9] é o Ano, data[3..4] é o Mês, data[0..1] é o Dia
    sprintf(cronoA, "%.4s%.2s%.2s%.8s", tA->data + 6, tA->data + 3, tA->data, tA->hora);
    // tB
    sprintf(cronoB, "%.4s%.2s%.2s%.8s", tB->data + 6, tB->data + 3, tB->data, tB->hora);
    
    return strcmp(cronoA, cronoB);
}
