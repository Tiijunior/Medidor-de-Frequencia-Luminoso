//Define a pinagem do primeiro 74HC595
int latchPin = 2;
int dataPin = 3; 
int clockPin = 4;

//Define a pinagem do segundo 74HC595
int latchPin_1 = 5;
int dataPin_1 = 6; 
int clockPin_1 = 7;

// incializa o parametro para fazer o teste
int ledTest = true;

//incializa os pinos e o serial.
void setup() {
  // CI 74HC595
  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);

  // CI 74HC595
  pinMode(latchPin_1, OUTPUT);
  pinMode(clockPin_1, OUTPUT);
  pinMode(dataPin_1, OUTPUT);

  Serial.begin(115200);

// iniciliza o teste dos leds.
  if(ledTest == true)
  {
    teste_leds();
  }

}


void loop(){
  // estabelece uma comunicação serial.
  if(Serial.available() > 0)
  {
    int dados = Serial.read();    // recebe e armazena os valores recebido pela porta serial
    if(dados < 10)                // parametro para verificar qual fileira de led vai acender.
    {
      acender_led(dados);
      delay(30);
    }
    else{
      acender_led_1(dados);
      delay(30);
    }
  }

  delay(30);
  acender_led(0);                           // apaga os leds
  acender_led_1(0);                         // apaga os leds

}

//Teste para verificar se os leds estão funcionando.
void teste_leds(){

  for(int i = 1; i <= 8; i++)
  {
    acender_led(i);
    delay(150);
  }
  
  for(int j = 11; j <= 17; j++)
  {
    acender_led_1(j);
    delay(150);
  }
  delay(100);
  acender_led(0); 
  acender_led_1(0);
  delay(100);
  acender_led(8);
  acender_led_1(17);
  delay(100);
  acender_led(0); 
  acender_led_1(0);
}

// acende os leds da primeira fileira.
void acender_led(int valor){

  if (valor == 0)
    controlar_led(0);
  else if (valor == 1)
    controlar_led(128);
  else if (valor == 2)
    controlar_led(192);
  else if (valor == 3)
    controlar_led(224);
  else if (valor == 4)
    controlar_led(240);
  else if (valor == 5)
    controlar_led(248);
  else if (valor == 6)
    controlar_led(252);
  else if (valor == 7)
    controlar_led(254);
  else if (valor == 8)
    controlar_led(255);

}

// acende os leds da segunda fileira.
void acender_led_1(int valor){

  if (valor == 0)
    controlar_led_1(0);
  else if (valor == 11)
    controlar_led_1(128);
  else if (valor == 12)
    controlar_led_1(192);
  else if (valor == 13)
    controlar_led_1(224);
  else if (valor == 14)
    controlar_led_1(240);
  else if (valor == 15)
    controlar_led_1(248);
  else if (valor == 16)
    controlar_led_1(252);
  else if (valor == 17)
    controlar_led_1(254);
}

// controla o primeiro CI 74HC595
void controlar_led(byte dataOut){

  shiftOut(dataPin, clockPin, LSBFIRST, dataOut);
  digitalWrite(latchPin, LOW);
  digitalWrite(latchPin, HIGH);
  digitalWrite(latchPin, LOW);
}

// controla o segundo CI 74HC595
void controlar_led_1(byte dataOut){
  shiftOut(dataPin_1, clockPin_1, LSBFIRST, dataOut);
  digitalWrite(latchPin_1, LOW);
  digitalWrite(latchPin_1, HIGH);
  digitalWrite(latchPin_1, LOW);
}