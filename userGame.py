import sqlalchemy


class userGame:
    def __init__(self, dbURL):
        self.engine = sqlalchemy.create_engine(dbURL)
        self.meta = sqlalchemy.MetaData()
        self.meta.reflect(self.engine)
        self.connection = self.engine.connect()
        self.userGame = self.meta.tables["usergame"]

    def newUserGame(self, userID, gameID):
        query = self.userGame.insert().values(
            userID=userID,
            gameID=gameID,
        )
        done = self.connection.execute(query)
        self.connection.commit()
        if done:
            return True
        else:
            return False

    def deleteUserGame(self, userGameID):
        query = self.userGame.delete().where(
            self.userGame.c["userGameID"] == userGameID
        )
        done = self.connection.execute(query)
        self.connection.commit()
        if done:
            return True
        else:
            return False

    def editUserGameData(self, userGameData, newUserGameData, dataType):
        query = (
            self.userGame.update()
            .where(self.userGame.c[f"{dataType}"] == userGameData)
            .values({f"{dataType}": newUserGameData})
        )
        done = self.connection.execute(query)
        self.connection.commit()
        if done:
            return True
        else:
            return False

    # def edituser_game_id(self, game_id, newgame_id):
    #     query = (
    #         self.meta.tables["user_game"]
    #         .update()
    #         .where(self.meta.tables["user_game"].c["game_id"] == game_id)
    #         .values(game_id=newgame_id)
    #     )
    #     done = self.connection.execute(query)
    #     self.connection.commit()
    #     if done:
    #         return True
    #     else:
    #         return False
