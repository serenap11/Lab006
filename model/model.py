from database.DB_connect import get_connection
from strumento import Strumento

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        lista_strumenti = []
        try:
            cnx = get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = ("""SELECT codice, tipo, marca, anno_acquisto, valore, disponibile
                     FROM STRUMENTO""")
            cursor.execute(query)
            for row in cursor:
                strumento = Strumento(**row)
                lista_strumenti.append(strumento)
            return lista_strumenti
        except Exception as e:
            print(e)
            return None
        finally:
            cursor.close()
            cnx.close()

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        lista_tipo = []
        try:
            cnx = get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """
                    SELECT codice, tipo, marca, anno_acquisto, valore, disponibile
                    FROM STRUMENTO
                    WHERE tipo = %s
                    """
            cursor.execute(query, (tipo, ))
            for row in cursor:
                strumento = Strumento(**row)
                lista_tipo.append(strumento)
            return lista_tipo
        except Exception as e:
            print(e)
            return None
        finally:
            cursor.close()
            cnx.close()
