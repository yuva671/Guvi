from requests_html import HTML
with open("C:/Users/yuva0/Desktop/GUVI/marks.html") as html_file:
    source=html_file.read()
    html=HTML(html=source)
print(html.html)
