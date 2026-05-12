# Sprint1_Assembly

Título do projeto
  EV-Auth: Assembly-Level Charge Controller

Integrantes (nome + RM)
  Nícolas Andrade Rodrigues - 572782
  
Problema
  No cenário de automóveis elétricos, é necessária uma cautela maior, exigindo questões como verificações de conexão física segura e o nível de bateria, para não ocorrer sobrecarga ou vazamento de energia. Porém, o que se visa é que essa verificação seja feita de maneira mais eficiente e rápida possível, criando assim, a necessidade de um sistema leve e rapído, algo conectado diretamente ao hardware do sistema, sem a dependência do alto-nivel.
  
Justificativa
  A escolha pelo Assembly x86 (32 bits) justifica-se pela necessidade de eficiência máxima e tamanho reduzido. Em sistemas embarcados (chips de carregadores), o espaço de armazenamento é limitado e demanda controle total em registradores e consumo menor de recursos.
  
Proposta de solução
  Um sistema que verifique o veículo, nível de bateria do veículo e segurança de conexão do cabo. Somente com todos esses requisitos atendidos, será iniciada uma sessão de carregamento. E como dito anteriormente, esse sistema é feito em Assembly, o que nos permite um controle total de dados e maior eficiência.
  
Arquitetura utilizada
  Arquitetura CISC, que visa um número menor de instruções, facilitando o entendimento pois se assemelha a uma linguagem de alto nível. O sistema conversa diretamente com o kernel do linux via interrupção "int 0x80". A manipulação de registradores é feita no modelo EX
  
Trechos de código Assembly (se possível)
  {mov eax, 4      ; ID da função sys_write
mov ebx, 1      ; Canal de saída (Monitor)
mov ecx, msg    ; Endereço da memória onde está o texto
int 0x80        ; Interrupção: "Kernel, faz o seu trabalho!"} 
Este é o "Aperto de mão", onde conectamos o processador ao mundo real, onde visualizamos no terminal.

Impactos esperados
  Visamos o consumo mínimo de hardware, e mesmo utilizando menos das máquinas, é esperado uma velocidade maior do sistema, pela conexão em baixo nível do código do projeto

Relação com sustentabilidade e energias renováveis
  Sustentabilidade de hardware, pois demandando menos do hardware, é necessário menores ciclos de processamento, fazendo utilizar menos energia. Em escala mínima, não é possível ver grande diferença ou sustentabilidade, mas em larga escala, o impacto acumulado é enorme.
  Olhando para o projeto agora e futuramente, se usassemos linguagens de alto nível, com demanda de memória que vem aumentando a cada dia, há chance do sistema novo não se adequar ao chip antigo, e o dispositivo se tornar lixo eletrônico. Porém com a linguagem de baixo nível, o sistema pode se adequar por muito mais tempo.
