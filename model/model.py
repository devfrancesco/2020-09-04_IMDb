import copy

import networkx as nx
from networkx.classes import neighbors

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._movies = []
        self._idMapM = {}
        self._optPath = []

    def getBestPath(self, source_id):
        self._optPath = []
        source = self._idMapM[int(source_id)]
        parziale = [source]
        self._ricorsione(parziale, -1) # peso = -1

        return self._optPath

    def _ricorsione(self, parziale, ultimo_peso):
        if len(parziale) > len(self._optPath):
            self._optPath = copy.deepcopy(parziale)
        nodo_corrente = parziale[-1]
        for vicino in self._graph.neighbors(nodo_corrente):
            if vicino not in parziale:
                pesoCorrente = self._graph[nodo_corrente][vicino]['weight']
                if ultimo_peso <= pesoCorrente:
                    parziale.append(vicino)
                    self._ricorsione(parziale, pesoCorrente)
                    parziale.pop()

    def buildGraph(self, rank):
        self._graph.clear()
        self._idMapM = {}
        self._movies = DAO.getAllMovies()
        for m in self._movies:
            self._idMapM[m.id] = m
        self._graph.add_nodes_from(self._movies)
        allEdges = DAO.getAllEdges(rank, self._idMapM)
        for e in allEdges:
            self._graph.add_edge(e.m1, e.m2, weight=e.peso)

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getAllRatings(self):
        return DAO.getAllRatings()

    def getTopFilm(self):
        if len(self._graph.nodes) == 0:
            return None, 0
        film_migliore, somma_massima = max(self._graph.degree(weight='weight'), key=lambda x: x[1])
        return film_migliore, somma_massima

    def getAllMoviesInGraph(self):
        return list(self._graph.nodes)
