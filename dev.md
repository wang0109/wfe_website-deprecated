Development log
----

To split routes that need auth, and those don't, check this out:
http://stackoverflow.com/questions/7951810/check-each-node-js-request-for-authentication-credential

Idea for S3 auth,save key in db, send key to client side and keep as a token in browser storage across tabs,
then use as part of context in js code that use AWS sdk to get files off S3.

part of db design:
map user id to its secret key, or further, we could do the reverse way, given secret key as the primary key and , it is asscociated with one or more user ids
