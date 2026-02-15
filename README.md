# Playwright Zombie Check

A Python utility that converts HTML strings to PDF files using Playwright. This project generates multiple PDFs in batch with configurable delays between iterations.

## Features

- Convert HTML content to PDF using Playwright's Chromium browser
- Load HTML from external files
- Batch PDF generation with configurable delays
- Automatic output directory creation
- Structured logging with timestamps

## Installation

1. Install dependencies:
```bash
uv add playwright
```

2. Install Playwright browsers:
```bash
uv run playwright install
```

## Usage

Run the script:
```bash
uv run main.py
```

The script will:
1. Load HTML from `sample.html`
2. Generate 20 PDF files in the `outputs/` directory
3. Wait 3 seconds between each PDF generation
4. Log progress to the console

## Project Structure

- `main.py` - Main script with async PDF generation logic
- `sample.html` - HTML template to convert to PDF
- `outputs/` - Directory where generated PDFs are saved (created automatically)

## Configuration

To modify the number of iterations or delay time, edit the `main()` function in `main.py`:

```python
for i in range(20):  # Change 20 to desired number of iterations
    # ...
    await asyncio.sleep(3)  # Change 3 to desired delay in seconds
```

To use custom HTML content, either:
- Modify `sample.html` directly
- Call `html_to_pdf()` with custom HTML content

## Logging

The application uses Python's `logging` module with the following format:
```
TIMESTAMP - LEVEL - MESSAGE
```

Example output:
```
2026-02-15 10:30:45,123 - INFO - PDF created successfully at: outputs/output_1.pdf
```

## Docker

A Dockerfile is included to containerize the application:

```bash
docker buildx build -t playwright-zombie-check .
docker run --name zombie-check playwright-zombie-check
```

### Building for Multiple Platforms

To build for multiple platforms (amd64, arm64):

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t playwright-zombie-check:latest --push .
```

### ⚠️ Zombie Processes Warning

When running this code in a Docker container, **zombie processes** (`headless_shell` processes) may accumulate. This occurs because:

1. Playwright launches Chromium browser processes
2. In Docker containers without proper init systems, child processes may become zombies
3. Multiple iterations without proper cleanup can lead to process accumulation