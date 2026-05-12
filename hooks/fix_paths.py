import re

def on_page_markdown(markdown, page, config, files):
    """
    Normalize page URLs to use forward slashes, silencing MkDocs warnings on Windows.
    """
    if hasattr(page, 'url') and page.url and '\\' in page.url:
        page.url = page.url.replace('\\', '/')
    return markdown

def on_page_content(html, page, config, files):
    """
    Hook to fix backslashes in URLs generated on Windows.
    This specifically targets the 'Copy Page' button and other link-like structures.
    """
    site_url = config.get('site_url', '')
    if not site_url:
        return html
    
    site_url = site_url.rstrip('/')
    escaped_site_url = re.escape(site_url)
    
    # This pattern looks for the site_url followed by paths that might contain backslashes
    # inside attributes or script strings.
    pattern = rf'({escaped_site_url}[^`"\'>\s]+)'
    
    def replace_backslashes(match):
        url = match.group(0)
        if '\\' in url:
            return url.replace('\\', '/')
        return url
    
    return re.sub(pattern, replace_backslashes, html)
