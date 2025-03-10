# Sultan's using Django, Python and Postgres.

## Introduction
Welcome to Sultan's restaurant! A website offering a prestigious menu and booking facility, allowing users to conveniently create and manage bookings at the restaurant.

The intended purpose is to provide a seamless experience with a user-friendly menu and streamlined booking process. Allowing users to view the menu and managing bookings at a time and on a device that suits. Potentials users of the site can include regular customers who know exactly what they want to eat and when or food enthusiasts venturing out to explore the rich culinary experience Sultan's has to offer.  
## Table of Contents

### [User Experience (UX)](#user-experience-ux-1)

* User Stories

* Mind Map: Ideas

* Wireframe Designs 

* UX View

* Pseudo - functions needed (Brainstorm)

* Process Map

* Models and Entity Relationship Diagrams

### [Main Page](#main-page-1)

* Features

### [Testing](#testing-1)

* Fixed Bugs 

* Validation Testing

* Manual Testing

* Automated Testing

* User Story Testing 

### [Future Developments](#future-developments-1)

###  [Workload Planning](#workload-planning-1)

###   [Site Production, Deployment and Contribution](#site-production-deployment-and-contribution-1) 

 * Site production

 * Deployment

 * Contribution

### [Technologies and tools Used](#technologies-and-tools-used-1)

* Languages used

* Frameworks, Libraries and Programs Used
     	
### [Credits](#credits-1)

* Content

 * General
  
 * Overall Credit

### [Personal Summary](#personal-summary-1)

#
 

## User Experience (UX)
### User Stories

The initial step taken was to the establish the user stories identifying the needs and requirements for the site. These have further provided the foundation for the project allowing me to categorise the development and deployment using agile methodology.

Each user below contains the initial story along with acceptance criteria. These both would need be satisfied during development and testing for the user story to be deemed a success.

### **US1:** As a **customer** I can **create a booking reservation online** so that **I can secure the booking**
#### Acceptance Criteria

- The customer should be prompted to register and/or login. 
- The site should authenticate the user so that bookings can be attached to them.
- The booking form should include fields: 
    -  contact number (required)
    - email (required)
    - time slot (required)
     - date (required)
     - number of people (required) 
    -  special requests (optional)
    
- The booking form should be validated for any errors/missing values.
- On a successful booking, the customer should receive a notification.
- The customer should only be able to see their own bookings.

### **US2:** As a **customer** I can **cancel the booking** so that **I can create again at another time**
#### Acceptance Criteria

-	The customer should be authenticated so they can only see their own bookings.
-	The customer should be able to select the relevant booking to delete.
-	The customer should be asked to confirm the delete.
-	The customer should receive a notification once the delete has been completed. 
-	The booking should be removed from the customer’s account.

### **US3:** As a **customer** I can **cancel the booking** so that **I can create again at another time**
#### Acceptance Criteria

-	The customer should be authenticated so they can only see their own bookings.
-	The customer should be able to select the relevant booking to update.
-	The selecting booking information should be place in the booking form for the customer to update.
-	The site should check availability of the said changes.
-	The site should update the booking if there is availability.
-	The customer should receive a notification of the update.

### **US4:** As a **customer** I can **see the menu online** so that **I can decide what I want to eat beforehand**
#### Acceptance Criteria

- The menu should be accessible on all devices in a clean and easy to read format.
- The menu should contain all the items currently being served at the restaurant.
- Each item should have a name, description (where applicable) and a price.
- Unavailable items are not shown/marked as unavailable.
- Menu is broken down into the relevant categories for ease.
- Any allergen information is easy to find. 

### **US5:** As a **manager** I can **update the menu** so that **customers can see the latest menu**
#### Acceptance Criteria

- The manager should be able to login and be validated as such.
- A link should be made available for the manager to update the menu.
- The manager should be able to navigate to the menu section.
- Each menu item has a name, an option description, price and status which should be filled in.
  -   Status should allow for the item to be active/inactive from the menu.
- The manager should be able to add new items to the menu.
- The manager should be able to delete/update current items in the menu.
   -   An item being deleted should ask for confirmation of deletion.
- Any changes made should be reflected on the live menu.

### **US6:** As a **admin** I can **add promotions to the home page** so that **the customer can see these as they become live**
#### Acceptance Criteria

- The admin should be able to login and be validated as such.
- The admin should be able to navigate to the welcome promotions section.
- The admin should be able to add/update/delete any special offers.
  -  Should have the option to "toggle" active/previous promotions.
- Any changes made should be reflected on the live menu.

### **US7:** As a **manager** I can **manage bookings via the admin panel** so that **I can efficiently manage the restaurant**
#### Acceptance Criteria

- The manager should be able to easily navigate to the bookings section.
- The manager should be able to see all the bookings and the related information.
- The manager should be able to search using the following.
     - Name
     - Contact info (number/email)
     - Date
- The manager should be able to create/edit/delete bookings.
    - The delete should prompt a confirmation.
    - new/edited bookings should be shown in the customer's account to view.

### **US8:** As a **super user** I can **create accounts for the staff** so that **they can help the managers when things are busy**
#### Acceptance Criteria

- The super user should be able to create staff accounts as requested by management.
- The accounts should have specific permissions on the admin panel for certain members.
- The staff accounts should only be able to see/use areas permitted on the admin panel.

**Please Note**: The acceptance criteria may be added to/updated within the agile tool to allow implementation of the core requirements in the user stories.

### Mind Map: Ideas

