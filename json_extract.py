from urllib.request import urlopen
import json

url = 'http://danalyze.mybluemix.net/story?format=json&url=https://keerthigowda.github.io/watson/' # write the url here

usock = urlopen(url)
#print("URL OPENED")
data = usock.read()
#print("Reading data")
usock.close()
fp = open('json.txt','w')
fp.write(data.decode())
fp.close()

fp = open("json.txt", 'r')
for word in fp:
    json_dict = json.loads(word)
    
    print("It is currently = " + str(json_dict["doc-sentiment"]["type"]))
    if(json_dict["doc-sentiment"]["type"] != "neutral"):
        print(json_dict["doc-sentiment"]["score"])

    emotion_list = sorted(json_dict["doc-emotion"], key=json_dict["doc-emotion"].__getitem__)
    print("Your patner's current feeling : " + str(emotion_list[-1]))
	#if(
    break
fp.close()
