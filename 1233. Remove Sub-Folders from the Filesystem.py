# solution 1. The set is used to verify that the parent root exists.
class Solution(object):
    def removeSubfolders(self, folder):
        ans = set()
        roots = set()
        
        for path in folder:
            roots.add(path)
            
        for path in folder:
            for i in range(path.count('/')-1, -1, -1):
                subPath = path.rsplit('/', i)[0]
                if subPath in roots:
                    ans.add(subPath)
                    break
                    
        return list(ans)



# solution 2. If sorting is used, it is more efficient because it only needs to be compared with the previous path.
class Solution(object):
    def removeSubfolders(self, folder):
        ans = []
        for path in sorted(folder):
            if not ans or not path.startswith(ans[-1] + '/'):
                ans.append(path)
        return ans