Following on from the user stories, a initial mind map(pen to paper) was created to capture functionality of the site. The purpose of this was to provide a high-level understanding of how the user stories could be implemented:

![Mindmap](readme-images/mind_map.jpeg)


### Wireframe Designs

The next step taken was to create wireframes (shown below) using Balsamiq. These wireframes illustrate the planned layouts and components to be used to satisfy the user stories.

![home/index](readme-images/wireframes/1_home.png)

![menu](readme-images/wireframes/2_menu.png)

![aboutus](readme-images/wireframes/3_aboutus.png)

![booking_not_logged_in](readme-images/wireframes/4_booking_not_logged_in.png)

![login](readme-images/wireframes/5_login.png)

![register](readme-images/wireframes/6_Register.png)

![logout](readme-images/wireframes/7_logout.png)

![booking_logged_in](readme-images/wireframes/8_booking_logged_in.png)

![booking_created](readme-images/wireframes/9_booking_created.png)

![booking_unavailable](readme-images/wireframes/10_booking_unavailable.png)

![booking_invalid](readme-images/wireframes/11_booking_invalid.png)

![booking_deleted](readme-images/wireframes/12_booking_delete.png)

![booking_updated](readme-images/wireframes/13_booking_update.png)

[Back to Contents.](#table-of-contents)


### UX View

Following on from the wireframe designs, final UX views of the site were created:

![home/index](readme-images/UX/1_ux_home.png)

![menu](readme-images/UX/2_ux_menu.png)

![aboutus](readme-images/UX/3_ux_aboutus.png)

![booking_not_logged_in](readme-images/UX/4_ux_booking_not_logged_in.png)

![login](readme-images/UX/5_ux_sign_in.png)

![register](readme-images/UX/6_ux_register.png)

![logout](readme-images/UX/7_ux_logout.png)

![booking_logged_in](readme-images/UX/8_ux_booking_logged_in.png)

![delete_booking](readme-images/UX/9_ux_delete_booking.png)

![update_booking](readme-images/UX/10_ux_update_booking.png)

[Back to Contents.](#table-of-contents)

Completion of the UX element provided a clear refined picture of the finished product. The definition of colours, classes, placements, and components provided all the necessary information to develop the site ensuring a positive user experience.  


### Pseudo - functions needed (Brainstorm)

On completion of the UX element, the next step take was to map out the functions needed for the booking system to perform as needed: 

![pseudo-functions](readme-images/pseudo_functions.jpeg)

### Process Map

The diagrams below map out the processes and paths taken based on the choices made and the validation outcome:

![create booking](readme-images/process-maps/process_map_create_booking.png)

![update booking](readme-images/process-maps/process_map_update_booking.png)

![delete booking](readme-images/process-maps/process_map_delete_booking.png)

![promotion management](readme-images/process-maps/process_map_prmotions.png)

![menu management](readme-images/process-maps/process_map_menu.png)

These process maps have played a pivital part as a reference guide during the course of the development. They have allowed me to ensure that all requirements and acceptance criteria from the user stories have been satisfied. 

[Back to Contents.](#table-of-contents)


### Models and Entity Relationship Diagrams (ERD's)

The project is broken down in to four django models:

1. WelcomePromotion - for the promotions on the home page.
2. MenuItem - for the menu items.
3. MakeBooking - for the bookings.
4. AboutUs - for the content on the about us page. 

#### 1. WelcomePromotion

The welcome model contains the setup:

- promotion_title:  the title for the promotion.
- description: description of the promotion.
- is_valid: whether the current promotion is running or not.
- added_on: automated date on when the promotion was added.

The ERD schema for the WelcomePromotion model is displayed below:

![ERD: WelcomePromotion](readme-images/ERDS/erd_welcomePromotion.png)


#### 2. MenuItem

The MenuItem model contains the setup:

- name: name of the item.
- description: description of the item.
- category: category choices( Starter, Main, Side, Dessert, Drink) for the item to placed in.
- price: cost of the item.f
- added_on: automated date on when the item was added to the menu. 
- active: whether the item is available or not.

The ERD schema for the MenuItem model is displayed below:

![ERD: MenuItem](readme-images/ERDS/erd_MenuItem.png)


#### 3. MakeBooking

The MakeBooking model contains the setup:

- user: name of the requested user.
- name: name for the booking(automatically assigned the requested user).
- email: email for the booking.
- phone: phone for the booking.
- date: date of the booking.
- time_slot: time for the booking.
- number_of_people: number of people on the booking.
- special_requests: any special requests for the booking (e.g. birthday).

The ERD schema for the MakeBooking model is displayed below:

![ERD: MakeBooking](readme-images/ERDS/erd_MakeBooking.png)

#### 4. AboutUs

The AboutUs model contains the setup:

- name: name of the entry.
- description: content for the current entry.
- added_on: automated date on when entry was added in.
- is_valid: whether the current about us content is displayed or not. 

The ERD schema for the AboutUs model is displayed below:

![ERD: AboutUs](readme-images/ERDS/erd_AboutUs.png)

[Back to Contents.](#table-of-contents)

## Main page

### Features

[Back to Contents.](#table-of-contents)

## Testing

### Fixed Bugs 


### Validation Testing


### Manual Testing




## Future Developments



## Workload Planning



[Back to Contents.](#table-of-contents)

## Site Production, Deployment and Contribution  

### Site production



### Contribution


## Technologies and tools Used
### Languages used
   
### Frameworks, Libraries and Programs Used



[Back to Contents.](#table-of-contents)    
## Credits
### Content

## Overall Credit


## Personal Summary


