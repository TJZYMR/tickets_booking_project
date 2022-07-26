## PROJECT DESCRIPTION:=>
- WHAT IS AN ONLINE MOVIE TICKET BOOKING SYSTEM ?
	A movie ticket booking system provides its customers the ability to purchase theatre seats online.
	E-ticketing systems allow the customers to browse through movies currently being played and to book seats, anywhere and 		anytime.
### Requirements and Goals of the System
	Our ticket booking service should meet the following requirements:
#### Functional Requirements
		Our ticket booking service should be able to list down different cities where its affiliate cinemas are located.
		Once the user selects the city, the service should display the movies released in that particular city.
		Once the user selects the movie, the service should display the cinemas running that movie and its available shows.
		The user should be able to select the show at a particular cinema and book their tickets.
		The service should be able to show the user the seating arrangement of the cinema hall and the user should be able to select multiple seats according to their preference.
		The user should be able to distinguish available seats from the booked ones.
		Users should be able to put a hold on the seats for five minutes before they make a payment to finalize the booking.
		The user should be able to wait if there is a chance that seats might become available – e.g. when holds by other users expire.
		Waiting customers should be serviced fairly in a first come first serve manner.
### Non-Functional Requirements:
			The system would need to be highly concurrent. There will be multiple booking requests for the same seat at any particular point in time. The service should handle this gracefully and fairly.
			The core thing of the service is ticket booking which means financial transactions. This means that the system should be secure and the database ACID compliant.

------------


### TECH-STACK:=>

	1. Python
	2. Django and Django-rest-framework    
	3. Unit testing using **Pytest and django.test**
	4. Logging
	5. API monitoring using Sentry.io
	6. Message Queue with Rabbitmq
	7. Task scheduling using Celery
	8. Caching using **Redis**/Memcached
	9. Docker and Docker-compose
	10. SQL Database-POSTGRES
	11. Nosql Database=Mongodb
	12. For deployment=>AWS ec2,s3,etc...
	13. Payment Gateway Integration using Razorpay or Payu or stripe(Undecided)

------------


### SYSTEM DESIGN:=>
                        
![alt text for screen readers](BOokmyshow_SYstemDesign.png "Text to show on mouseover")


------------


###### APIS :=>
	1. getCities/
	2. getTheatreByCity/
	3. getMovieByTheatre/
	4. getAuditoriumByMovie/
	5. getShowByAuditorium/
	6. bookseat/
	7. sendticketbyemial/
	8. postcommentsandreview/
	9. getAvailableSeatByShows/



------------

### DB DESIGN:=>




------------
### Commands And Extra Info on what is used and what will be:=>







####press alt+m shortcut

------------

