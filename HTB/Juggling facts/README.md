This challenge presents a web application that displays various facts through three available options:
- Spooky facts
- Not So Spooky Facts  
- Secret Facts

![Web Application Interface](./images/image.png)

The application loads facts by making a POST request to `/api/getfacts` with a JSON body:

![API Request Structure](./images/image(1).png)

Setting "type" to "secrets" returns the response: "Currently this type can be only accessed through localhost!"

Examining the source code reveals the validation logic:

![Source Code Analysis](./images/image(2).png)

There's a validation that prevents accessing secrets unless the request originates from localhost(1). However, the application also uses a switch/case statement to handle different type values(2). As suggested by the challenge title, the vulnerability involves Type Juggling, which occurs because the `switch` statement performs loose comparison.

![Switch Statement Logic](./images/image(3).png)

To obtain the secrets without directly setting "type" to "secrets", we can exploit PHP's type juggling behavior using this comparison table:

![](https://secops.group/wp-content/uploads/2022/12/Strict-Comparisions-1024x582.png)

When comparing a string with `true`, the comparison evaluates to true. This allows us to fall into the first case (the "secrets" case), successfully retrieving the flag:

![Flag Retrieved](./images/image(4).png)