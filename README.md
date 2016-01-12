WFE school project
===

Development
---
Starting with: https://orchestrate.io/blog/2014/06/26/build-user-authentication-with-node-js-express-passport-and-orchestrate/

Run
---
```
node server/index.js
```
or use "nodemon" in place of node, which auto restarts server when source codes change

To install nodemon: 
```
sudo npm -g install nodemon
```
AWS
---
To open web port: http://stackoverflow.com/questions/5004159/opening-port-80-ec2-amazon-web-services/10454688#10454688

Login:
ssh -i wfe.pem ubuntu@ec2-52-32-38-91.us-west-2.compute.amazonaws.com

Key is sent via email.

Online access:
http://ec2-52-32-38-91.us-west-2.compute.amazonaws.com:5000/

Issues
---
Fix Ubuntu nodemon "cannot find node" issue: The reason is that node is called nodejs on Ubuntu, just do this to fix:
sudo ln -s /usr/bin/nodejs /usr/local/bin/node

Roadmap
---
1. User auth
2. File access control
3. Role management
4. Files searching
5. Video/Audio playing
6. 2-FA
7. Annotation collaboration


