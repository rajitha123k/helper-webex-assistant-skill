<!-- __________________________________________________ Basic Repo Steps ___________________________________________________________________________ -->


<!-- # Repo-Template
This is an Internal WXSD Template to be used for GitHub Repos moving forward. Follow the steps below: For extended details, visit https://cisco.sharepoint.com/:w:/r/sites/WXSD-WebexSolutionsDevelopment/Shared%20Documents/Onboarding%20Instructions%20%26%20Guides/Github%20%26%20Security/Github%20Readme%20Detailed%20Standards.docx?d=wba3225a5102341cf874d319d3f334b9b&csf=1&web=1&e=yggr2S 



<!--   Step 1) Name your repository: Repo Name must ALWAYS end with "bot", "embeddedapp: or "macro"
      Examples: "<insert repo name>-bot", "<insert repo name>-embeddedapp", "<insert repo name>macro"

      

~3 words, kebab case, use words to indicate what it does. Visit https://github.com/wxsd-sales/readme-template/blob/master/README.md for more details  
-->

<!--  Step 2) Add One sentence description to your repository: Copy/Paste from Webex Labs Card sentence.
       Example: "Redirect an Auto Attendant caller to an SMS conversation to alleviate Call Queue Agent responsibilities."
-->

<!--  Step 3) Add at least 1 tag to the repo: Indicating if it’s a “bot”, “macro” or “embeddedapp”.       
                 *Additional tags are allowed: should be lowercase and hyphenated for spaces.
                Repo does not use “macros” as a tag (use “macro” instead)
-->

<!--  Step 4) MAKE SURE an MIT license is included in your Repository. If another license is needed, verify with management. This is for legal reasons.
-->

<!--  Step 4) Use following Template to copy/paste your details below in place of the directions 
Make sure you include the "Keep this here" portions (it is for legal, and security infosec reasons).
-->

<!-- _________________________________________________________ Actual Template Starts Below ___________________________________________________________ -->


# Webex Assistant Helper Skill

## Setup

### Prerequisites & Dependencies: 

- For this you need to have pyenv, pyenv-virtualenv, pip, Poetry, webex-skills libraries installed on your machine
- Tested on MacOS


<!-- GETTING STARTED -->

### Installation Steps for Helper Skill:
1. Run
   ```
   webex-skills project init helper
   ```
2. Open main.py file and replace it with the main.py file present in this github repo at /helper-skill/helper/main.py
3. Open .env file and leave lines 1-5 as it is and copy line 7-10 from .env.example file present in this repository at helper-skill/.env.example and paste them in your .env file.
4. You can get your NEWS_API_KEY rom 'https://newsapi.org/account'
5. WEBVIEW_URL is the public URL which you can get after publishing the meetings-app (Meetings app code is attached with this repo)
6. Run
   ```
   webex-skills skills run helper
   ```

### Installation Steps for Meetings App:
1. Run 
   ```
   npm init
   ```
2. Create a file named .env and paste the contents from .env.example file located at meetings-app/.env.example
3. Run 
   ```
   npm start
   ```

Now your skill can be tested on your devices, for this you will need to register the Skill. A step-by-step guide on creating and editing your Skill can be found in the [Webex Assistant Skills Developer Portal Guide]([https://help.webex.com/en-us/article/n01kjh1/New-user-experience-with-RoomOS-11](https://developer.webex.com/docs/api/guides/webex-assistant-skills-guide-developer-portal-guide))
 
## License
<!-- MAKE SURE an MIT license is included in your Repository. If another license is needed, verify with management. This is for legal reasons.--> 

<!-- Keep the following statement -->
All contents are licensed under the MIT license. Please see [license](LICENSE) for details.


## Disclaimer
<!-- Keep the following here -->  
 Everything included is for demo and Proof of Concept purposes only. Use of the site is solely at your own risk. This site may contain links to third party content, which we do not warrant, endorse, or assume liability for. These demos are for Cisco Webex usecases, but are not Official Cisco Webex Branded demos.


## Questions
Please contact the WXSD team at [wxsd@external.cisco.com](mailto:wxsd@external.cisco.com?subject=RepoName) for questions. Or, if you're a Cisco internal employee, reach out to us on the Webex App via our bot (globalexpert@webex.bot). In the "Engagement Type" field, choose the "API/SDK Proof of Concept Integration Development" option to make sure you reach our team. 
