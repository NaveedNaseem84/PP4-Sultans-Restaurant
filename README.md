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

### [Project Walkthrough](#project-walkthrough-1)

* Home
* Menu
* Book
* About us

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
- Each menu item has a name, an option description, price, and status which should be filled in.
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

Following on from the user stories, an initial mind map(pen to paper) was created to capture functionality of the site. The purpose of this was to provide a high-level understanding of how the user stories could be implemented:

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

These process maps have played an essential part as a reference guide during the development. They have allowed me to ensure that all requirements and acceptance criteria from the user stories have been satisfied. 

[Back to Contents.](#table-of-contents)


### Models and Entity Relationship Diagrams (ERD's)

The project is broken down into four django models:

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
- category: category choices( Starter, Main, Side, Dessert, Drink).
- price: cost of the item.
- added_on: automated date on when the item was added to the menu. 
- active: whether the item is available or not.

The ERD schema for the MenuItem model is displayed below:

![ERD: MenuItem](readme-images/ERDS/erd_MenuItem.png)


#### 3. MakeBooking

The MakeBooking model contains the setup:

- user: the individual creating the booking.
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

## Project Walkthrough

For the purposes of this project, roles with specific permissions have been setup and are as follows,

**manager:** The manager account has been setup so that they can:
- add/update/delete promotions on the home page.
- add/update/delete content on the about us page.
- add/update/delete items on the menu.

**admin:** The admin account has been setup so that they can:
- add/update/delete promotions from the home page.

**testuser:** The testuser account is a standard user, registered via the website that can:
- add/update/delete their own bookings.
- can only see their own bookings when logged in.

For clarity, these accounts will be referenced throughout this document.

**Please note:** The management of the menu, promotions and about us content is done using Django's admin panel. It is proposed as future developments to incorporate this into the front-end design reducing the need to use the admin panel.

## Home

The site presents a clean, elegant design with the aim of providing a welcoming atmosphere. The user is presented with a crisp layout, in an easy flowing colour scheme. The user's attention is captured by promotions available which are presented in an eye-catching way. The site is accessible on multiple devices giving a seamless user experience as illustrated below:

![Responsive site](readme-images/project-walkthrough/responsive-all-devices.png)

_**Image above generated using https://ui.dev/amiresponsive illustrating the responsiveness of the site.**_

### Features
#### Navigation

- The top of the page features a navigation menu with the site links available to the right
- home, menu, book, about us, login, register links: these take the user to the respected pages. 
- The navigation menu is available through the site and is styled reflecting which page the user is currently on(in bold) and which link is being hovered over (in red)

![menu-bar-full](readme-images/project-walkthrough/menu_full.png)

#### Menu - toggle
 
 - Devices running in other views such as mobile are presented with a light version of the menu that can be expanded as need providing the same functionality as the full version:

 ![toggle-menu](readme-images/project-walkthrough/menu_toggle.png)

 Below the menu, the user is welcomed to the site and instantly made aware of any special promotions that are running at the restaurant:


![home-welcome](readme-images/project-walkthrough/home_welcome.png)

The homepage also provides additional user interaction by placing convenient links to the menu and the bookings page in a clear manner. The placement of these links highlights the ease of access to the services on offer:

![follow-on-links](readme-images/project-walkthrough/follow_on_links.png)

Should the admin add, update, or remove any current promotions via the admin panel, these changes are reflected instantly on the live home page:

![no-promotions](readme-images/project-walkthrough/no-promotions.png)


#### Footer

- The footer contains links to the respected social media sites Facebook, X, Instagram, and YouTube using font awesome icons.
- These links are all opened in a new tab.
- The footer is available on all pages.

![footer-links](readme-images/project-walkthrough/footer_links.png)

**Please note:** There are currently no active social media pages for Sultan's. These links have been added in as place holders only. 

[Back to Contents.](#table-of-contents)

## Menu
### Features

Navigating to the menu page the user is presented with simple but effective layout. The menu has been broken down into the relevant categories to provide maximum user experience:

![menu-page](readme-images/project-walkthrough/menu_page.png)

The user has the option to select any heading as they please resulting in a fully responsive, interactive menu that provides the requested information. The menu items are listed with their name, description (if applicable) and price:

![show-menu-open](readme-images/project-walkthrough/show_menu_open.png)

There is an allergen note made available at the bottom of the menu, ensuring that any necessary information is available to user along with any dietary needs.

Like the promotions on the home page, if the manager adds, updates, or removes any items from the menu, these changes are reflected instantly on the site. This ensures that that site always provides the latest version of the menu.

[Back to Contents.](#table-of-contents)

## Bookings
### Features

The booking page requires the user to be logged in. The purpose of this login is to ensure that only the logged in user can create, update, or delete a booking, which will be reflected within their account. The initial navigation to this page presents the follow:

![alt text](readme-images/project-walkthrough/booking_not_logged_in.png)

If the user has an account already with Sultan's, they are welcome to login. On successful login, they are re-directed to the bookings page under their account. 

If the user is a new visitor to the site and does not have an account, they have a link available on the login page and the navigation menu to register:

![register](readme-images/project-walkthrough/register.png)

The registration process is simple; a username, optional email and a password that meets the criteria given. Once registered, the user is logged in as this registered user and automatically logged in:

![logged-in](readme-images/project-walkthrough/booking_logged_in.png)

**Please Note:** The assumption is now that the testuser has logged in for the remainder of this section.

Once logged, the booking page features a form allowing the testuser to create a booking. The information collected on the form is:

- Email - required field (in the correct format).
- Phone - required field (in the correct format with a maximum of 11 numbers).
- Date - required field ( from today onwards)
- Time slot - required field.
- Number of people - required field.
- special requests - optional.

![booking-form](readme-images/project-walkthrough/booking_form_empty.png)

On submission of the form, the required fields are validated. If there are any errors, these are highlighted accordingly, prompting correction.

In addition to the validation, there is a requirement for the date to be valid; it can only be from today onwards. Should the date be prior to today, an alert is given:

![invalid-date](readme-images/project-walkthrough/invalid_date.png)

[Back to Contents.](#table-of-contents)

### Create Booking

On a successful submission of the form, the site will perform an availability check to ensure that the date and time requested by testuser is available to book. If available, the booking will be created, testuser notified, and the booking details made available in testuser's account:

![booking-created](readme-images/project-walkthrough/booking_created.png)

If there is no availability, testuser is notified accordingly:

![no-availability](readme-images/project-walkthrough/no-availability.png)

The options to update and delete the booking are now available to testuser.

### Update Booking

To update the booking, the "Update" button is clicked which takes testuser to the update booking page. This page pre-populates the form with the current details make the process quick and easy:

![update-booking](readme-images/project-walkthrough/update_booking.png)

Testuser now can simply go in and update fields such as the number of people, or special requests, and save the form. If the date and time are to change, this would need to be checked for availability. If there is availability, the booking is updated,and an alert displayed:

![booking-updated](readme-images/project-walkthrough/booking_updated.png)

If there is no availability, similar to creating a booking, an alert is displayed. 

Should testuser want to navigate back to the bookings page, and select another booking, there is a "click here" link available to do this. 

### Delete Booking

To delete the booking, the "Delete" button is selected which displays an alert asking for confirmation of the delete:

![delete-confirm](readme-images/project-walkthrough/delete-confirm.png)

Once the delete has been confirmed, the selected booking is deleted and no longer visible in testuser's account. An alert is also displayed confirming the delete:

![booking-deleted](readme-images/project-walkthrough/booking_deleted.png)

### Booking Management

The manager has the ability to manage all the bookings that have been created. Once logged in, and authenticated as having access to the admin panel the manager will have total visiblity:

![manager-booking-visbility](readme-images/project-walkthrough/manager_booking_visibility.png)

From here, the manager is able to create, update or delete a booking. Once the neccessary action has been performed, the respected user's will show the changes.

In addition to this, to allow the management of bookings to be as efficient as possible, the manager has the facility to search by username, email and phone. Filtering options are also available and include date and time slot which can be seen on the right of the screen.


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


