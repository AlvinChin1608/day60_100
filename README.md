# day60_100

# Building a Flask Contact Form with Email Functionality
While working on a Flask application with a contact form, I learned several key web development and email communication concepts. Here's a summary of my learning experience:

## Project Overview
This project aimed to create a contact form using Flask that allows users to send their messages directly to my email. The form collects the user's name, email address, phone number, and message, and upon submission, sends this information to my email address using the SMTP protocol.

## Demo
![](https://github.com/AlvinChin1608/day60_100/blob/main/gif_demo/ScreenRecording2024-07-25at23.14.08-ezgif.com-video-to-gif-converter.gif)

## Learning Highlights

1. __Integrating Bootstrap for Styling:__
   
  - I successfully applied Bootstrap's CSS classes to enhance the visual layout of the website, making it more appealing and user-friendly. This included using Bootstrap's grid system for layout management and its components for elements like buttons, forms, and responsive layouts.

2. __Understanding Form Structure:__

  - __Form Basics:__ I learned about structuring forms with input fields, labels, and buttons. The form collects user inputs such as name, email, phone number, and message. Each input field is paired with a label to improve accessibility and user experience.
  - __Form Attributes:__ I used attributes like __'action'__ and __'method'___ to specify how and where the form data should be sent. The __'action'__ attribute defines the URL endpoint on the server that handles the form submission, while the __'method'___ attribute determines how the data is sent, typically using the __'POST'__ method for secure data transmission.

3. __Implementing Form Handling in Flask:__

  - __Setting Up Routes:__ I set up a route in Flask to handle form submissions using the __'POST'__ method. This allowed me to securely transmit form data to the server.
  - __Accessing Form Data:__ By utilizing __'request.form'__, I was able to retrieve user input from the form fields on the server side, enabling me to process and use the data as needed.
    
4. __SMTP and Email Sending:__

  - __smtplib Integration:__ To send form submissions to my email, I integrated Python's smtplib library, which involved configuring SMTP settings and securely logging in with my email credentials.
  - __Email Message Composition:__ I crafted email messages using Python string manipulation to include the user's input, ensuring the format was clear and concise.

## Conclusion
This project provided valuable insights into web development with Flask, specifically in handling form submissions and email integration. It was a great learning experience that helped me understand the importance of server-side data handling and secure email communication. Moving forward, I plan to implement additional features, such as form validation and confirmation emails, to further improve the functionality and user experience of my website.
