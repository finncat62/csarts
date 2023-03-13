#V3 might be working better then v2. All changes are in the build frontier

import sys, os, time

from ai_F.ai import *
from board_F.board import *


# minimax version

#features for the future:
#     - use pygaem to display (might not work on person running code's computer)
#     - have winning image sequence
#     - when there are no possible moves that can win, tie 


class TicTacToeGame:
  validationInputs = {
    "y": True,
    "yes": True,
    "sure": True,
    "of course": True,
    "definatly": True,
    "affirmative": True,
    "yup": True,
    "ya": True,
    "yuh": True,
    "certainly": True,
    "n": False,
    "no": False,
    "nope": False,
    "nadda": False,
    "never": False,
  }
 
  def __init__(self):
    print("game initialization")
    self.board = c_board(True,[],0,[],True)
    print("press anything to start a game")
    input("> ")
    self.getPlayMode()
    self.startGame()
  
  def startGame(self):
    #os.system("clear")
    
    self.board.resetBoard()

    self.playGame()

  
  def playGame(self):
    endGameStates = [c_board.winType["x"],c_board.winType["o"],c_board.winType["tie"]]
    self.display()
    if (self.board.winState in endGameStates):
    
      valid = False
      while (not valid):
        try:
          print(" continue on same game mode:       1")
          print(" try playing a different gamemode: 2")
          try:
            answer = int(input(">"))
          except:
            raise Exception("not a number")
          if (answer == 2):
            valid = True
            self.getPlayMode()
          elif (answer == 1):
            valid = True
          else:
            valid = False
            raise Exception("answer is not 1 or 2")
        except Exception as e:
          print(e)
     # os.system("clear")
      self.startGame()
    elif(self.board.winState == c_board.winType["none"]):
      if (self.playAi == False):
        self.playerMark()
      else:
        if (self.playerFirst == self.board.currentTurn):
          print("player")
          self.playerMark()
        else:
          print("ai")

          aiMove = c_aiPlayer(self.board.field,self.board.currentTurn,self.playerFirst,self.board.width,[],self.aiMode).getMove()
          print('aiMove is', aiMove)
          
          self.board.fillBoard(aiMove)

      self.board.winState = self.board.evaluatePosition()
      print("wS: ",self.board.winState)
      self.playGame()
  
  
  def printWinner(self):
    if (self.playAi):
      if((self.playerFirst == self.board.currentTurn)):
        print("you win")
      else:
        print("ai wins")
    elif(not self.playAi):
      if(self.board.currentTurn):
        print("p1 wins")
      else:
        print("p2 wins")
 
  def display(self):
    #os.system("clear")
    self.board.printBoard()
    print(self.board.path)
    if(self.board.winState == c_board.winType["tie"]):
      print("tie")
    elif(self.board.winState == c_board.winType["x"] or self.board.winState == c_board.winType["o"]):
      self.board.currentTurn = not self.board.currentTurn
      self.printWinner()
      self.board.newField()
  
 
  def playerMark(self):  #either x or o
    self.foundTile = False
    valid = False
    while(not valid):
      try:
        answer = input("tileNum: ")
        if(answer == "e"):
          self.resetScreen()
          self.board.newField()
          break
          
        tileNum = int(answer)
        for row in self.board.field:
          for val in row:
            if val == tileNum:
              valid = True
        
        if(not valid):
          raise Exception("no tile found")
      except Exception as e:
        print(e)
      self.board.fillBoard(tileNum)
    
  def resetScreen(self):
    while(True):
      print("sit here to relax")
      time.sleep(1)
      print("we are zen")
      time.sleep(1)
      print("press enter to start a new game")
      time.sleep(1)
      print("but take your time")
      input(">")
      self.startGame()
   
    
  def getPlayMode(self):
    self.board.resetBoard()
    allValid = False
    while (allValid == False):
      try:
        print("play against AI? y/n")
        answer = input("> ").lower().strip()

        if (answer not in self.validationInputs):
          raise Exception("not a valid input")

        self.playAi = self.validationInputs[answer]
        if (not self.playAi):
          allValid = True
          break

        
        print("AI Mode: 1) next!")
        print("         2) random!")
        print("         3) Smart")
        answer = input(">").strip()
        if(answer not in ["1","2","3"]):
          raise Exception("not a valid input")
        self.aiMode = int(answer)
        
        print("play first? y/n")
        answer = input("> ").lower().strip()
        if (answer not in self.validationInputs):
          raise Exception("not a valid input")

        self.playerFirst = self.validationInputs[answer]
        allValid = True
      except Exception as e:
        print(e)


def main():
  global game
  game = TicTacToeGame()
  

main()
