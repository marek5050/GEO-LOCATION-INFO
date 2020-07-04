cat ./README.t.md > ./README.md
echo "Last updated: " `date` >> ./README.md
echo "" >> README.md
echo "*"`ls ./data | grep csv`"*" >> ./README.md
echo "\`\`\`" >> ./README.md
head ./data/*.csv >> ./README.md
echo "\`\`\`" >> ./README.md
