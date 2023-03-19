# declaração das bibliotecas:

import matplotlib.pyplot as plt  # Responsável pelo biblioteca gráfica estatístico
import numpy as np  # Responsável pelos cálculos da FFT
import pyaudio as pa  # Responsável por captar o som da placa de som ou microfone.
import struct  # Utilizado para enviar pacotes via serial
import serial  # Responsável pela comunicação serial
import time  # Responsável pelo cálculo do tempo.


# Funções que irá enviar a amplitude para o Arduino.
def acender_leds1(frequencia):
    if 50 < frequencia <= 500:
        arduino.write(struct.pack('>B', 1))
    elif 500 < frequencia <= 800:
        arduino.write(struct.pack('>B', 2))
    elif 800 < frequencia <= 1000:
        arduino.write(struct.pack('>B', 3))
    elif 1000 < frequencia <= 1150:
        arduino.write(struct.pack('>B', 4))
    elif 1150 < frequencia <= 1200:
        arduino.write(struct.pack('>B', 5))
    elif 1200 < frequencia <= 1300:
        arduino.write(struct.pack('>B', 6))
    elif 1300 < frequencia <= 1400:
        arduino.write(struct.pack('>B', 7))
    elif 1400 < frequencia:
        arduino.write(struct.pack('>B', 8))
    else:
        arduino.write(struct.pack('>B', 0))


def acender_leds2(amplitude):
    if 0 < amplitude <= 125:
        arduino.write(struct.pack('>B', 11))
    elif 125 < amplitude <= 250:
        arduino.write(struct.pack('>B', 12))
    elif 250 < amplitude <= 375:
        arduino.write(struct.pack('>B', 13))
    elif 375 < amplitude <= 500:
        arduino.write(struct.pack('>B', 14))
    elif 500 < amplitude <= 750:
        arduino.write(struct.pack('>B', 15))
    elif 750 < amplitude <= 875:
        arduino.write(struct.pack('>B', 16))
    elif 875 < amplitude:
        arduino.write(struct.pack('>B', 17))
    else:
        arduino.write(struct.pack('>B', 10))


# Esse trecho irá estabelecer uma conexão, com a porta a qual o Arduino irá estar conectado.
# Caso ele não achar o Arduino, ou não estabelecer uma conexão, irá gerar um erro e encerra
# o programa.

conexao = True
try:
    arduino = serial.Serial("COM3", 115200, timeout=0.1)
    print("Conexão na porta ", arduino.portstr + " estabelecida com sucesso!")

except serial.SerialException:
    print("Conexão com arduino não estabelecida.\nVerifique os cabos e a conexão!")
    conexao = False
    pass

time.sleep(1)

if conexao:
    amostragem = 4096  # Cria uma variável que irá ser definida com uma amostragem de 4096
    FORMAT = pa.paInt16  # Define o formato de sequência binária de 16 bits.
    CANAL = 1  # Define o canal aonde o som vai passar.
    RATE = 84100  # Variável que avalia a frequência de amostra em Hz

    p = pa.PyAudio()  # Instancia o objeto.
    # define os parâmetros para coletar a amostragem que passa no canal 1.
    stream = p.open(
        format=FORMAT,
        channels=CANAL,
        rate=RATE,
        input=True,
        frames_per_buffer=amostragem
    )

    # Trecho responsável pela geração do gráfico, onde irá mostra em vermelho a onda senoidal
    # do sinal analógico, e em azul, a mesma onda já processada pelo calculo de Fourier.
    # Mostrando de forma digital.

    fig, (ax, ax1) = plt.subplots(2)  # define que irá ser 2 quadros, onde o ax é o sinal original e o ax1 o FFT
    x_fft = np.linspace(0, RATE, amostragem)
    x = np.arange(0, 2 * amostragem, 2)
    line, = ax.plot(x, np.random.rand(amostragem), 'r')
    line_fft, = ax1.semilogx(x_fft, np.random.rand(amostragem))
    ax.set_ylim(-32000, 32000)
    ax.ser_xlim = (0, amostragem)
    ax1.set_ylim(0, 1)
    ax1.set_xlim(10, RATE / 2)
    fig.show()

    # Esse trecho, é responsável por coletar a amostra do microfone, armazenar nas variáveis e efetuar o calculo de
    # Fourier, e ele irá se repetir por um tempo infinito, ou até se fechar o programa, em quanto ele tiver rodando
    # ele irá coletar as amostras e exibir na tela conforme o programa foi escrito.

    while True:
        dados = stream.read(amostragem)  # Recebe os dados do microfone conforme o valor da amostragem.
        dadosInt = struct.unpack(str(amostragem) + 'h',
                                 dados)  # Converte os valores recebido do microfone em um valor inteiro
        line.set_ydata(dadosInt)
        line_fft.set_ydata(np.abs(np.fft.fft(dadosInt)) * 2 / (3300 * amostragem))
        fig.canvas.draw()
        fig.canvas.flush_events()

        # Calculo da FFT para Frequência
        fft = abs(np.fft.fft(dadosInt).real)
        fft = fft[:int(len(fft) / 2)]
        freq = np.fft.fftfreq(amostragem, 1.0 / RATE)
        freq = freq[:int(len(freq) / 2)]
        frequencia = freq[np.where(fft == np.max(fft))[0][0]] + 1
        print("Frequência: %d Hz" % frequencia)

        # Calculo da FFT para amplitude
        calculo_amplitude = np.fft.fft(dadosInt)
        calculo_amplitude = np.abs(calculo_amplitude)
        amplitude_sinal = calculo_amplitude[:int(len(calculo_amplitude) / 2)]
        amplitude_sinal = amplitude_sinal[np.where(np.max(calculo_amplitude))]
        amplitude = int(amplitude_sinal / 100)

        acender_leds2(amplitude)
        acender_leds1(frequencia)

    stream.stop_stream()
    stream.close()
    p.terminate()

else:
    print("Sem conexão!")
