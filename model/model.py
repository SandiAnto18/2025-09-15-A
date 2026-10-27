
import networkx as nx

from database.DAO import DAO

class Model:

    def __init__(self):
        # CREO UN GRAFO SEMPLICE E PESATO (non orientato)
        self._graph = nx.Graph()

    def getAllYears(self):
        # RECUPERO GLI ANNI DAL DAO
        return DAO.getAllYears()

    def buildGraph(self, da, a):
        # RECUPERO I PILOTI DEL PERIODO
        piloti = DAO.getDriver(da, a)

        # SVUOTO IL GRAFO PRECEDENTE
        self._graph.clear()

        # AGGIUNGO I PILOTI COME NODI
        self._graph.add_nodes_from(piloti)

        # CREO UNA MAPPA per collegare l' ID PILOTA all' OGGETTO DRIVER
        dMap = {}
        for d in piloti:
            dMap[d.driverId] = d

        # RECUPERO LE COPPIE DI PILOTI E I PESI
        archi = DAO.getP1P2peso(da, a)

        # AGGIUNGO GLI ARCHI CON IL LORO PESO
        for p1, p2, peso in archi:
            pilota1 = dMap[p1]
            pilota2 = dMap[p2]

            self._graph.add_edge(
                pilota1,
                pilota2,
                weight=peso
            )

    def getNumNodi(self):
        # RESTITUISCO IL NUMERO DI NODI
        return self._graph.number_of_nodes()

    def getNumArchi(self):
        # RESTITUISCO IL NUMERO DI ARCHI
        return self._graph.number_of_edges()

