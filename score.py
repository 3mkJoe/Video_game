import sqlalchemy

# Import pandas package
# import pandas as pd
# import numpy as np


class score:
    def __init__(self, db_url):
        self.engine = sqlalchemy.create_engine(db_url)
        self.meta = sqlalchemy.MetaData()
        self.meta.reflect(self.engine)
        self.connection = self.engine.connect()
        self.scoreTable = self.meta.tables["score"]

    # create score row
    def createScore(self, scoreNumber, userID):
        query = self.scoreTable.insert().values(
            scoreNumber=scoreNumber,
            userID=userID,
        )
        done = self.connection.execute(query)
        self.connection.commit()
        if done:
            return False
        else:
            return True

    # delete score by score Number or ID
    def deleteScoreData(self, scoreData, type="ID"):
        query = self.scoreTable.delete().where(
            self.scoreTable.c[f"score{type}"] == scoreData
        )
        done = self.connection.execute(query)
        self.connection.commit()
        if done:
            return True
        else:
            return False

    # update from score column
    def updateScoreData(self, scoreData, updatedScoreData, dataType="scoreNumber"):
        query = (
            self.scoreTable.update()
            .values({f"{dataType}": updatedScoreData})
            .where(self.scoreTable.c[f"{dataType}"] == scoreData)
        )
        done = self.connection.execute(query)
        self.connection.commit()
        if done:
            return True
        else:
            return False

    # def getColumnNames(self):
    #     # technologies= {
    #     # 'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    #     # 'Fee' :[22000,25000,23000,24000,26000],
    #     # 'Duration':['30days','50days','30days', None,np.nan],
    #     # 'Discount':[1000,2300,1000,1200,2500]}
    #     # df = pd.DataFrame(technologies)
    #     df = pd.DataFrame(self.tables['score'])
    #     print(df)
    #     column_headers = df.columns.values.tolist()
    #     print("The Column Header :", column_headers)

    # update score
    # def updateScoreData(self, scoreData, updateScoreData,dataType='Number'):

    #         if(dataType=='Number'):
    #             columnData=score.scoreNumber
    #         else:
    #             columnData=self.meta.tables['score'].c['scoreID']
    #         query = (
    #             self.meta.tables["score"]
    #             .update()
    #             .where(
    #                 self.meta.tables["score"].c[f'score{dataType}'] == scoreData
    #             ).values( columnData = updateScoreData)
    #         )
    #         # print(type(score+type1))
    #         done = self.connection.execute(query)
    #         self.connection.commit()
    #         if(done):
    #             print("Score updated")
    #             return True
    #         else:
    #             print("Score not updated")
    #             return False
    # columnid=selftables[score].scoreid
    # columnNumber=selftables[score].scorenumber

    # if (type1 = 'scoreID'):
    #      columnname

    # if(type(self.meta.tables['score'].c.scoresID)==type(type1)):
    #      print('yes')
    # else:
    #      print('no')
    #      print(type(self.meta.tables['score'].c.scoresID),self.meta.tables['score'].c.scoresID,type(type1),type1)
    # scoreType=int("scores"+type1)

    # delete score by score id
    # def deleteScoreID(self, scoreID):
    #         query = (
    #             self.meta.tables["score"]
    #             .delete()
    #             .where(
    #                 self.meta.tables["score"].c['scoreID'] == scoreID
    #             )
    #         )
    #         done = self.connection.execute(query)
    #         self.connection.commit()
    #         if(done):
    #             print("Score deleted")
    #             return True
    #         else:
    #             print("Score not deleted")
    #             return False
