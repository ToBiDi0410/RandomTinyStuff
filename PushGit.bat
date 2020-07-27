@echo off
set /p title="Enter Commit Title: "
set /p branch="Enter Branch: "
git branch %branch%
git add -A
git commit -m "%title%"
git push -u origin master