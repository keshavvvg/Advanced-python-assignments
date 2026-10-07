import re

# Sample text containing various email patterns
sample_text = """
Contact us at support@example.com or sales.team@company.org.
You can also reach out to john.doe123@my-domain.co.uk.
Invalid addresses like user@, @domain.com, or test@site should be ignored.
"""

email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

# Find all matching emails in the text
found_emails = re.findall(email_pattern, sample_text)

print("Found Email Addresses:")
for email in found_emails:
    print(f"- {email}")



#OUTPUT:

'''
Found Email Addresses:
- support@example.com
- sales.team@company.org
- john.doe123@my-domain.co.uk
'''
