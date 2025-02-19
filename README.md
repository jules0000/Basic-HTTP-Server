# Simple Python HTTP Server

This is a basic HTTP server built using Python's `socket` module. It serves static HTML files from the `htdocs/` directory.

## Features
- Serves static files from the `htdocs/` directory
- Handles requests for `index.html` and other specified files
- Returns `404 Not Found` for missing files
- Includes proper encoding (`utf-8`) to handle text responses
- Implements exception handling to prevent server crashes

## Directory Structure
```
httpserver.py
htdocs/
    index.html
    ipsum.html
```

## Requirements
- Python 3.x

## Installation
1. Clone or download this repository.
2. Ensure you have Python installed (`python --version`).

## Usage
1. **Create the necessary files:**
   - `httpserver.py` (server script)
   - `htdocs/index.html` (default home page)
   - `htdocs/ipsum.html` (additional page)

2. **Run the server:**
   ```sh
   python httpserver.py
   ```

3. **Access the web pages:**
   - Open a browser and visit:
     - `http://localhost:8000/` (to view `index.html`)
     - `http://localhost:8000/ipsum.html` (to view `ipsum.html`)

## File Contents

### `htdocs/index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Simple Web Page</title>
</head>
<body>
    <h1>Welcome!</h1>
    <p>This is the index page.</p>
    <a href="/ipsum.html">Go to Ipsum</a>
</body>
</html>
```

### `htdocs/ipsum.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Ipsum Page</title>
</head>
<body>
<h1>Lorem Ipsum</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
<a href="/">Go Home</a>
</body>
</html>
```

## Key Improvements in This Version
- Uses `os.path.join()` to ensure cross-platform file path compatibility
- Handles file paths safely with `filename.lstrip('/')`
- Checks file existence using `os.path.exists()` before attempting to read
- Implements proper UTF-8 encoding for reading files and sending responses
- Catches general exceptions to prevent server crashes

## Stopping the Server
To stop the server, press `Ctrl + C` in the terminal.


