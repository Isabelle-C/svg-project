# svg-project

# What is this?
This is a project with some svg files I created for fun. Hopefully, others would find it useful, too 😊

# To run the auxillary python script
## Follow the steps below
1. Clone the repo
2. Activate env
```bash
poetry shell
```
3. Set up python env
```bash
poetry install
```
4. Run the script
```bash
python ./src/main.py
```

## Additional package information
If you run into errors like I did, you need to install cairo separatebly by run the following commands:
```bash
brew install cairo
ln -s /opt/homebrew/lib/libcairo.2.dylib .
```