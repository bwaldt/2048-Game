from random import randint
from BaseAI import BaseAI
from Displayer  import Displayer


class PlayerAI(BaseAI):
    def _init_(self):
        self.direction = -1

    def getNewTile(self):
        if randint(0, 99) < 100 * .9:
            return 2
        else:
            return 4

    def getMove(self, grid):
        moves = grid.getAvailableMoves()
        rv = self.alpha_beta(grid, 4, -999, 999,True)
        return moves[randint(0, len(moves) - 1)] if moves else None

    def alpha_beta(self, grid, depth, alpha, beta, maxPlayer):
        print 'Depth: ', depth
        if depth == 0:
            print grid.getAvailableCells()
            print 'Hueristic: ', h
            return (grid, h)

        moves = grid.getAvailableMoves()

        if maxPlayer == True:

            if moves == []:
                print "No moves"

            maxChild, maxUtility = 0, alpha


            for child in moves:
                newgrid = grid.clone()
                newgrid.move(child)
                compgrid, utility = self.alpha_beta(newgrid, depth - 1, alpha, beta, False)

                print '$$$$$$$$$$$$$$$$$$$', utility

                if utility > maxUtility:
                    maxChild, maxUtility = compgrid, utility

                if maxUtility > beta:
                    break

                if maxUtility > alpha:
                    alpha = maxUtility
                    print 'Alpha: ', alpha

            return (maxChild, maxUtility)

        else: # COMPUTER / MIN PLAYER

            if moves == []:
                print "No moves"

            minChild, minUtility = 0,beta

            for child in moves:
                newgrid = grid.clone()
                newgrid.move(child)
                usergrid, utility = self.alpha_beta(newgrid, depth - 1, alpha, beta, True)

                if utility < minUtility:
                    minChild, minUtility = usergrid, utility

                if minUtility < alpha:
                    break

                if minUtility < beta:
                    beta = minUtility
                    print 'Beta:', beta

            return (minChild, minUtility)

