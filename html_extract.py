from urllib.request import urlopen

url = 'https://docs.google.com/document/d/19tmr6E2o_fi5PY8hg5pA-DmFxpGlbtVN4_zhqv33gTM/' # write the url here

usock = urlopen(url)
#print("URL OPENED")
data = usock.read()
#print("Reading data")
usock.close()
fp = open('log_html.txt','w')
fp.write(data.decode())
fp.close()
fp = open('log_html.txt', 'r')
count = 0
html_text = ""
for word in fp:
    #print("index = ")
    #init_value = word.find("Initialization")
    #print(init_value)
    #print(word)	
    init_value = word.find("Initialization")
    if(init_value != -1):
        count = count + 1
    #print(word)
    	
    if(count >= 2):	
        #print(init_value)

        final_value = word.find("ibi", init_value)
        #print(final_value)
        html_text = word[init_value:final_value - 1]
        #print(html_text)
        new_fp = open('output_html.txt', 'w')
        new_fp.write(html_text)
        new_fp.close()
        break
    
fp.close()

new_fp = open('output_html.txt', 'r')
index_fp = open('index_template.html', 'r')
output_fp = open('index.html', 'w')
#print("second stage")
for word_index in index_fp:
    
    if("<body>" not in word_index):
        output_fp.write(word_index)
        #print("word = ")
        #print(word_index)
    else:
        #print("body found")
        
        output_fp.write("<body>")
        for temp_word in new_fp:
            output_fp.write(temp_word)
        #print("context written")
        output_fp.write("</body>")
        output_fp.write("</html>")
        
        output_fp.close()
        break
    
new_fp.close()
index_fp.close()

    



            


