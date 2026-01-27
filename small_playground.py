#!/usr/bin/python3
data5 = "e;R cNsRtOs;;eE OanYti tieSCC Kd eNTT oxShNsteL emeif;pnlO Ka u TnAtTfdLe UTI;o irf lr EuytwHtte onirruEoLh yeltztl  OHSinpstUwA As L AfiMiNBlwsvnRrpTeEM:tyiIaNNsLUeeOTidPon  p DQt; i6inbADNeNFHAloltA BoieScney MI;EoEn otnoBDkWosB udtL lAs OEn yCogVrHnbsAwt  YrpOed s;oaIilteb7klaauL hsiW loFdUen))YsLOU aE  R tsIAdWes;esA tltopAyhr:bKyt( e hMiePaHAacShiRzSA rSsv umteTswe(Mn fVDNUtUwOtshrACh"
hint5 = "INTELLIGENCECHECKx7x27"

def pw_to_key(pw:str) -> list:
	return [ord(c)-64 for c in pw]
def decrypt(data, key:list):
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
#text3 = decrypt(data2, pw_to_key("HUMANSCANTSOLVETHISSOBETTERSTOPHERE"))
#text4 = decrypt(data3, pw_to_key("EILLE"))
#text5 = decrypt(data4, pw_to_key("XDYOYOY"))
#text6 = ???

