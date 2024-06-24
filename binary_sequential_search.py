import random
import time


def pesquisa_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def pesquisa_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def gerar_vetor(tamanho):
    return [random.randint(0, tamanho * 10) for i in range(tamanho)]


def medir_tempo(func, lista, alvo):
    inicio = time.perf_counter()
    resultado = func(lista, alvo)
    fim = time.perf_counter()
    return resultado, fim - inicio


def main():
    tamanhos = input("Digite os tamanhos dos vetores: ")
    tamanhos = [int(tamanho) for tamanho in tamanhos.split(',')]
    
    resultados = []
    for tamanho in tamanhos:
        vetor = gerar_vetor(tamanho)
        vetor.sort()
        alvo_existente = vetor[random.randint(0, tamanho-1)]
        alvo_inexistente = tamanho * 10 + 1
        
        print(f"\nVetor de tamanho {tamanho}: {vetor[:10]}...")
        print(f"Alvo existente: {alvo_existente}")
        print(f"Alvo inexistente: {alvo_inexistente}")
        
        resultado_seq_existente, tempo_seq_existente = medir_tempo(pesquisa_sequencial, vetor, alvo_existente)
        resultado_bin_existente, tempo_bin_existente = medir_tempo(pesquisa_binaria, vetor, alvo_existente)
        
        resultado_seq_inexistente, tempo_seq_inexistente = medir_tempo(pesquisa_sequencial, vetor, alvo_inexistente)
        resultado_bin_inexistente, tempo_bin_inexistente = medir_tempo(pesquisa_binaria, vetor, alvo_inexistente)
        
        resultados.append({
            'tamanho': tamanho,
            'seq_existente': tempo_seq_existente,
            'bin_existente': tempo_bin_existente,
            'seq_inexistente': tempo_seq_inexistente,
            'bin_inexistente': tempo_bin_inexistente,
        })
    
    for resultado in resultados:
        print(f"\nTamanho do vetor: {resultado['tamanho']}")
        print(f"Tempo pesquisa sequencial (existente): {resultado['seq_existente']:.10f} segundos")
        print(f"Tempo pesquisa binária (existente): {resultado['bin_existente']:.10f} segundos")
        print(f"Tempo pesquisa sequencial (inexistente): {resultado['seq_inexistente']:.10f} segundos")
        print(f"Tempo pesquisa binária (inexistente): {resultado['bin_inexistente']:.10f} segundos")


main()
