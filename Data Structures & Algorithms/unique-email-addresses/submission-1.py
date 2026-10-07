class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        cleaned = set()
        for email in emails:
            localName,domainName = email.split("@")
            localName = localName.replace(".","")
            localName = localName.split("+")[0]
            # localName = temp[0]
            email = localName + domainName
            cleaned.add((localName,domainName))
        return len(cleaned)
