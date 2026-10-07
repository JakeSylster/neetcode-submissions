class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        cleaned = []
        for email in emails:
            localName = email.split("@")
            localName[0] = localName[0].replace(".","")
            temp = localName[0].split("+")
            localName[0] = temp[0]
            email = localName[0] + localName[1]
            if email in cleaned:
                continue
            cleaned.append(email)
        return len(cleaned)
