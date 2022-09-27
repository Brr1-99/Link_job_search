import webbrowser

jobs = ["first_job", "second_job"]

def job_url(keywords: str) -> str: 
    keywords.replace(' ', '%20')
    return f"https://www.linkedin.com/jobs/search/?&distance=25&f_TPR=r86400&geoId=105646813&keywords={keywords}&sortBy=DD"

chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

def main() -> None:
    for job in jobs:
        webbrowser.get(chrome_path).open(job_url(job))

if __name__ == "__main__":
    main()