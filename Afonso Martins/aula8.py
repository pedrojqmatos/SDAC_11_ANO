str = " X-DSPAM-Confidence: 0.8475 "
colon_position = str.find(':')
substring_after_colon = str[colon_position + 1:].strip()
assurance_Worth = float(substring_after_colon)
print(assurance_Worth)
