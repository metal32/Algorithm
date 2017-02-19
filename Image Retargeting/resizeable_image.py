import imagematrix
import sys
class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self):
        energy={}
        # Calculate each energy once
        for i in range(self.width):
            for j in range(self.height):
                energy[(i,j)]=self.energy(i,j)

        dp={}
        for i in range(self.width):
            dp[(i,0)]=energy[(i,0)]

        backpointer={}
        for j in range(1,self.height):
            for i in range(self.width):
                # Moving directly down
                dp[(i,j)] = energy[(i,j)] + dp[(i,j-1)]
                backpointer[(i,j)] = 0
                # Movind Down-Left, so we have to check wether the width pixel is not on the edge
                if i!=0:
                    if dp[(i,j)]>energy[(i,j)]+dp[(i-1,j-1)]:
                        dp[(i,j)] = energy[(i,j)] + dp[(i-1,j-1)]
                        backpointer[(i,j)] = -1
                # Moving Down-Right, we have to make sure that our width pixel is not on the right edge
                if i != self.width-1:
                    if dp[i,j] > energy[i,j] + dp[i+1,j-1]:
                        dp[i,j] = energy[i,j] + dp[i+1,j-1]
                        backpointer[(i,j)] = 1

        #Find best pixel in bottom row
        best_value=sys.maxint
        index=None
        for i in range(self.width):
            if dp[(i,self.height-1)] < best_value:
                best_value = dp[(i,self.height-1)]
                index = i

        # Follow backpointers back to up
        seam=[]
        for j in range(self.height-1,0,-1):
            seam.append((index,j))
            index=index+backpointer[(index,j)]
        seam.append((index,0))
        return seam

    def remove_best_seam(self):
        self.remove_seam(self.best_seam())
