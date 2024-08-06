# Html Scraper
simple html scraper (+code cleaning)

# Usage
```js
async function fetchHTML(target_url) {
    try {
        const response = await fetch(`https://html-scraper.vercel.app/scrape?url=${target_url}`);
        const html = await response.text();
        return html
    } catch (error) {
        return `Error: ${error.message}`;
    }
}
let result = await fetchHTML('https://naver.me/GHvErx98');
console.log(result)
```
