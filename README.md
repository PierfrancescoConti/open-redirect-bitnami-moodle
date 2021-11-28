# open-redirect-bitnami-moodle
Simple open-redirect check on Bitnami Moodle 
<br><br>
### Usage
```
        ./open-redirect-bitnami-moodle.py <URL/Domain/IP>
```
Examples:
```
        ->  ./open-redirect-bitnami-moodle.py 192.168.161.178
        ->  ./open-redirect-bitnami-moodle.py mymoodle.domain.com
        ->  ./open-redirect-bitnami-moodle.py http://mymoodle.domain.com/
```
<br><br>
### PoC
If the script returns "Vulnerable!", then it is possible to redirect the connection to an arbitrary host as shown in the next Figure.
<br><br>

![Screenshot](PoC.png) <br><br>

<br>
<hr>

### badmoodle
This is a badmoodle module, take a look at my friend's repo!<br>
https://github.com/cyberaz0r/badmoodle
