# Html Scraper
simple html scraper (+code cleaning)

# Usage
```js
async function fetchHTML() {
    try {
        const response = await fetch(`https://html-scraper.vercel.app/scrape?url=${target_url}`);
        const html = await response.text();
        console.log(html)
    } catch (error) {
        console.log(`Error: ${error.message}`);
    }
}
fetchHTML();
```
