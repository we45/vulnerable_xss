# DOM Based XSS

#### Step 1:

* Click `Todo` icon
* Enter a genuine value

   ![DOM Based](img/dom_based_xss_1.png)

* Now we can Enter a `DOM XSS` payload

```commandline
<a onmouseover=alert(document.cookie)>click me!</a>
```

* Then mouseover on the `click me!` text

    ![DOM Based](img/dom_based_xss_2.png)
