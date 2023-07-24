import connect
import user as fileUser
import game as fileGame
import score as fileScore
import userGame as fileUserGame

user = fileUser.user(connect.DB_URl)
score = fileScore.score(connect.DB_URl)
userGame = fileUserGame.userGame(connect.DB_URl)
game = fileGame.game(connect.DB_URl)

# score.updateScoreData(2,1,'userID')
# score.deleteScoreData(3)
# score.createScore(200,2)

# game.updateGameData("Brawl stars",'NFS')
# game.deleteGameData(1)
# game.createGame("Brawl stars", 1)

# print(user.login('ahmad','1234'))
# print(user.getAllUsers())
# print(user.getUser(1))
# print(user.findUser('ahmad'))
# user.register("ahmad", "ahmad ali", 5678)
user.updateUserTableElement(1, "ahmad sherif", "fullname")
# user.userScoreData(1)
# user.userScoreData(2)
# user.userGameData(2)
# user.deleteUser(4)

# userGame.editUserGameData(2,1, "gameID")
# userGame.newUserGame(2,1)
# userGame.deleteUserGame(1)
