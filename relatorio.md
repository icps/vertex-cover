# Modelagem

A modelagem deste problema se deu da seguinte forma: seja o grafo não-orientado, bipartido e conexo
G = (V, E), onde V são os vértices e E são as arestas. Como esse grafo é bipartido, primeiramente temos
que descobrir as partições do mesmo. Para isso, após adicionar todas as arestas, calculamos uma coloração
do grafo de no máximo duas cores, dessa forma, os grafos de cor 1 estão em uma partição e os grafos de cor
2 estão em outra. Essa coloração é calculada utilizando uma Busca em Profundidade (Depth-first search -
DFS), onde, para cada vértice u, pintado da cor 1, seu próximo vizinho v é pintado da cor 2. Como sabemos
previamente que o vértice é bipartido, essa coloração sempre acontecerá como esperado. Além disso, como
sabemos que o grafo é conexo, não precisamos reinicializar o DFS para outras fontes, tendo apenas uma única
árvore (ou seja, começamos de um vértice fonte e não há a necessidade de calcular a coloração a partir de
outro vértice, pois não há vértices que não sejam atingı́veis a partir do vértice fonte).
Após obter as partições S e T do grafo G, transformamos esse grafo em direcionado da seguinte forma:
seja (u, v) uma aresta não direcionada, onde u ∈ S e v ∈ T , então, essa aresta passa a ser direcionada de u
para v. Além disso, adicionamos um vértice fonte s, que possui arestas direcionadas para todos os vértices
de S (para cada vértice v em S, criamos a aresta direcionada (s, v)) e um vértice sorvedouro t que, para cada
vértice v ∈ T , cria-se a aresta direcionada (v, t). Todas as arestas presentes no grafo tem capacidade igual a
um. A figura 1 mostra um exemplo da transformação acima. Com isso, modelamos este problema como um
problema de fluxo, o qual podemos resolver através do algoritmo Edmonds-Karp.
Ao executar o algoritmo no grafo obtido com a transformação descrita acima, calculamos o maximum
bipartite matching. O teorema de König nos diz que “em qualquer grafo bipartido, o número de arestas em
um maximum matching é igual ao número de vértices de uma cobertura de vértices mı́nima”. Dessa forma,
ao resolvermos o problema de maximum matching automaticamente resolvemos o problema de cobertura de
vértices mı́nima, que é o que desejamos.

Figure 1: Exemplo de grafo G, obtido a partir das arestas {(5, 3), (5, 4), (2, 5), (2, 1), (3, 1)}




# Análise de Complexidade

Para a leitura da entrada de tamanho E, precisa-se ler toda a entrada, logo, temos um custo O(E). A
adição de arestas no grafo, que consiste em adicionar um novo valor na lista de adjacências, possui custo
constante. A coloração dos vértices, feita por um DFS, tem custo O(V + E) e a adição da fonte e sorvedouro
tem custo O(V) (pois a adição de arestas tem custo constante). Logo, a transformação do grafo original
para o problema de fluxo tem custo O(V + E). O algoritmo de Edmonds-Karp, que utiliza uma Busca em
Largura (Breadth-first Search - BFS) para encontrar augmenting path no algoritmo de Ford-Fulkerson, tem
custo O(V E^2). Logo, o custo total é O(V E^2).
