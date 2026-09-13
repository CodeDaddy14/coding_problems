class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])  # path compression
                return self.parent[x]

            def union(self, x, y):
                rootX, rootY = self.find(x), self.find(y)
                if rootX == rootY:
                    return
                self.parent[rootY] = rootX

        email_to_idx = {}  
        email_to_name = {}  
        idx = 0
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_idx:
                    email_to_idx[email] = idx
                    idx += 1
                email_to_name[email] = name

        dsu = DSU(idx)
        for account in accounts:
            first_mail = email_to_idx[account[1]]

            # union all emails in this row with the first email
            for email in account[2:]:
                dsu.union(first_mail, email_to_idx[email])

        #finding root to each email
        root_to_mail = {}
        for email, i in email_to_idx.items():
            root = dsu.find(i)
            root_to_mail.setdefault(root, []).append(email)

        # build result
        result = []
        for root, emails in root_to_mail.items():
            name = email_to_name[emails[0]]
            result.append([name] + sorted(emails))
        return result