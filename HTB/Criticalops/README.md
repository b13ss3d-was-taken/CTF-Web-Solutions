The application presents a simple interface with login functionality:

![image.png](./images/image.png)

After successfully logging in and analyzing the network traffic, it took me a while to notice an interesting behavior. The server doesn't send a `Set-Cookie` header in the response, yet somehow a session is established:

![image.png](./images/image(1).png)

Upon closer inspection of subsequent requests, an `authToken` cookie appears in the browser, despite not being set by the server:

![image.png](./images/image(2).png)

Decoding this token reveals it's a HS256 JWT containing user information:

![image.png](./images/image(3).png)

The key insight comes from examining the client-side authentication flow. The JWT is generated on the client-side, and by inspecting the JavaScript code, we can discover the secret key used to sign the token:

![image.png](./images/image(4).png)

With access to the signing secret, we can forge our own JWT with administrative privileges. Using a JWT manipulation tool, we craft a new token with the admin role:

![image.png](./images/image(5).png)

After placing the forged JWT in the browser's Local Storage and navigating to `/admin`, we successfully access the administrative panel and retrieve the flag:

![image.png](./images/image(6).png)