@ECHO OFF
# Made By Nadav Chen # 
# cd to Where Jenkins client is located in your PC
cd C:\Users\[PATH]\jen
# open the jenkins web client with your default browser [LINK: Jenkins URL] 
start "" http://localhost:8081/
java -jar .\jenkins.war 
PAUSE
# Made By Nadav Chen # 