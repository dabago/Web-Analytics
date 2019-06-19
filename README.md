# Individual assignment 2

## IE analytics

You're asked to create a service that allows users to keep track of
the analytics in their websites (think of Google Analytics).  You'll
need to implement the following:

### POST /register-url

this endpoint needs to receive a JSON via POST that will contain the
URL that's was visited.  For Example:

``` json
{"url": "http://client.com/route1"}
```

Clients of the IE Analytics service will call this route everytime
someone visits one of the web pages of their website.

### GET /dash

In this URL the user will see a bar chart of the 10 most visited URLs
in which, in the **x** axis there will be the URL, and the count in
the **y** axis
