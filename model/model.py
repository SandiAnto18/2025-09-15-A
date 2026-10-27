
import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()  # Grafo semplice e pesato

    def getAllYears(self):
        # Recupero gli anni dal DAO
        return DAO.getAllYears()

    def buildGraph(self,da,a):
        piloti= DAO.getDriver(da,a)

        # Svuoto il grafo prima di ricostruirlo
        self._graph.clear()

        # Aggiungo i costruttori come nodi
        self._graph.add_nodes_from(piloti)

        # Creo una mappa: ID -> oggetto Pilota
        pMap = {}
        for p in piloti:
                pMap[p.driverId] = p
        # Recupero le coppie di costruttori e i relativi pesi
        archi = DAO.getP1P2peso(da,a)

        # Aggiungo gli archi con il loro peso
        for p1, p2, peso in archi:
                pilota1 = pMap[p1]
                pilota2 = pMap[p2]

                self._graph.add_edge(
                    pilota1,
                    pilota2,
                    weight=peso
                )

    def getNumNodi(self):
            # Restituisco il numero di nodi
            return len(self._graph.nodes())

    def getNumArchi(self):
            # Restituisco il numero di archi
            return len(self._graph.edges())




