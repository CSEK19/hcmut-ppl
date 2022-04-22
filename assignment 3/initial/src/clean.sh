echo "Cleaning solutions/"
rm -rf "./test/solutions/"

echo "Cleaning testcases/"
rm -rf "./test/testcases/"

mkdir "./test/solutions"
mkdir "./test/testcases"

cd ./test/solutions
touch 1.txt

cd ../..

cd ./test/testcases
touch 1.txt

echo "Clean successfully"