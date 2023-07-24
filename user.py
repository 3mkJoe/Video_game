import sqlalchemy


class user:
    def __init__(self, dbURL):
        self.engine = sqlalchemy.create_engine(dbURL)
        self.meta = sqlalchemy.MetaData()
        self.meta.reflect(self.engine)
        self.connection = self.engine.connect()
        self.userTable = self.meta.tables["user"]
        self.scoreTable = self.meta.tables["score"]
        self.userGameTable = self.meta.tables["usergame"]
        self.gameTable = self.meta.tables["game"]

    def login(self, username, password):
        query = (
            self.meta.tables["user"]
            .select()
            .where(
                self.meta.tables["user"].c.username == username,
                self.meta.tables["user"].c.password == password,
            )
        )
        result = self.connection.execute(query).fetchall()
        if result:
            return result

    def getAllUsers(self):
        query = self.meta.tables["user"].select()
        return self.connection.execute(query).fetchall()

    def getUser(self, username, password):
        query = self.userTable.select().where(
            self.userTable.c["username"] == username,
            self.userTable.c["password"] == password,
        )
        user = self.connection.execute(query).fetchall()
        return user

    def findUser(self, username):
        query = self.userTable.select().where(self.userTable.c.username == username)
        user = self.connection.execute(query).fetchall()
        return user

    def checkUser(self, username, password):
        query = self.userTable.select().where(
            self.userTable.c.username == username,
            self.userTable.c.password == password,
        )
        result = self.connection.execute(query).fetchall()
        if not result:
            return False
        else:
            return True

    def userGameData(self, userID):
        joinQueryUser = (
            self.userTable.join(
                self.userGameTable,
                self.userGameTable.c["userID"] == self.userTable.c["userID"],
                # == self.gameTable.c["gameID"],
                # self.userGameTable,
                # self.userGameTable.c["gameID"] == self.gameTable.c["gameID"],
            )
            .join(
                self.gameTable,
                self.userGameTable.c["gameID"] == self.gameTable.c["gameID"],
            )
            .select()
            .where(self.userTable.c["userID"] == userID)
        ).with_only_columns(self.userTable.c["username"], self.gameTable.c["gameName"])

        # def filterUser(self, dataType, filter=[]):
        #     data = []
        #     for x in filter:
        #         x = self.userTable.c[f"{dataType}"] == x
        #         print(x)
        #         data.append(x)
        #     query = self.userTable.select().where(*data)
        #     user = self.connection.execute(query).fetchall()
        #     return user

        result = self.connection.execute(joinQueryUser).fetchall()
        return result

    def userScoreData(self, userID):
        joinQuery = (
            self.userTable.join(
                self.scoreTable,
                self.scoreTable.c["userID"] == self.userTable.c["userID"],
            )
            .select()
            .where(self.userTable.c["userID"] == userID)
        ).with_only_columns(
            self.userTable.c["username"], self.scoreTable.c["scoreNumber"]
        )
        result = self.connection.execute(joinQuery).fetchall()
        return result

    def register(self, username, fullname, password):
        if not self.checkUser(username, password):
            query = self.userTable.insert().values(
                username=username,
                fullname=fullname,
                password=password,
            )
            done = self.connection.execute(query)
            self.connection.commit()
            if done:
                return True
        else:
            return False

    def deleteUser(self, id):
        query = self.userTable.delete().where(self.userTable.c["userID"] == id)
        done = self.connection.execute(query)
        self.connection.commit()
        if done:
            return True
        else:
            return False

    def updateUserTableElement(self, userID, newUserData, dataType):
        # if type(userData) == int and type(newUserData) == int:
        #     return False
        query = (
            self.userTable.update()
            .where(self.userTable.c["userID"] == userID)
            .values({f"{dataType}": newUserData})
        )

        done = self.connection.execute(query)
        self.connection.commit()
        if done:
            return True
        else:
            return False

    # def chechScoreId(self,score_id):
    #     self.meta.tables['score'].select().where(self.meta.tables['score'].c.score_id==score_id)

    # joinQueryGame = (
    #     self.gameTable.join(
    #         self.userGameTable,
    #         self.userGameTable.c["gameID"] == self.gameTable.c["gameID"],
    #     )
    #     .select()
    #     .where(self.userTable.c["userID"] == userID)
    # ).with_only_columns(
    #     self.gameTable.c["gameName"], self.userGameTable.c["gameName"]
    # )

    # def editFullname(self, fullname, newFullname):
    #     query = (
    #         self.userTable.update()
    #         .where(self.userTable.c["fullname"] == fullname)
    #         .values(fullname=newFullname)
    #     )
    #     done = self.connection.execute(query)
    #     self.connection.commit()
    #     if done:
    #         return True
    #     else:
    #         return False

    # def editPassword(self, password, newPassword):
    #     query = (
    #         self.userTable.update()
    #         .where(self.userTable.c["password"] == password)
    #         .values(password=newPassword)
    #     )
    #     done = self.connection.execute(query)
    #     self.connection.commit()
    #     if done:
    #         return True
    #     else:
    #         return False

    # def editScoreId(self, scoreID, newScoreId):
    #     query = (
    #         self.userTable.update()
    #         .where(self.userTable.c["scoreID"] == scoreID)
    #         .values(scoreID=newScoreId)
    #     )
    #     done = self.connection.execute(query)
    #     self.connection.commit()
    #     if done:
    #         return True
    #     else:
    #         return False
