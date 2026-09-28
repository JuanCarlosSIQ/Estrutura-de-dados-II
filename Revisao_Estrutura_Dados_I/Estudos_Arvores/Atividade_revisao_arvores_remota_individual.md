Atividade de Revisao: Estruturas de Arvores
Disciplina: Estrutura de Dados II
Professora: Kadidja Valeria
Nome: Juan Carlos Siqueira de Lima
Turma: D1
Data: 28/09/2026
---
ETAPA 1 - REVISAO BIBLIOGRAFICA

Conceitos basicos:
 No: e o elemento que guarda o dado e aponta pros outros.
 Raiz: e o primeiro no la do topo, nao tem ninguem acima dele.
 Pai e filho: o de cima e pai e o de baixo e filho.
 Folha: e o no do fim da arvore que nao tem filho nenhum.
 Altura: quantidade de passos da raiz ate a folha mais distante.
 Percurso: a ordem que a gente usa pra passar por todos os nos.

Tipos de arvore:

1. Arvore Geral
 Como organiza: qualquer no pode ter quantos filhos quiser.
 Regra: so tem uma raiz e um caminho unico pra cada no.
 Busca e insercao: busca olha no por no e pra inserir so pendura embaixo.
 Ajuste: nao ajusta nada sozinho.
 Uso: pastas do computador.

2. Arvore Binaria
 Como organiza: cada no tem no maximo 2 filhos (esquerda e direita).
 Regra: limite de 2 filhos por no.
 Busca e insercao: busca olha elemento por elemento e insercao coloca no primeiro lugar vago.
 Ajuste: nao organiza nada.
 Uso: contas matematicas e tomadas de decisao.

3. Arvore Binaria de Busca (ABB)
 Como organiza: arvore binaria ordenada.
 Regra: menor vai pra esquerda e maior vai pra direita.
 Busca e insercao: compara com o no atual, se for menor vai pra esquerda e se for maior pra direita.
 Ajuste: nao se arruma sozinha, vira uma linha reta se entrar ordenado.
 Uso: listas de busca simples na memoria.

4. Arvore AVL
 Como organiza: ABB que fica sempre equilibrada.
 Regra: a diferenca de altura dos dois lados nao pode ser maior que 1.
 Busca e insercao: busca e rapida e na insercao ajusta se pender pra um lado.
 Ajuste: faz rotacoes pros lados pra reequilibrar.
 Uso: sistemas com muita leitura e pouca alteracao.

5. Arvore Rubro-Negra
 Como organiza: ABB onde os nos sao vermelhos ou pretos.
 Regra: no vermelho nao tem filho vermelho e a quantidade de nos pretos ate as pontas e igual.
 Busca e insercao: busca rapida, insere como vermelho e checa as regras.
 Ajuste: troca cor e faz rotacoes.
 Uso: linguagens tipo C++ e no Linux.

6. Arvore B
 Como organiza: o no guarda varios valores juntos.
 Regra: todas as folhas ficam na mesma altura.
 Busca e insercao: busca olha os valores dentro do no, insere na folha.
 Ajuste: se encher ele se divide em dois.
 Uso: arquivos no disco do PC.

7. Arvore B+
 Como organiza: dados de verdade so ficam nas folhas, os nos de cima sao so mapa.
 Regra: folhas sao ligadas numa lista.
 Busca e insercao: vai ate a folha e segue a lista.
 Ajuste: se divide quando enche e atualiza o mapa.
 Uso: banco de dados tipo MySQL.

8. Heap
 Como organiza: arvore guardada num vetor.
 Regra: pai e sempre maior que os filhos (max-heap) ou menor (min-heap).
 Busca e insercao: maior ou menor esta no topo, insere no fim e vai subindo.
 Ajuste: sobe ou desce elementos pra manter a regra.
 Uso: fila de prioridade.

9. Trie
 Como organiza: usada pra palavras, cada no guarda uma letra.
 Regra: palavras com inicio igual usam o mesmo caminho.
 Busca e insercao: vai olhando letra por letra.
 Ajuste: nao precisa ajustar.
 Uso: autocompletar e dicionarios.
