from graphics import *
import random

# game board
win = GraphWin("Tic Tac Toe", 800, 800)
line1 = Line(Point(300,100),Point(300,700))
line1.setWidth(5)
line1.draw(win)
line2 = Line(Point(500,100),Point(500,700))
line2.setWidth(5)
line2.draw(win)
line3 = Line(Point(100,300),Point(700,300))
line3.setWidth(5)
line3.draw(win)
line4 = Line(Point(100,500),Point(700,500))
line4.setWidth(5)
line4.draw(win)
title = Text(Point(400,40),"Tic-Tac-Toe")
title.setSize(36)
title.draw(win)

class Game():
    def __init__(self):
        self.over = False
        self.win = win
        self.turn = 1
        self.text_turn = Text(Point(400, 760), "Player 1's Turn")
        self.winning_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        self.filled = []
        self.p1 = []
        self.p2 = []
        self.p1_score = 0
        self.p2_score = 0
        self.p1_score_text = Text(Point(50,100),"Player 1:")
        self.p1_score_text.setSize(16)
        self.p1_score_number = Text(Point(50,150),str(self.p1_score))
        self.p1_score_number.setSize(16)
        self.p2_score_text = Text(Point(750,100),"Player 2:")
        self.p2_score_text.setSize(16)
        self.p2_score_number = Text(Point(750,150),str(self.p2_score))
        self.p2_score_number.setSize(16)
        self.scoreboard = [self.p1_score_text,self.p1_score_number,self.p2_score_text,self.p2_score_number]
        
    def click_box(self,click):
        x = click.getX()
        y = click.getY()
        box = 0
        if 100 < x < 300 and 100 < y < 300:
            box = 1
        elif 300 < x < 500 and 100 < y < 300:
            box = 2
        elif 500 < x < 700 and 100 < y < 300:
            box = 3
        elif 100 < x < 300 and 300 < y < 500:
            box = 4
        elif 300 < x < 500 and 300 < y < 500:
            box = 5
        elif 500 < x < 700 and 300 < y < 500:    
            box = 6
        elif 100 < x < 300 and 500 < y < 700:
            box = 7
        elif 300 < x < 500 and 500 < y < 700:
            box = 8
        elif 500 < x < 700 and 500 < y < 700:
            box = 9
        return box    
        
    def place(self,box):
        multx = box%3
        if multx == 0:
            multx = 3
        x = (multx * 200)
        multy = box/3
        if int(multy) != multy:
            multy = int(multy + 1)
        y = multy * 200
        point = Point(x,y)
        if self.turn == 1:
            shape = Circle(point,75)
            shape.setWidth(5)
            shape.draw(win)
        else:
            shape1 = Line(Point(x-75,y-75),Point(x+75,y+75))
            shape1.setWidth(5)
            shape1.draw(win)
            shape2 = Line(Point(x+75,y-75),Point(x-75,y+75))
            shape2.setWidth(5)
            shape2.draw(win)
        
    def player_turn(self):
        self.text_turn.undraw()
        self.text_turn.setText("Player " + str(self.turn) + "'s Turn")
        self.text_turn.draw(self.win)
        click = self.win.getMouse()
        box = self.click_box(click)
        while box == 0:
            click = self.win.getMouse()
            box = self.click_box(click)
        if box not in self.filled:
            self.filled.append(box)
            if self.turn == 1:
                self.p1.append(box)
            else:
                self.p2.append(box)
            self.place(box)
        else:
            while box in self.filled:
                click = self.win.getMouse()
                box = self.click_box(click)
            self.filled.append(box)
            self.place(box)
            if self.turn == 1:
                self.p1.append(box)
            else:
                self.p2.append(box)
            self.place(box)
            
    def check_winner(self, p1, p2, turn):
        if turn == 1:
            if 1 in p1 and 2 in p1 and 3 in p1:
                self.over = True
                self.winner = 1
                return -1
            elif 4 in p1 and 5 in p1 and 6 in p1:
                self.over = True
                self.winner = 1
                return -1
            elif 7 in p1 and 8 in p1 and 9 in p1:
                self.over = True
                self.winner = 1
                return -1
            elif 1 in p1 and 4 in p1 and 7 in p1:
                self.over = True
                self.winner = 1
                return -1
            elif 2 in p1 and 5 in p1 and 8 in p1:
                self.over = True
                self.winner = 1
                return -1
            elif 3 in p1 and 6 in p1 and 9 in p1:
                self.over = True
                self.winner = 1
                return -1
            elif 1 in p1 and 5 in p1 and 9 in p1:
                self.over = True
                self.winner = 1
                return -1
            elif 3 in p1 and 5 in p1 and 7 in p1:
                self.over = True
                self.winner = 1
                return -1
        else:
            if 1 in p2 and 2 in p2 and 3 in p2:
                self.over = True
                self.winner = 2
                return 1
            elif 4 in p2 and 5 in p2 and 6 in p2:
                self.over = True
                self.winner = 2
                return 1
            elif 7 in p2 and 8 in p2 and 9 in p2:
                self.over = True
                self.winner = 2
                return 1
            elif 1 in p2 and 4 in p2 and 7 in p2:
                self.over = True
                self.winner = 2
                return 1
            elif 2 in p2 and 5 in p2 and 8 in p2:
                self.over = True
                self.winner = 2
                return 1
            elif 3 in p2 and 6 in p2 and 9 in p2:
                self.over = True
                self.winner = 2
                return 1
            elif 1 in p2 and 5 in p2 and 9 in p2:
                self.over = True
                self.winner = 2
                return 1
            elif 3 in p2 and 5 in p2 and 7 in p2:
                self.over = True
                self.winner = 2
                return 1
    def tie(self,filled):
        if len(filled) == 9 and self.over == False:
            self.over = True
            self.winner = 0
            return 0
    
    def end_game(self):
        self.text_turn.undraw()
        if self.winner != 0:
            self.text_turn.setText("Player " + str(self.winner) + " wins!")
        else:
            self.text_turn.setText("Cat's Game.")
        self.text_turn.draw(self.win)
        if self.winner == 1:
            self.p1_score += 1
            self.p1_score_number.setText(str(self.p1_score))
        elif self.winner == 2:
            self.p2_score += 1
            self.p2_score_number.setText(str(self.p2_score))
        for item in self.scoreboard:
            item.draw(self.win)
            
    """def computer_choose(self):
        available_moves = []
        moves_to_choose = []
        copy_available_combos = list(self.winning_combos)
        available_combos = list(self.winning_combos)
        opponent_combos = []
        for square in range(1,10):
            if square not in self.filled:
                available_moves.append(square)
        if len(available_moves) == 9:
            return 3
        if 5 in available_moves:
            return 5
        for three in copy_available_combos:
            addedo = False
            addedp = False
            for square in three:
                # adds
                if addedp == False and square in self.p1:
                    available_combos.remove(three)
                    addedp = True
                elif addedo == False and square not in self.p2:
                    opponent_combos.append(three)
                    addedo = True
        if len(available_combos) > 0:
            for three in available_combos:
                open = []
                for square in three:
                    if square not in self.p2:
                        open.append(square)
                if len(open) == 1 and open[0] in available_moves:
                    return open[0]
        
        if len(opponent_combos) > 0:
            for three in opponent_combos:
                open = []
                for square in three:
                    if square not in self.p1:
                        open.append(square)
                if len(open) == 1 and open[0] in available_moves:
                    return open[0]
            for three in opponent_combos:
                for other in opponent_combos:
                    for square in other:
                        if three.count(square) == 1 and other != three and square in available_moves:
                            print(three,other,square)
                            return square
        if len(opponent_combos) > 0 and len(available_combos) > 0:
            for three in available_combos:
                for square in three:
                    for pack in opponent_combos:
                        for single in opponent_combos:
                            if single == square:
                                return single
        return available_moves[0]"""
    
    def minimax(self):
        avail_moves = []
        turn_outs = []
        for x in range(1,10):
            if x not in self.filled:
                avail_moves.append(x)
                turn_outs.append(PossMove(0,Null))
        
        for move in range(len(avail_moves)):
            over = False
            done_moves = list(self.filled)
            comp_moves = list(self.p2)
            opp_moves = list(self.p1)
            new_avail = list(avail_moves)
            new_avail.remove(avail_moves[move])
            comp_moves.append(avail_moves[move])
            turn = 2
            turn_outs[move].depth += 1
            turn_outs[move].score = self.score_move(comp_moves,opp_moves,turn,done_moves)
            if turn_outs[move].score == Null:
                pass;
            
            
    def score_move(self,comp_moves,opp_moves,turn,done_moves):
        if game.check_winner(opp_moves,comp_moves,turn) == 1:
            return 1
        elif game.check_winner(opp_moves,comp_moves,turn) == -1:
            return -1
        elif game.tie(done_moves) == 0:
            return 0
                
            
            
            
        
    def computer_turn(self,choice):
        self.text_turn.undraw()
        self.text_turn.setText("Player " + str(self.turn) + "'s Turn")
        self.text_turn.draw(self.win)
        box = choice
        if box not in self.filled:
            self.filled.append(box)
            self.p2.append(box)
            self.place(box)
        
class PossMove():
    def __init__(self, depth, score):
        self.depth = depth
        self.score = score
        self.turn = 2
        self.next_moves = []
        
                    
        
        
        
        
def start(turn):
    turn = random.randint(1,2)
    turn = 1
    return turn

game = Game()
def play():
    game.turn = start(game.turn)
    while not game.over:
        game.player_turn()
        game.check_winner(game.p1,game.p2,game.turn)
        game.tie(game.filled)
        if game.turn == 1:
            game.turn = 2
        else:
            game.turn = 1
    game.end_game()
play()
win.getMouse()