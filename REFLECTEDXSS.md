# Reflected XSS

#### Step 1:

* Click `Contact Us` icon
* Enter a genuine value

   ![Reflected Based](img/reflected_xss_1.png)


* It will redirect into a information page
    
    ![Reflected Based](img/reflected_xss_2.png)

* Now we can Enter a `Reflected XSS` payload in the url header
    
    ![Reflected Based](img/reflected_xss_4.png)

```commandline
<script > alert(document.cookie)</script >
```

* Once you enter the payload 

    ![Reflected Based](img/reflected_xss_3.png)
