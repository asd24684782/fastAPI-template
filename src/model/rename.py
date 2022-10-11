# Standard library imports
import logging
import json
import uuid

# Third party imports
import psycopg2

# Local application imports


logger = logging.getLogger()

class rename:
    """PostgreSQL Database class."""

    def __init__(self, host, username, password, port, dbName):
        self.__host     = host
        self.__username = username
        self.__password = password
        self.__port     = port
        self.__dbName   = dbName

    def connect(self):
        """Connect to a Postgres database."""
        try:
            conn = psycopg2.connect(
                host=self.__host,
                user=self.__username,
                password=self.__password,
                port=self.__port,
                dbname=self.__dbName
            )


        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            logger.info('Connection opened successfully.')
            return conn
    
    #Read data from rename table
    def getrename(self):
        try:
            sql = """ SELECT * FROM rename"""
            conn = self.connect()
            with conn.cursor() as cur:
                cur.execute(sql)
                records = cur.fetchall()

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e
        
        finally:
            if conn:
                conn.close()     
            return records

    #inert data into rename table
    def insertrename(self, renameUUID, renameJsonStr):
        try:
            sql = """ INSERT INTO rename (id, info) VALUES (%s, %s) """
            insertTuple = (renameUUID, renameJsonStr)
            
            conn = self.connect()
            with conn.cursor() as cur:
                cur.execute(sql, insertTuple)
                conn.commit()

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            if conn:
                conn.close()
            logger.info('insert successfully.')

    #delete data from rename table
    def deleterename(self, renameUUID):
        try:
            sql = """ DELETE FROM rename WHERE id=%s """

            conn = self.connect()
            with conn.cursor() as cur:
                cur.execute(sql, (renameUUID,))
                conn.commit()
                rows_deleted = cur.rowcount
                print(rows_deleted)

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            if conn:
                conn.close()
            logger.info('delete successfully.')     
        
        

if __name__ == '__main__':
    pass