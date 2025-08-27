This challenge exposes two ports. The first one hosts the main application:

![image.png](./images/image.png)

The second port runs an "email client" service:

![image.png](./images/image(1).png)

Initially, I assumed I needed to create an account using this email service, but that's not necessary. The email client is used to receive tokens when requesting password resets:

![image.png](./images/image(2).png)

This behavior seemed suspicious, so I examined the source code. The `getPasswordReset` function has several critical vulnerabilities: it doesn't validate if a token exists or has expired, and it doesn't verify if the token belongs to a specific user:

![image.png](./images/image(3).png)

This means I can reset the admin's password instead of my own. The admin's email address can also be found in the source code:

![image.png](./images/image(4).png)

After logging in as admin, the `Dispatch Weapon` feature becomes available. This is a form that accepts markdown input:

![image.png](./images/image(5).png)

Reviewing the code reveals a dangerous vulnerability. When using markdown image syntax (`![description](URL)`), the application uses a regular expression to extract the URL (1), then executes `curl -s ${URL}` (2) to fetch the image contents:

![image.png](./images/image(6).png)

The application then base64 encodes the command result to embed the image using a data URI scheme.

Since we control the URL parameter, we can inject commands. To read the flag, I used the payload `![](; cat /flag.txt)`, which successfully retrieved the flag:

![image.png](./images/image(7).png)