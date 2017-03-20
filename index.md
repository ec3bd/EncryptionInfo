# Encryption and Django

We need to encrypt two mediums: strings of plaintext in the context of messages between users and files uploaded by the users to be stored on the server.

### Messages between users
Every user we create a RSA keypair for and store both their public and private keys as TextFields in a django model. When sending a message from one user to another, the recipient's public key is retrieved from the database and used to encode the message. However, the private key field must remain accessible only by its owner when trying to read messages.
We can store all the messages in a separate table (with foriegn keys identifying the sending and receiving users) and we never have to store the plaintext, just the encrypted version and the user models will have the keys necessary to display them upon user request.

### Files
This will probably prove a bit trickier depending on how the instructions are interpreted, as we may have to do the manipulation in javascript instead of python which would be uncharted waters. Django does have a FileField field for models, which conveniently wraps serverside file storage. We could upload files via a form element, encrypt them on server, and store the encrypted version of the file to a FileField in a model. However, the instructions say the files have to be uploaded before they are uploaded to the web application, which may mean that we need to do it in javascript. Javascript is loaded onto the clients computer and can encrypt a file there so that the file is not transported over the network in unencrypted form when sending it to the server. This may not be what they meant and it may be sufficient to simply encrypt it before saving it though.

Basically for both of these we should be able to use the same library we used in lab, and therefore pretty much the same method for the actual encryption. The storage will be handled fairly seamlessly by Django's models. 

If we wanted to do SSL, which would solve the potential problem of having to have the file secure before it is uploaded, it seems like it would be difficult on the django development server, so we should probably consider other ways of getting around this potential obstacle.
