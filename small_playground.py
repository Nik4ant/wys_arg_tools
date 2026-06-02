#!/usr/bin/python3
text6 = "fifth test passed; encryption: QUANTUMCHECK7THOUSANDTOTHEPOWEROFSEVEN; DATA(i Ihilfs6kdsRNot A gKBClr Mo;w; t tsEsnVpttzw O xiOhwTtubAaSDRl nesCelnBozuteLi afuiOnenSRa Olsrt iyiL iOTAid snehlw ;HAhoAiElkUi;a neAMh FrsoYatAetrDso:iSuLeeUo mLpt   bT ednfIh YbNt  n vdScpt lsltNee(I;iSeAsr;MULstaeoyM e  Bds ywr wWr too telrLsoyNsUiAiKeen;P yocel stdybteu  aeAnh) nREvNtHIAWLopaNuI eBtlo mnYrL )"
data6 = "i Ihilfs6kdsRNot A gKBClr Mo;w; t tsEsnVpttzw O xiOhwTtubAaSDRl nesCelnBozuteLi afuiOnenSRa Olsrt iyiL iOTAid snehlw ;HAhoAiElkUi;a neAMh FrsoYatAetrDso:iSuLeeUo mLpt   bT ednfIh YbNt  n vdScpt lsltNee(I;iSeAsr;MULstaeoyM e  Bds ywr wWr too telrLsoyNsUiAiKeen;P yocel stdybteu  aeAnh) nREvNtHIAWLopaNuI eBtlo mnYrL "
hint6 = "QUANTUMCHECK7THOUSANDTOTHEPOWEROFSEVEN"


## level 5 set a precident that the password can contain:
## - Any letters in any case (ABC; abc)
## - Digits (123)
def pw_to_key(pw: str) -> list:
	return [
		int(c) if c in "0123456789" else ord(c) - 64
		for c in pw.upper()
	]


## Implementation before level 5
def pw_to_key_old(pw: str) -> list:
	return [ord(c) - 64 for c in pw]


def decrypt(data, key: list):
	index = 0
	result = data[:0]
	key_index = 0
	while data:
		index = (index + key[key_index]) % len(data)
		key_index = (key_index + 1) % len(key)
		result += data[index:index+1]
		data = data[:index] + data[index+1:]
	return result


#text2 = decrypt(data1, [17])

#text3 = decrypt(data2, pw_to_key_old("HUMANSCANTSOLVETHISSOBETTERSTOPHERE"))

#text4 = decrypt(data3, pw_to_key_old("EILLE"))

#text5 = decrypt(data4, pw_to_key_old("XDYOYOY"))

# Step 0) Change 'x' to 'X' 
key5_original = pw_to_key("INTELLIGENCECHECKx7x27".upper())
# Step 1) Apply level 5 key to itself 7 times 
key5 = key5_original.copy()
for _ in range(7):
	key5 = decrypt(key5, key5_original)
# Step 2) Multiply all values by 27
for i in range(len(key5)):
	key5[i] *= 27
text6 = decrypt(data5, key5)
print(text6)
