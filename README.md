# JobSearch Automation
<h1 align="center">
  <br>
<img src="/images/img.png" width="160">
</h1>

<h4 align="center">Code to automate the collection of LinkedIn's job listings.</h4>

<br/>

---
## Disclaimer

- Running this code requires username and password information for LinkedIn, I am not responsible for the security of your information.
- Use this code at your own risk
- LinkedIn's HTML may change from the time of this writing

---

### Python Environment

- Pyenv 1.2.18
- Python 3.74
- <a href="https://github.com/bryanee23/jobsearch_public/blob/master/system%20files/requirements.txt"> Requirements List </a>

___

### Instructions

- Install all requirements
- Configure webdriver <a href="https://chromedriver.chromium.org/getting-started">Link to tutorial</a>
- Create config.txt file in 'system files' folder w/ username and password
- Get the number of pages
- Copy and past target URL
<h1 align="center">
  <br>
<img src="/images/url.gif">
</h1>
<br>
- Paste URL and pages into TARGET_PAGE object in directory.py
<br>
<h1 align="center">
  <br>
<img src="/images/directory.gif">
</h1>
<br>
- Run get_job_listing.py in the terminal
- Place mouse on the left margin of the page to prevent unwanted clicks


## Notes
- Original repo and working docs is on a private repo to keep my info secure
___

### Demo
<h1 align="center">
  <br>
<img src="/images/jobsearch_public.gif">
</h1>
- Video speed setting is on cheetah on coffee mode to keep file size small
- Run time of algorithm = ~26 mins
- <a href="https://drive.google.com/file/d/1Mtl1elcg69WEoGcxJhD6v-uYRDoWORDa/view?usp=sharing">Demo Video</a>
<br/>