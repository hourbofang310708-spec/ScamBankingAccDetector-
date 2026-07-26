import re

def _calculate_url_risk(self, text):
    """Engine 4: Detects malicious URL structural patterns using Regex."""
    # Find any URL in the message
    url_pattern = r'https?://[^\s]+|www\.[^\s]+'
    urls = re.findall(url_pattern, text.lower())
    
    if not urls:
        return 0.0  # No link present
        
    risk_score = 1.0  # Base risk for having a link
    
    for url in urls:
        # Check for suspicious high-risk domain extensions
        if re.search(r'\.(xyz|top|tk|buzz|click|info|net|cc|icu|work)\b', url):
            risk_score += 2.5
            
        # Check for stacked hyphens (ex: aba-bank-login-update)
        if url.count('-') >= 2:
            risk_score += 1.5
            
        # Check if URL uses a raw IP address instead of domain name
        if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url):
            risk_score += 3.0
            
    return risk_score
    # tomorror ready for big data
    