---
ETAPA 2 - QUADRO COMPARATIVO

| Estrutura | Organizacao dos dados | Regra ou propriedade | Operacao ou ajuste | Aplicacao | Referencia |
| ABB | Arvore de 2 filhos ordenada. | Menor na esquerda, maior na direita. | Nao se ajusta sozinha. | Dicionarios na memoria. | Materiais da aula, video aulas e jogo no site Visualgo.net |
| AVL | Arvore ordenada e equilibrada. | Lados com diferenca de altura no maximo 1. | Rotacoes nos nos. | Sistemas com muita leitura. | Materiais da aula, video aulas e jogo no site Visualgo.net |
| Rubro-negra | Arvore com nos vermelhos e pretos. | Vermelho nao tem filho vermelho. | Troca cor e faz rotacao. | C++ e Linux. | Materiais da aula |
| B | Varios dados no mesmo no. | Folhas no mesmo nivel. | Divide o no quando enche. | Arquivos no disco. | Materiais da aula e videos |
| B+ | Dados so nas folhas. | Folhas ligadas em fila. | Divide no e altera mapa. | Banco de dados. | Materiais da aula e videos |
| Arvore Geral | No tem quantos filhos quiser. | So uma raiz. | Sem ajuste. | Pastas no PC. | Materiais da aula |
| Arvore Binaria | Maximo 2 filhos por no. | Limite 2 filhos. | Sem ordenacao. | Contas matematicas. | Materiais da aula e video aulas |
| Heap | Arvore em vetor. | Pai maior ou menor que os filhos. | Sobe ou desce elemento. | Fila de prioridade. | Materiais da aula|
| Trie | Uma letra em cada no. | Aproveita inicio igual das palavras. | Anda letra por letra. | Autocompletar. | Materiais da aula |

---

ETAPA 3 - ANALOGIAS

1. Estante de numeros que reorganiza por rotacoes:
Estrutura: Arvore AVL.
Justificativa: quando um lado fica mais alto que o outro ela roda os nos pra equilibrar.
Limite: na estante mexe no movel, na arvore so muda os ponteiros da memoria.

2. Catalogo com chaves por pagina que se divide:
Estrutura: Arvore B.
Justificativa: guarda varios dados no no e quando enche divide em dois.
Limite: no papel rasga a folha, na memoria so cria um no novo.

3. Fila com maior prioridade no topo:
Estrutura: Heap.
Justificativa: o maior ou mais importante fica na raiz pra sair primeiro.
Limite: em fila normal e por ordem de chegada, no heap quem e importante passa na frente.

4. Indice que anda letra por letra:
Estrutura: Trie.
Justificativa: cada no e uma letra e palavras com mesmo inicio usam o mesmo caminho.
Limite: no livro ve a palavra inteira, na trie vai de letra em letra.

5. Estrutura com cores e rotacoes:
Estrutura: Arvore Rubro-Negra.
Justificativa: usa as cores vermelho e preto pra saber quando ajustar e nao deixar a arvore ficar torta.
Limite: cor no dia a dia e so enfeite, na arvore e regra de codigo.

6. Indice que vai pras folhas ligadas entre si:
Estrutura: Arvore B+.
Justificativa: dados ficam so nas folhas e elas sao ligadas em fila.
Limite: no livro procura a pagina na mao, na B+ vai direto puxando a fila.

7. Coleção onde menor vai pra esquerda e maior pra direita:
Estrutura: Arvore Binaria de Busca (ABB).
Justificativa: regra basica da ABB, menor na esquerda e maior na direita.
Limite: em colecao fisica as coisas sao fixas, na ABB o codigo decide o caminho na hora.

---

Referencias:
-Site educativo Visualgo.net, utilizado na atividade de jogo.
-Videos educativos no Youtube e Tiktok com ensino de conceitos basicos de arvore (https://www.youtube.com/watch?v=3zmjQlJhBLM).
-Inteligencias artificiais para exemplificar e tirar duvidas.
