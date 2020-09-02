def isValidInstall(x, y, pillarBoard, beamBoard, isBeam, n):
    if not isBeam:
        return (0 <= x <= n and 0 <= y < n and (pillarBoard[x][y-1] or beamBoard[x-1][y] or beamBoard[x][y])) or y == 0
    elif isBeam:
        return (0 <= x < n and 0 <= y <= n and (pillarBoard[x][y-1] or (beamBoard[x-1][y] and beamBoard[x+1][y]) or pillarBoard[x+1][y-1]))
    return False

def removeBuild(x, y, pillarBoard, beamBoard, isBeam, n, ans):
    if not isBeam:
        if [x, y, isBeam] in ans:
            ans.remove([x, y, isBeam])
            pillarBoard[x][y] = 0
            for dx, dy, d_isBeam in ans:
                if not isValidInstall(dx, dy, pillarBoard, beamBoard, d_isBeam, n):
                    pillarBoard[x][y] = 1
                    ans.append([x, y, isBeam])
                    return
    elif isBeam:
        if [x, y, isBeam] in ans:
            ans.remove([x, y, isBeam])
            beamBoard[x][y] = 0
            for dx, dy, d_isBeam in ans:
                if not isValidInstall(dx, dy, pillarBoard, beamBoard, d_isBeam, n):
                    beamBoard[x][y] = 1
                    ans.append([x, y, isBeam])
                    return

def solution(n, build_frame):
    ans = []
    pillarBoard = [[0] * (n+1) for _ in range(n+1)]
    beamBoard = [[0] * (n+1) for _ in range(n+1)]

    for x, y, isBeam, isInstall in build_frame:
        if isInstall:
            if not isBeam and isValidInstall(x, y, pillarBoard, beamBoard, isBeam, n):
                ans.append([x, y, 0])
                pillarBoard[x][y] = 1
            elif isBeam and isValidInstall(x, y, pillarBoard, beamBoard, isBeam, n):
                ans.append([x, y, 1])
                beamBoard[x][y] = 1
        else:
            removeBuild(x, y, pillarBoard, beamBoard, isBeam, n, ans)
    return sorted(ans)
