

while :
do
	git checkout gh-pages --quiet
	python3 html_extract.py
	git add index.html
	git commit -m "New commit" -q > temp
	git push --quiet
	python3 json_extract.py
	sleep 1
	echo "\n\n"
done

