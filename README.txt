Participantes:

17/0016641 - Lucas Dalle Rocha
17/0018997 - Matheus Breder Branquinho Nogueira

Execute os comandos para rodar cada método de busca:

DFS:
(mediumMaze):	python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
(bigMaze):	python pacman.py -l bigMaze -p SearchAgent -a fn=dfs -z .5
(openMaze):	python pacman.py -l openMaze -p SearchAgent -a fn=dfs

A* (subHeuristic):
(mediumMaze):	python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=subHeuristic
(bigMaze):	python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=subHeuristic -z .5
(openMaze):	python pacman.py -l openMaze -p SearchAgent -a fn=astar,heuristic=subHeuristic

A* (geoHeuristic):
(mediumMaze):	python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=geoHeuristic
(bigMaze):	python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=geoHeuristic -z .5
(openMaze):	python pacman.py -l openMaze -p SearchAgent -a fn=astar,heuristic=geoHeuristic