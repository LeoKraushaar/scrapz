
if [ $# -eq 0 ]; then
	message="backup"
else
	message=$1
fi


git add .
git commit -m "$message"
git push origin leo