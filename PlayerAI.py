from random import randint
from BaseAI import BaseAI

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
        return moves[randint(0, len(moves) - 2)] if moves else None

    def alpha_beta_max(self, grid, depth, alpha, beta):
        if depth == 0:
            h = 16 - grid.getAvailableCells()
            return (grid, h)

        moves = grid.getAvailableMoves()

        if moves == []:
            print "No moves"

        for child in moves:
            newgrid = grid.clone()
            newgrid.move(child)
            compgrid, utility = self.alpha_beta_min(newgrid, depth - 1, alpha, beta)

            if utility > maxUtility:
                (maxChild, maxUtility) = (compgrid, utility)

            if maxUtiliy > beta:
                break

            if maxUtiliy > alpha:
                alpha = maxUtility

        return (maxChild, maxUtility)


    def alpha_beta_min(self, grid, depth, apha, beta):
        if depth == 0:
            h = 16 - grid.getAvailableCells()
            return (grid, h)

        moves = grid.getAvailableMoves()

        if moves == []:
            print "No moves"


        for child in moves:
            newgrid = grid.clone()
            newgrid.move(child)
            usergrid, utility = self.alpha_beta_max(newgrid, depth - 1, alpha, beta)

            if utility < minUtility:
                (minChild, minUtility) = (usergrid, utility)

            if minUtiliy < alpha:
                break

            if minUtiliy < beta:
                beta = minUtility

        return (minChild, minUtility)