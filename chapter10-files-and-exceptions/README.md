# Chapter 10 - Files and Exceptions

The call to `open()` has two arguments. The first argument is the name of the file we want to open. The second argument, `'w'`, tells Python that we want to open the file in _write mode_. You can open a file in _read mode_ ('r'), _write mode_ ('w'), _ append mode_ ('a'), or a mode that allows you to read and write to the file ('r+'). If you omit the mode argument, Python opens the file in read-only mode by default.

The `open()` function automatically creates the file you’re writing to if it doesn’t already exist. However, be careful opening a file in write mode ('w') because if the file does exist, Python will erase the contents of the file
before returning the file object.

**Note:**: Python can only write strings to a text file. If you want to store numerical data in a text file, you'll have to convert the data to string format first using the `str()` function.