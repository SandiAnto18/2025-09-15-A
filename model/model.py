
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

    def getTop3Edges(self):
        # Recupero gli archi con i relativi attributi
        edges = list(self._graph.edges(data=True))

        # Ordino per peso decrescente
        edges.sort(key=lambda e: -e[2]["weight"])

        # Restituisco i primi tre archi
        return edges[:3]

    def TotCompConnesse(self):
        # Individuo tutte le componenti connesse
        comp = list(nx.connected_components(self._graph))
        return comp

    def getLargestComp(self, comp):
        # Scelgo la componente con più nodi
        largest = max(comp, key=len)

        # Ordino i nodi per grado decrescente
        largestOrdinata = sorted(
            largest,
            key=lambda x: self._graph.degree(x),
            reverse=True
        )

        return largestOrdinata

    def getDegree(self, c):
        # Restituisco il grado del costruttore
        return self._graph.degree(c)

