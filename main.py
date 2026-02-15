import asyncio
import logging
from pathlib import Path
from playwright.async_api import async_playwright

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


async def html_to_pdf(html_content: str, output_path: str = "output.pdf") -> None:
    """
    Create a PDF from an HTML string using Playwright.
    
    Args:
        html_content: HTML content as a string
        output_path: Path where the PDF will be saved (default: output.pdf)
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Set the HTML content
        await page.set_content(html_content)
        
        # Generate PDF
        await page.pdf(path=output_path)
        
        await browser.close()
        logging.info(f"PDF created successfully at: {output_path}")


async def main():
    # Load HTML from file
    html_file = Path("sample.html")
    html_content = html_file.read_text()
    
    # Create outputs directory if it doesn't exist
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    
    # Loop 20 times with 3 second delay between iterations
    for i in range(20):
        output_path = output_dir / f"output_{i+1}.pdf"
        await html_to_pdf(html_content, str(output_path))
        
        if i < 19:  # Don't wait after the last iteration
            await asyncio.sleep(3)


if __name__ == "__main__":
    asyncio.run(main())
