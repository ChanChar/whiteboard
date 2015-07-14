import requests
r = requests.get('https://api.clever.com/v1.1/sections/530e5979049e75a9262d0af2/students', headers={'Authorization':'Bearer DEMO_TOKEN'})
r.status_code
r.text
