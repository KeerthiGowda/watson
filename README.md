# Check gh-pages branch for all the files

# Extracting emtions from speech using IBM Watson.

Files:
1. index.html: 
Watson parses the text file from a web page. So, we are dynamically updating a webpage based on the input text provided.

2. html_extract.py:
We are using google voice to convert speech to text. A speech will directly be availabe as text in google docs. We are using this python parser to read the source files of the google doc and extract the text inside the document.

3. json_extract.py:
Once the watson reads the data from the web page, it produces a json output with the emotions embedded into it. We are using this python parser to extract these emotions and dispay it to user.

We had built the watson's interface as per the below guide,
https://github.com/jeancarl/node-red-labs/blob/master/node-red-alchemyapi/node-red-alchemyapi.pdf
