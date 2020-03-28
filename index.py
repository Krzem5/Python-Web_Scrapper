from PIL import Image
import io
import json
import re
import urllib.request



IMG_REGEX=r"\"(https://preview\.redd\.it/[^\"]+)\""
ID_REGEX=r"\"postIds\": \[([^\]]+)\]"



URL="https://gateway.reddit.com/desktopapi/v1/subreddits/Faces"



def scrap(URL,i=1,MAX=50):
	def c(s):
		n=""
		for k in s:
			if (k in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890[]{}:,\""):
				n+=k
		return n
	req=urllib.request.Request(url=URL,headers={"User-Agent":"windows:face_web_scrapper:v1.0.2 by Krzem"})
	handler=urllib.request.urlopen(req)
	s=str(handler.read())[2:-1]
	l=None
	for m in re.finditer(IMG_REGEX,s,re.MULTILINE):
		n=m.groups(1)[0]
		if ("?width=" not in n):
			req=urllib.request.Request(url=l,headers={"User-Agent":"windows:face_web_scrapper:v1.0.2 by Krzem"})
			stream=io.BytesIO(urllib.request.urlopen(req).read())
			Image.open(stream).save("./data/"+str(i)+".png")
			i+=1
			if (i>MAX):
				return
		else:
			l=n
	scrap(URL+"?after="+json.loads(c(s))["token"],i=i,MAX=MAX)



scrap(URL,MAX=30)