data = 'X-DSPAM-Confidence: 0.8475 '

fn = data.find(':')

d = data[fn + 1:].strip()

fld = float(d)

rd = round(fld)

print(rd)