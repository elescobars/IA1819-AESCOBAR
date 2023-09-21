# Comparando algoritmos de búsqueda en términos de espacio y tiempo

Utilizando el ejemplo del juego de puzzle 8 de habdolla en github, se compararon los diferentes algoritmos de búsqueda para visualizar las diferencias entre el rendimiento de cada uno de ellos en cuestiones de espacio y tiempo.

## Rendimiento de algoritmos en dificultad EASY

|Algoritmo|Dificultad|Complejidad en espacio|Complejidad en tiempo|
|:---:|:---:|:---:|:---:|
|breadthFirstSearch()|EASY|78 estados visitados|22 recorridos|
|depthFirstSearch()|EASY|116 estados visitados|59 recorridos|
|uniformCostSearch()|EASY|39 estados visitados|21 recorridos|
|bestFirstSearch()|EASY|14 estados visitados|22 recorridos|
|aStar(Heuristic.H_ONE)|EASY|27 estados visitados|24 recorridos|
|aStar(Heuristic.H_TWO)|EASY|59 estados visitados|23 recorridos|
|aStar(Heuristic.H_THREE)|EASY|64 estados visitados|22 recorridos|

## Rendimiento de algoritmos en dificultad MEDIUM

|Algoritmo|Dificultad|Complejidad en espacio|Complejidad en tiempo|
|:---:|:---:|:---:|:---:|
|breadthFirstSearch()|MEDIUM|499 estados visitados|30 recorridos|
|depthFirstSearch()|MEDIUM|26 estados visitados|29 recorridos|
|uniformCostSearch()|MEDIUM|227 estados visitados|23 recorridos|
|bestFirstSearch()|MEDIUM|949 estados visitados|30 recorridos|
|aStar(Heuristic.H_ONE)|MEDIUM|157 estados visitados|27 recorridos|
|aStar(Heuristic.H_TWO)|MEDIUM|317 estados visitados|24 recorridos|
|aStar(Heuristic.H_THREE)|MEDIUM|532 estados visitados|29 recorridos|

## Rendimiento de algoritmos en dificultad HARD

|Algoritmo|Dificultad|Complejidad en espacio|Complejidad en tiempo|
|:---:|:---:|:---:|:---:|
|breadthFirstSearch()|HARD|181 440 estados visitados|269 recorridos|
|depthFirstSearch()|HARD|42 554 estados visitados **(1)**|9 559 recorridos|
|uniformCostSearch()|HARD|181 360 estados visitados|298 recorridos|
|bestFirstSearch()|HARD|1 663 estados visitados|103 recorridos|
|aStar(Heuristic.H_ONE)|HARD|181 405 estados visitados|327 recorridos|
|aStar(Heuristic.H_TWO)|HARD|181 137 estados visitados|348 recorridos|
|aStar(Heuristic.H_THREE)|HARD|174 454 estados visitados|348 recorridos|

**(1)** No se toma como una medida confiable de complejidad en espacio debido a un posible overflow de la variable que cuenta los estados visitados. Como vemos, el tiempo sugiere un incremento masivo de la complejidad con el uso del algoritmo.