# usage (within dir you want to put files): bash merge.bash <old_dir>
echo git remote add project-a $1
echo git fetch project-a --tags
echo git merge --allow-unrelated-histories project-a/master # or whichever branch you want to merge
echo git remote remove project-a