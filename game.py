import sqlalchemy


class game:
    def __init__(self, DB_URI):
        self.engine = sqlalchemy.create_engine(DB_URI)
        self.meta = sqlalchemy.MetaData()
        self.meta.reflect(self.engine)
        self.connection = self.engine.connect()
        self.gameTable = self.meta.tables["game"]

    # update from game column
    def updateGameData(self, gameData, updatedGameData):
        if type(gameData) == int:
            column = "score"
            dataType = "ID"
        else:
            column = "game"
            dataType = "Name"
        query = (
            self.gameTable.update()
            .values({f"{column}{dataType}": updatedGameData})
            .where(self.gameTable.c[f"{column}{dataType}"] == gameData)
        )
        done = self.connection.execute(query)
        self.connection.commit()
        if done:
            return True
        else:
            return False

    # delete game row
    def deleteGameData(self, gameData):
        query = self.gameTable.delete().where(self.gameTable.c["gameID"] == gameData)
        done = self.connection.execute(query)
        self.connection.commit()
        if done:
            return True
        else:
            return False

    # create game row
    def createGame(self, gameName, scoreID):
        query = self.gameTable.insert().values(gameName=gameName, scoreID=scoreID)
        done = self.connection.execute(query)
        self.connection.commit()
        if done:
            return False
        else:
            return True

    # def create(self, gameName, score_id):
    #     query = (
    #         self.meta.tables["game"]
    #         .insert()
    #         .values(gameName=gameName, score_id=score_id)
    #     )
    #     complete = self.connection.execute(query)
    #     self.connection.commit()
    #     if complete:
    #         print("New game")
    #         return True
    #     else:
    #         print("No new game")
    #         return False
    # #gameName
    # def changeName(self, gameName, newgameName):
    #     query = (
    #         self.meta.tables["game"]
    #         .update()
    #         .where(
    #         self.meta.tables["game"].c.gameName == gameName
    #         ).values(gameName = newgameName)
    #     )
    #     self.connection.execute(query)
    #     self.connection.commit()

    # def changescoer_id(self, score_id, newscore_id):
    #     query = (
    #         self.meta.tables["game"]
    #         .update()
    #         .where(
    #         self.meta.tables["game"].c.score_id == score_id
    #         ).values(score_id = newscore_id)
    #     )
    #     self.connection.execute(query)
    #     self.connection.commit()

    # def deleteName(self, gameName):
    #     query = (
    #         self.meta.tables["game"]
    #         .delete()
    #         .where(self.meta.tables["game"].c.gameName == gameName)
    #     )
    #     self.connection.execute(query)
    #     self.connection.commit()

    # def deleteID(self, game_id):
    #     query = (
    #         self.meta.tables["game"]
    #         .delete()
    #         .where(self.meta.tables["game"].c.game_id == game_id)
    #     )
    #     self.connection.execute(query)
    #     self.connection.commit()
