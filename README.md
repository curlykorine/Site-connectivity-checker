# Site connectivity checker
Desktop application for checking site connection in a background mode by sending ICMP messages.

## Problem and solution
Usually, when people need some site to interact with and it crashes, they update the page many times to check whether the site is available or not. Instead of this, we propose the desktop app which will ping the site every minute by sending ICMP messages in a background mode. When the site becomes available the app will send notification with site link to the user.

## Prerequirements
* Python3
* Python libraries from [requirements.txt](https://github.com/curlykorine/Site-connectivity-checker/blob/main/requirements.txt)

## Getting started guide
1. From [Site-connectivity-checker](https://github.com/curlykorine/Site-connectivity-checker) repository download all the documents to your local project
2. Write in command line/terminal from the project directory `pip install -r requirements.txt` to install all the required libraries 
3. From the project directory write in command line/terminal `python3 ./main.py` or `python main.py` to run the app

## Glossary
Name                      | Description
--------------------------|--------------------------------------------------------------------
Ping                      | an ICMP message to the site server
Pinger/Checker            | a program that sends ICMP messages to the site server
Notification              | a short window that activates when the site is available
Site links storage        | a local database to store the site links
Checklist/Data            | a window with site links storage 
Request processing system | a system that gets request from the user and depending on that sends this request to the data storage or to the pinger

## How to use
1. After starting app execution you should add sites, which you often visit, to the checklist.
2. When some of these sites crashes start pinging it.
3. As soon as the site is available again the app will stop pinging it and send you notification with a link.
4. If the app is pinging the site, but you are not interested in this site anymore, just stop pinging.
5. You can also see the checklist of sites, add new sites and delete old ones whenever you want.
6. Stop app execution if there is no need in that.

## Features
* `add <site link>` to add the site to checklist of sites
* `delete <site link>` to delete the site from checklist of sites
* `on <site link>` to start pinging the site untill it will be available
* `off <site link>` to stop pinging the site if you are not interested anymore in this site
* `checklist` to see the checklist of sites
* `quit` to stop the app

## Architecture decisions
We decided to use [observer pattern](https://en.wikipedia.org/wiki/Observer_pattern) as it perfectly suits to our solution: an object (pinger) maintains dependent (user), called observer, and  automatically notifies it about any changes (sites' availability) using special methods (sending notifications).

![image](https://user-images.githubusercontent.com/69847727/134787343-0310f0ba-1a09-4f75-8a11-3a44077a3b41.png)
![image](https://user-images.githubusercontent.com/69847727/134787351-17ae8031-4ecf-41ee-b876-662e076e5a03.png)
![image](https://user-images.githubusercontent.com/69847727/134787464-a5ae3cf2-5a77-45f7-9645-c0a86edffdb6.png)

## Authors
Evgeniy Lutanin, Karina Singatullina,  
Innopolis University, AAI
