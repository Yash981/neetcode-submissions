class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unq = set()
        for email in emails:
            local,domain = email.split('@')
            localName = []
            for x in local:
                if x == '.':
                    continue
                elif x == '+':
                    break
                localName.append(x)
            unq.add("".join(localName)+domain)
        return len(set(unq))
