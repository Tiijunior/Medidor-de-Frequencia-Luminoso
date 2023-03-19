# Medidor de Frequência Luminoso
 Projeto efetuado na faculdade na matéria de processamento digital de sinais, onde utilizando a Transformada de Fourier, para a conversão de áudio analógico em sinal digital, com isso os leds acende de acordo com a frequência e a sua amplitude

Projeto
O sinal é captado pelo microfone e armazenada na memória para processamento posterior. Dois parâmetros são relevantes:
A taxa de amostragem ou frequência de amostragem (fs) do sistema de medição (por exemplo, 48 kHz). Número médio de amostras obtidas num segundo (amostras por segundo).
O número selecionado de amostras; o comprimento de bloco (BL). Esta é sempre uma potência inteira para a base 2 na FFT (por exemplo, 2^10 = 1024 amostras)
A partir dos dois parâmetros básicos fs e BL, podem ser determinados outros parâmetros da medição.
Largura de banda fn (= frequência Nyquist). Este valor indica a frequência máxima teórica que pode ser determinada pela FFT.
fn = fs / 2
Por exemplo, a uma taxa de amostragem de 48 kHz, os componentes de frequência até 24 kHz podem ser teoricamente determinados. No caso de um sistema analógico, o valor praticamente alcançável está geralmente um pouco abaixo disso, devido a filtros analógicos - por exemplo, a 20 kHz.
Duração da medição D. A duração da medição é dada pela taxa de amostragem fs e pelo comprimento de bloco BL.
D = BL / fs.
A fs = 48 kHz e BL = 1024, isto rende 1024/48000 Hz = 21.33 ms
Resolução de frequência df. A resolução de frequência indica o espaçamento de frequência entre dois resultados de medição.
df = fs / BL
A fs = 48 kHz e BL = 1024, isto dá um df de 48000 Hz / 1024 = 46,88 Hz.

Na prática, a frequência de amostragem fs é geralmente uma variável dada pelo sistema. No entanto, ao selecionar o comprimento de bloco BL, a duração da medição e a resolução de frequência podem ser definidas. Aplica-se o seguinte:
Um pequeno comprimento de bloco resulta em rápidas repetições de medição com uma resolução de frequência grosseira.
Um grande comprimento de bloco resulta em repetições de medição mais lentas com resolução de frequência fina.





