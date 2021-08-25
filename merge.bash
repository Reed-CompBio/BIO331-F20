# usage (within dir you want to put files): bash merge.bash <old_dir>
git remote add project-a $1
git fetch project-a --tags
git merge --allow-unrelated-histories project-a/master # or whichever branch you want to merge
git remote remove project-a