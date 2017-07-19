from random import randint
from BaseAI import BaseAI
from Displayer  import Displayer


class PlayerAI(BaseAI):
    def __init__(self):
        self.direction = -1

    def getNewTile(self):
        if randint(0, 99) < 100 * .9:
            return 2
        else:
            return 4

    def hueristic(self, grid):
        cell = grid.getAvailableCells()
        maxTiles = self.getMaxTiles(grid)
        maxSum = sum(maxTiles) - maxTiles[4]
        maxCorner = self.isMaxInCorner(grid)
        evalScore = 7500 * maxCorner + len(cell) * 5000 + maxSum * 0.8 + maxTiles[4] * 2
        return (evalScore)

    def isMaxInCorner(self,grid):
        maxTileInGrid = 3
        maxLocation = [-1,-1]
        for x in xrange(grid.size):
            for y in xrange(grid.size):
                if grid.map[x][y] > maxTileInGrid:
                    maxTileInGrid = grid.map[x][y]
                    maxLocation = [x,y]

        if maxLocation == [0,0] or maxLocation == [3,0] or maxLocation == [0,3] or maxLocation == [3,3]:
            return 1
        else:
            return 0

    def getMaxTiles(self, grid):
        maxTile = 0
        dist = 0
        maxTiles = [0, 0, 0, 0]
        for x in xrange(grid.size):
            for y in xrange(grid.size):
                dist = dist + (x - y) * grid.map[x][y] * 3.0
                maxTile = grid.map[x][y]
                if maxTile > maxTiles[0]:
                    maxTiles[0] = maxTile
                    maxTiles.sort(cmp=None, key=None, reverse=False)
        maxTiles.append(dist)
        return maxTiles


    def getMove(self, grid):
        moves = grid.getAvailableMoves()
        rv = self.alpha_beta(grid, 4, -float('inf'), float('inf'),True)
        if grid.canMove([rv[0]]):
            return rv[0]
        else:
            return moves[0]


    def alpha_beta(self, grid, depth, alpha, beta, maxPlayer):
        """

        :param grid:
        :param depth: how deep to search
        :param alpha:
        :param beta:
        :param maxPlayer: true if moving player
        :return: list [ direction , alpha/beta]
        """
        if depth == 0:
            h = self.hueristic(grid)
            return [-1, h]


        if maxPlayer == True:
            moves = grid.getAvailableMoves()
            #print moves
            if moves == []:
                return [-1,self.hueristic(grid)]
            maxUtility = -float('inf')
            self.direction = -1
            for child in moves:
                newgrid = grid.clone()
                newgrid.move(child)
                r = self.alpha_beta(newgrid, depth - 1, alpha, beta, False)
                utility = r[1]
                if utility > maxUtility:
                    self.direction = child
                    maxUtility = utility
                if maxUtility >= beta:
                    break

                if maxUtility > alpha:
                    alpha = maxUtility
            return [self.direction, maxUtility]

        else: # COMPUTER / MIN PLAYER
            avail = grid.getAvailableCells()

            if avail == []:
                return [-1,self.hueristic(grid)]
            minUtility = float('inf')
            for child in avail:
                newgrid = grid.clone()
                newgrid.map[child[0]][child[1]] = self.getNewTile()
                r = self.alpha_beta(newgrid, depth - 1, alpha, beta, True)
                utility = min(minUtility,r[1])
                if utility < minUtility:
                    minUtility = utility
                if minUtility <= alpha:
                    break
                if minUtility < beta:
                    beta = minUtility
            return [-1, minUtility]

