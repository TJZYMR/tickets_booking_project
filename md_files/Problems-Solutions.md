# Problems:=>

1. **How to add all .pyc files in gitignore?**
     =First, make sure that you don't have any changes to commit;
        
    1.Edit or create your .gitignore and put the follow code:
            
            *.log

            *.pot

            *.pyc

            */*/*/__pycache__/

            */*/__pycache__/

            */__pycache__/

    2.Save -> git add . -> git commit
    3.'Clean Git Hub Cache' for your repo:
        git rm -rf --cached .
        git add .
        git commit -m "message"
    Commit and it's done!
    
    
    > **[IMPORTANT]**
    > git rm -rf --cached .This command cleans cached files and that's why after that line we need to stage all the file.This is done when you alrady added .pyc filed to staging area then we need to remove those files from this area and that's when removing cache command is used.


2. **Adding env file to gitignore**
    =>.env in gitignore first and then these steps
        a. git rm -f .env
        b. git add .  
        c. git commit -m "remove .env file from git"
        d. git push
3. **Should JWT be stored in localStorage or cookie?**
    Do not store your token in LocalStorage or SessionStorage, because such token can be read from javascript and therefore it is vulnarable to XSS attack.

    Do not store your token in Cookie. Cookie (with HttpOnly flag) is a better option - it's XSS prone, but it's vulnarable to CSRF attack
    
    Instead, on login, you can deliver two tokens: access token and refresh token. Access token should be stored in Javascript memory and Refresh token should be stored in HttpOnly Cookie. Refresh token is used only and only for creating new access tokens - nothing more.

    When user opens new tab, or on site refresh, you need to perform request to create new access token, based on refresh token which is stored in Cookie.

    I also strongly recommend to read this article: https://hasura.io/blog/best-practices-of-using-jwt-with-graphql/

4.**Localstorage vs Cookie**
    Cookies and local storage serve different purposes. Cookies are primarily for reading server-side, local storage can only be read by the client-side. So the question is, in your app, who needs this data — the client or the server?

    Local Storage
        Problems:

        Web Storage (localStorage/sessionStorage) is accessible through JavaScript on the same domain. This means that any JavaScript running on your site will have access to web storage, and because of this can be vulnerable to cross-site scripting (XSS) attacks. XSS in a nutshell is a type of vulnerability where an attacker can inject JavaScript that will run on your page. Basic XSS attacks attempt to inject JavaScript through form inputs, where the attacker puts alert('You are Hacked'); into a form to see if it is run by the browser and can be viewed by other users.
    Cookies
        Problems:

        Cookies, when used with the HttpOnly cookie flag, are not accessible through JavaScript, and are immune to XSS. You can also set the Secure cookie flag to guarantee the cookie is only sent over HTTPS. This is one of the main reasons that cookies have been leveraged in the past to store tokens or session data. Modern developers are hesitant to use cookies because they traditionally required state to be stored on the server, thus breaking RESTful best practices. Cookies as a storage mechanism do not require state to be stored on the server if you are storing a JWT in the cookie. This is because the JWT encapsulates everything the server needs to serve the request.

        However, cookies are vulnerable to a different type of attack: cross-site request forgery (CSRF). A CSRF attack is a type of attack that occurs when a malicious web site, email, or blog causes a user’s web browser to perform an unwanted action on a trusted site on which the user is currently authenticated. This is an exploit of how the browser handles cookies. A cookie can only be sent to the domains in which it is allowed. By default, this is the domain that originally set the cookie. The cookie will be sent for a request regardless of whether you are on galaxies.com or hahagonnahackyou.com.
    
    Key Differences:
        Capacity:

            Local Storage: 10MB
            Cookies: 4kb
        
        Browser Support:

            Local Storage: HTML5
            Cookies: HTML4, HTML5
        
        Storage Location:

            Local Storage: Browser Only
            Cookies: Browser & Server
        
        Send With Request:

            Local Storage: Yes
            Cookies: No
        
        Accessed From:

            Local Storage: Any Window
            Cookies: Any Window.
        
        Expiry Date:

            Local Storage: Never Expire, until done by javascript.
            Cookies: Yes, Have expiry date.
        
        Note: Use that, what suits you.