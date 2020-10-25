@ECHO OFF
# cd to Where Jenkins client is located in your PC
cd C:\Users\Nadav Chen\Documents\jen
# open the jenkins web client with your default browser [LINK: Jenkins URL] 
start "" http://localhost:8080/
java -jar jenkins.war
PAUSE
