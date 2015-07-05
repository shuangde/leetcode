class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        width1 = C - A
        height1 = D - B
        width2 = G - E
        height2 = H - F
        totalArea = width1 * height1 + width2 * height2
        leftX = min(A, E)
        rightX = max(C, G)
        upY = max(D, H)
        downY = min(B, F)
        realWidth = rightX - leftX
        realHeight = upY - downY
        if realWidth < width1 + width2 and realHeight < height1 + height2:
            totalArea -= (width1 + width2 - realWidth) * (height1 + height2 - realHeight)
        return totalArea
