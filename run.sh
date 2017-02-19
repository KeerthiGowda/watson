

while :
do
	echo "Press [CTRL+C] to stop.."
	git checkout gh-pages --quiet
	python3 html_extract.py
	git add index.html
	git commit -m "New commit" -q
	git push --quiet
    clear
	python3 json_extract.py
	sleep 5
done

