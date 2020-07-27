@echo off
set /p title="Enter Commit Title: "

git add -A
git commit -m "%title%"
git push -u origin master