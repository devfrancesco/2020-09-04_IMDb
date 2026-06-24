from database.DB_connect import DBConnect
from model.arco import Arco
from model.movie import Movie


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllRatings():
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT distinct m.rank
                    from movies m
                    where m.`rank` is not null
                    order by m.rank asc"""
        cursor.execute(query)
        for row in cursor:
            results.append(row["rank"])
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllMovies():
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query = """select m.*
                    from movies m 
                    where m.`rank` is not null 
                    order by m.name """
        cursor.execute(query)
        for row in cursor:
            results.append(Movie(**row))
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllEdges(rank, idMapM):
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query = """with attori_comparsi_film as (
                        select m.id m_id, a.id as a_id
                        from movies m 
                        join roles r on r.movie_id = m.id 
                        join actors a on a.id = r.actor_id 
                        where m.`rank` >= %s
                        )
                    select a.m_id as m1, a2.m_id as m2, count(distinct a.a_id ) as peso
                    from attori_comparsi_film a
                    join attori_comparsi_film a2 on a.a_id = a2.a_id
                    where a.m_id < a2.m_id 
                    group by a.m_id , a2.m_id """
        cursor.execute(query, (rank,))
        for row in cursor:
            results.append(Arco(idMapM[row['m1']], idMapM[row['m2']], row['peso']))
        cursor.close()
        conn.close()
        return results


