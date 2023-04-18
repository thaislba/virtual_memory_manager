## Contexto

O presente projeto tem como objetivo apresentar uma simulação de um gerenciador de memória virtual. A técnica utilizada por esse tipo de gerenciamento não necessita que todo o programa seja carregado na memória principal para executá-lo, isso se deve ao fato de que nem todas as partes do programa são necessárias o tempo todo para seu funcionamento. Esse tipo de gerenciamento tem como objetivo expandir a memória total disponível ao adicionar o espaço em disco. Esse gerenciamento permite: 
que somente a memória necessária seja utilizada;
execução simultânea de diferentes programas;
execução de programas maiores que a memória física.
Para isso, o espaço de endereçamento de memória é dividido em páginas, sendo que cada página é uma porção da memória, ou seja, uma séria contígua de endereços. Essas páginas são mapeadas a partir da memória física e do disco. Esse mapeamento é gerenciado pela MMU - Memory Management Unity. Quando o programa sendo executado tenta acessar uma posição de memória, a MMU recebe o endereço virtual, busca a qual página esse endereço pertence, transforma o endereço virtual em endereço físico e envia os endereços físicos mapeados à memória.

## Funcionamento 

O funcionamento do gerenciador de memória virtual é baseado na demanda, ou seja, as páginas são carregadas na memória física apenas quando são necessárias para a execução de um programa. Quando um programa é executado, a MMU recebe o endereço virtual da página que o programa está tentando acessar. Se a página correspondente já estiver na memória física, a MMU converte o endereço virtual em um endereço físico e permite o acesso à página. Se a página não estiver na memória física, a MMU emite um sinal de falha de página, indicando que a página precisa ser carregada da memória virtual para a memória física. Quando a página não é mais necessária, ela é descarregada da memória física para a memória virtual, e o endereço físico correspondente na tabela de páginas é atualizado para indicar que a página não está mais presente na memória física.

![architecture_vmm](https://user-images.githubusercontent.com/39035437/232640981-df436fd6-18a2-4813-968b-105b6b4c02a9.jpg)

## Código


## Referências:

OLIVEIRA, Rômulo S.; CARISSIMI, Alexandre S.; TOSCANI, Simão S. Sistemas Operacionais-Vol. 11. 2009.
TANENBAUM, Andrew S.; MACHADO FILHO, Nery. Sistemas operacionais modernos. Prentice-Hall, 1995.
Notas de aulas de João Marcelo Borovina Josko
