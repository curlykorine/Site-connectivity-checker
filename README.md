# Site connectivity checker
Command line application for checking site connection in a background mode by sending ICMP messages.

## Problem and solution
Usually, when people need some site to interact with and it crashes, they update the page many times to check whether the site is available or not. Instead of this, we propose the command line app which will ping the site every minute by sending ICMP messages in a background mode. When the site becomes available the app will send notification with site link to the user.

## Prerequirements
* Windows OS
* Python3
* Python libraries from [requirements.txt](https://github.com/curlykorine/Site-connectivity-checker/blob/main/requirements.txt)

## Getting started guide
1. From [Site-connectivity-checker](https://github.com/curlykorine/Site-connectivity-checker) repository download all the documents to your local project
2. From the project directory write in command line/terminal `pip install -r requirements.txt` to install all the required libraries 
3. From the project directory write in command line/terminal `python3 ./main.py` or `python main.py` to run the app

## Glossary
Name                      | Description
--------------------------|--------------------------------------------------------------------
Ping                      | an ICMP message to the site server
Pinger/Checker            | a program that sends ICMP messages to the site server
Notification              | a short window that activates when the site is available
Sitelist/Data             | a local database to store all the site links
Checklist                 | a pinging at the moment site links storage 
Request processing system | a system that gets request from the user and depending on that sends this request to the data storage or to the pinger

## How to use
1. After starting app execution you should add sites, which you often visit, to the sitelist.
2. When some of these sites crashes - start pinging it, also this site will be added to the checklist automatically.
3. As soon as the site is available again, the app will stop pinging it, send you notification with a link and delete this site from the checklist.
4. If the app is pinging the site, but you are not interested in that site anymore, just stop pinging.
5. You can also see the sitelist, the checklist, add new sites and delete old ones whenever you want.
6. Stop app execution if there is no need in that.

## Features
* `add <site link>` to add the site to sitelist
* `delete <site link>` to delete the site from sitelist
* `on <site link>` to start pinging the site untill it will be available
* `off <site link>` to stop pinging the site if you are not interested anymore in this site
* `checklist` to see the list of sites that pinger is pinging now
* `sitelist` to see the list of all sites added
* `quit` to stop the app

## Demo
([![Watch the video]](https://youtu.be/vt5fpE0bzSY))

## Design decisions
We decided to use [observer pattern](https://en.wikipedia.org/wiki/Observer_pattern) as it perfectly suits to our solution: an object (pinger) maintains dependent (user), called observer, and  automatically notifies it about any changes (sites' availability) using special methods (sending notifications).

![image](https://user-images.githubusercontent.com/69847727/136710676-d5fbc0ea-13d3-4f53-9d64-9a214d0b40e4.png)

* **Single Responsibility Principle** - the source code consists of 2 classes: one of them is a pinger, which is responsible for pinging sites. Another class is responsible for the client side, where actions with the database take place and notifications are called. In our case, we have implemented a client under WindowClient.py.
* **Open-closed Principle** - the pinger contains a list of users, which are classes inherited from Client. Thus, you can create a class that inherits Client for another OS without changing the Pinger class.
* **Liskov substitution principle** - functions working with base classes have the ability to use objects of derived classes.
* **Interface Segregation Principle** - interfaces contain only necessary for pinging and managing data methods.
* **Dependency Inversion Principle** - the relationship between classes is based on dependencies on abstractions, not on concrete implemented classes.

![image](https://user-images.githubusercontent.com/69847727/134787351-17ae8031-4ecf-41ee-b876-662e076e5a03.png)

## Architecture decisions
Here static and dynamic view diagrams of Site connectivity checker project.

![image](https://user-images.githubusercontent.com/69847727/136712455-114d9563-2aaf-4b2a-8f51-eb3a5a9a27c7.png)
![image](https://user-images.githubusercontent.com/69847727/134787343-0310f0ba-1a09-4f75-8a11-3a44077a3b41.png)

## Code quality


## Authors
Evgeniy Lutanin, Karina Singatullina,  
Innopolis University, AAI
