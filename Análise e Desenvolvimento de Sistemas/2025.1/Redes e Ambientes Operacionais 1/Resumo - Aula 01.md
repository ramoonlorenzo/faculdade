# Redes de Dados

## Início

- As redes foram desenvolvidas devido às aplicações empresariais para microcomputadores.

- Os microcomputadores não eram conectados da mesma maneira que os **thin clients** no **mainframe**, não havendo uma maneira eficiente de compartilhar dados entre eles.

> As companhias investiram em computadores como dispositivos autônomos que às vezes vinham acompanhados de impressoras. Quando os empregados que não tinham impressoras queriam imprimir documentos, tinham que copiar seus arquivos em disquetes, levá-los até seu colega de trabalho e carregá-lo no seu PC e então fazer a impressão a partir daquele PC. Esta versão bastante rústica de rede tornou-se conhecida como **"Sneakernet"**.

- O compartilhamento de dados usando **disquetes** não era uma maneira eficiente e econômica de se administrar empresas:
  - Como **evitar a duplicação** de equipamentos e recursos?
  - Como se **comunicar eficazmente**?
  - Como **configurar e gerenciar** uma rede?

**Observações:**

- **thin clients:** É um computador cliente em uma rede de modelo cliente-servidor de duas camadas o qual tem poucos ou nenhum aplicativo instalados, de modo que depende primariamente de um servidor central para o processamento de atividades.

- **mainframe:** Um mainframe é um computador de grande porte dedicado normalmente ao processamento de um volume enorme de informações. O termo "mainframe" era utilizado para se referir ao gabinete principal que alojava a unidade central de processamento nos primeiros computadores.
- **disquetes:** O disquete é um dispositivo de armazenamento magnético que foi muito utilizado em computadores nas décadas de 1980 e 1990. Hoje, é considerado obsoleto e foi substituído por dispositivos como pen drives e cartões de memória.

No início dos anos 80, as tecnologias de rede que surgiram tinham sido criadas usando diferentes implementações de hardware e software. Devido à competição, cada empresa que criava hardware e software para redes, usava seus próprios padrões. Consequentemente, muitas das novas tecnologias de rede eram incompatíveis umas com as outras. Frequentemente, era necessário que o equipamento antigo de rede fosse removido para que fosse implementado o novo equipamento. Uma das primeiras soluções foi a criação de padrões de **redes locais (LAN)**.

![Topografia estrela](./Recursos/rede-local-lan.png)

**Exemplo: Topografia Estrela**

À medida que o uso do computador nas empresas cresceu, logo percebeu-se que as **LANs** não eram mais suficientes.

Era necessário um modo de mover informações de maneira rápida e eficiente, não só dentro da empresa, mas também de uma empresa para outra.

![Redes entre empresas](./Recursos/rede-empresas.png)

A solução foi a criação de outros tipos de redes.

## Classificação das redes quanto à extensão geográfica

|   Sigla    |           Nome            |     Distância     |       Contexto        | Descrição                                                                                                                                                                                                                                                                                                                                                                             |
| :--------: | :-----------------------: | :---------------: | :-------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PAN / WPAN |   Personal Area Network   |       1 m²        | Entorno de uma pessoa | Nesse tipo de rede sua distância é, no máximo, de algumas dezenas de metros (sem barreiras físicas, como paredes, etc), podemos citar, como exemplo da rede PAN, a rede Bluetooth.                                                                                                                                                                                                    |
| LAN / WLAN |    Local Area Network     | 10 m, 100 m, 1 km |        Campus         | Podemos defini-la como uma rede que está em uma região pequena, que pode chegar a algumas centenas de metros, mas que se reduz para bem menos. Se houver barreiras físicas (paredes, etc), haverá uma interconexão de equipamentos de comunicação de dados. Algumas características das redes locais são altas taxas de transmissão e baixas taxas de erro e são propriedade privada. |
| MAN / WMAN | Metropolitan Area Network |       10 km       |        Cidade         | São redes que ocupam o perímetro de um bairro ou uma cidade. Permitem que empresas com filiais em bairros diferentes se comuniquem.                                                                                                                                                                                                                                                   |
| WAN / WWAN |     Wide Area Network     |  100 km, 1000 km  |  País ou Continente   | São redes usadas para fazer o compartilhamento de recursos para usuários que estão geograficamente distribuídos. São redes com um custo elevado, pois utilizam circuitos para satélites e enlaces de micro-ondas.                                                                                                                                                                     |

**Observação:** A letra **"W"** no início representa a palavra **Wireless**, indicando que se trata de redes sem fio.

---

# Conectividade

A **placa de rede**, é um dispositivo de hardware responsável pela comunicação entre um computador e uma rede.

Essa placa é o hardware que permite aos computadores conversarem entre si através da rede e sua função é **controlar todo o envio e recebimento de dados** através da rede.

Cada arquitetura de rede exige um **tipo específico de placa**.

Com a utilização das tecnologias de **redes locais** e **WAN**, vários computadores são interligados para oferecer serviços aos seus usuários.

Para realizar isso, os computadores interligados assumem **diferentes papéis ou funções em relação aos outros**.

**Independente do tipo de aplicação utilizada na rede**, 2 computadores tipicamente se comunicam usando protocolos de pedido/resposta (request/response).

Um computador emite um **pedido** para um serviço e o segundo computador recebe e **responde** àquele pedido.

O requisitante assume o papel de um **cliente** e o que responde assume o papel de um **servidor**.

## Tipos de Comunicação

### Comunicação Ponto-a-Ponto

- Os hosts interconectados agem como **parceiros iguais**, ou pares.

- Cada computador pode assumir a função de **cliente** ou **servidor**.

- São relativamente fáceis de instalar e operar, pois **não é necessário nenhum equipamento adicional**, além de um SO que permita o controle de recursos.

![Exemplo de Comunicação Ponto-a-Ponto](./Recursos/ponto-a-ponto.png)

### Vantagens (Comunicação Ponto-a-Ponto)

- Mais **econômico** para implementar;

- **Não exige software adicional** especializado em administração de redes;

- Não exige um administrador **dedicado** de redes.

### Desvantagens (Comunicação Ponto-a-Ponto)

- **Não se adapta bem ao crescimento** de grandes redes e a administração se torna mais difícil de ser gerenciada;

- Cada **usuário precisa ser treinado** para realizar tarefas administrativas;

- Menos seguro;

- Todas as máquinas que compartilham os recursos tem o **desempenho** afetado de maneira negativa.

### Comunicação Cliente/Servidor

- Os serviços de redes estão localizados em um computador dedicado denominado **servidor**.

- O servidor **responde às solicitações de clientes** para arquivos, impressão, aplicativos e outros serviços.

- Os servidores são projetados para processarem **simultaneamente** solicitações de vários clientes.

![Exemplo de Comunicação Cliente/Servidor](./Recursos/cliente-servidor.png)

### Vantagens (Comunicação Cliente/Servidor)

- Oferece **maior segurança**;

- É **mais fácil de se administrar** quando a rede é grande pois a administração é centralizada;

- Pode-se fazer **backup dos dados em um local central**.

### Desvantagens (Comunicação Cliente/Servidor)

Exige **software especializado muito caro** para a operação de a administração de redes;

Exige **hardware mais caro** e muito mais potente para a máquina do servidor;

Requer um **administrador profissional**;

Possui um único ponto de falha. Se o servidor estiver inativo, os dados do usuário não estarão disponíveis.

---
