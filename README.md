# Sultan's using Django, Python and Postgres.

## Introduction
Welcome to Sultan's restaurant! A website offering a prestigious menu and booking facility, allowing users to conveniently create and manage bookings at the restaurant.

The intended purpose is to provide a seamless experience through out with a user-friendly menu and streamlined booking process. Allowing users to view the menu and managing bookings at a time and on a device that suits. Potentials users of the site can include regular customers who know exactly what they want to eat and when, or food enthusiasts venturing out to explore the rich culinary experience Sultan's has to offer.  
## Table of Contents

### [User Experience (UX)](#user-experience-ux-1)

* User Stories

* Mind Map: Ideas

* Wireframe Designs 

* UX View

* Pseudo - functions needed (Brainstorm)

* Process Map

* Models and Entity Relationship Diagrams (ERD's)

### [Project Walkthrough](#project-walkthrough-1)

* Roles

* Home

* Menu

* Booking

* About us

### [Testing](#testing-1)

* Fixed Bugs 

* Validation Testing

* Functionality/performance testing

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

## User Experience (UX)
### User Stories

The first step taken was to the establish the user stories identifying the needs and requirements for the site. These have further provided the foundation for the project allowing me to categorise the development and deployment using agile methodology.

Each user story below has the initial story along with acceptance criteria. These both would need be satisfied during development, testing and deployment for the user story to be considered a success.

### **US1:** As a **customer** I can **create a booking reservation online** so that **I can secure the booking.**
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

### **US2:** As a **customer** I can **delete the booking** so that **I can create again at another time.**
#### Acceptance Criteria

-	The customer should be authenticated so they can only see their own bookings.
-	The customer should be able to select the relevant booking to delete.
-	The customer should be asked to confirm the delete.
-	The customer should receive a notification once the delete has been completed. 
-	The booking should be removed from the customer’s account.

### **US3:** As a **customer** I can **update my booking** so that **I can fit it around my schedule.**
#### Acceptance Criteria

-	The customer should be authenticated so they can only see their own bookings.
-	The customer should be able to select the relevant booking to update.
-	The selecting booking information should be placed in the booking form for the customer to update.
-	The site should check availability of the said changes.
-	The site should update the booking if there is availability.
-	The customer should receive a notification of the update.

### **US4:** As a **customer** I can **see the menu online** so that **I can decide what I want to eat beforehand.**
#### Acceptance Criteria

- The menu should be accessible on all devices in a clean and easy to read format.
- The menu should contain all the items currently being served at the restaurant.
- Each item should have a name, description (where applicable) and a price.
- Unavailable items are not shown/marked as unavailable.
- Menu is broken down into the relevant categories for ease.
- Any allergen information is easy to find. 

### **US5:** As a **manager** I can **update the menu** so that **customers can see the latest menu.**
#### Acceptance Criteria

- The manager should be able to login and be validated as such.
- A link should be made available for the manager to update the menu.
- The manager should be able to navigate to the menu section.
- Each menu item has a name, an optional description, price, and status which should be filled in.
  -   Status should allow for the item to be active/inactive from the menu.
- The manager should be able to add new items to the menu.
- The manager should be able to delete/update current items in the menu.
   -   An item being deleted should ask for confirmation of deletion.
- Any changes made should be reflected on the live menu.

### **US6:** As a **admin** I can **add promotions to the home page** so that **the customer can see these as they become live.**
#### Acceptance Criteria

- The admin should be able to login and be validated as such.
- The admin should be able to navigate to the welcome promotions section.
- The admin should be able to add/update/delete any special offers.
  -  Should have the option to "toggle" active/previous promotions.
- Any changes made should be reflected on the live site.

### **US7:** As a **manager** I can **manage bookings via the admin panel** so that **I can efficiently manage the restaurant.**
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

### **US8:** As a **super user** I can **create accounts for the staff** so that **they can help the managers when things are busy.**
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

**Please note:** The process to add, update, or delete promotions and menu items is carried out via the admin panel. The purpose of the process maps for this functionality is to highlight suitability and how it aligns with the project goals.

[Back to Contents.](#table-of-contents)


### Models and Entity Relationship Diagrams (ERD's)

The project is broken down into four models:

1. WelcomePromotion - for the promotions on the home page.
2. MenuItem - for the menu items.
3. MakeBooking - for the bookings.
4. AboutUs - for the content on the about us page. 

#### 1. WelcomePromotion

The welcome model has the following setup:

- promotion_title:  the title for the promotion.
- description: description of the promotion.
- is_valid: whether the current promotion is running or not.
- added_on: automated date on when the promotion was added.

The ERD schema for the WelcomePromotion model is displayed below:

![ERD: WelcomePromotion](readme-images/ERDS/erd_welcomePromotion.png)


#### 2. MenuItem

The MenuItem model has the following setup:

- name: name of the item.
- description: description of the item.
- category: category choices( Starter, Main, Side, Dessert, Drink).
- price: cost of the item.
- added_on: automated date on when the item was added to the menu. 
- active: whether the item is available or not.

The ERD schema for the MenuItem model is displayed below:

![ERD: MenuItem](readme-images/ERDS/erd_MenuItem.png)


#### 3. MakeBooking

The MakeBooking model has the following setup:

- user: the individual creating the booking. This is retrieved from the User model. 
- email: email for the booking.
- phone: phone for the booking.
- date: date of the booking.
- time_slot: time for the booking.
- number_of_people: number of people on the booking.
- special_requests: any special requests for the booking (e.g. birthday).

The ERD schema for the MakeBooking model is displayed below:

![ERD: MakeBooking](readme-images/ERDS/erd_MakeBooking.png)

#### 4. AboutUs

The AboutUs model has the following setup:

- title: name of the entry.
- description: content for the current entry.
- added_on: automated date on when entry was added in.
- is_valid: whether the current about us content is displayed or not. 

The ERD schema for the AboutUs model is displayed below:

![ERD: AboutUs](readme-images/ERDS/erd_AboutUs.png)

**Please note:** nullable fields above are optional fields.

[Back to Contents.](#table-of-contents)

## Project Walkthrough

### Roles

For the purposes of this project, roles with specific permissions have been setup and are as follows:

**manager:** The manager account has been setup so that they can:
- add/update/delete promotions on the home page.
- update content on the about us page.
- add/update/delete items on the menu.

**admin:** The admin account has been setup so that they can:
- add/update/delete promotions from the home page.

**testuser:** The testuser account is a regular customer at Sultan's, registered via the website and can:
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

- The top of the page features a navigation menu with the site links available to the right.
- home, menu, book, about us, login, register links: these take the user to the respected pages. 
- The navigation menu is available through the site and is styled reflecting which page the user is currently on(in bold) and which link is being hovered over (in red).

![menu-bar-full](readme-images/project-walkthrough/menu_full.png)

#### Menu - toggle
 
 - Devices running in other views such as mobile are presented with a light version of the menu that can be expanded  providing the same functionality as the full version:

 ![toggle-menu](readme-images/project-walkthrough/menu_toggle.png)

 If a staff user (manager or admin) logs in, the menu updates with an added link to the admin panel usefully made available:

 ![admin-link](readme-images/project-walkthrough/admin_link.png)


 Below the menu, the user is welcomed to the site and instantly made aware of any special promotions that are running at the restaurant:


![home-welcome](readme-images/project-walkthrough/home_welcome.png)

The homepage also provides further user interaction by placing convenient links to the menu and the bookings page in a clear manner. The placement of these links highlights the ease of access to the services on offer:

![follow-on-links](readme-images/project-walkthrough/follow_on_links.png)

Should the **admin** add, update, or remove any current promotions via the admin panel, these changes are reflected instantly on the live home page:

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

There is an allergen note made available at the bottom of the menu, ensuring that any necessary information is available along with any dietary information.

Like the promotions on the home page, if the **manager** adds, updates, or removes any items from the menu, these changes are reflected instantly. This ensures that the site always provides the latest version of the menu.

[Back to Contents.](#table-of-contents)

## Booking
### Features

The booking page requires the user to be logged in. The purpose of this login is to ensure that only the logged in user can create, update, or delete a booking, which is reflected within their account. The initial navigation to this page presents the following:

![alt text](readme-images/project-walkthrough/booking_not_logged_in.png)

If the user already has an account with Sultan's, they are welcome to login. On successful login, they are re-directed to the bookings page under their account. 

If the user is a new visitor to the site and does not have an account, they have a link available on the login page and the navigation menu to register:

![register](readme-images/project-walkthrough/register.png)

The registration process is simple; a username, optional email and a password that meets the criteria given. Once registered, the user is automatically logged in:

![logged-in](readme-images/project-walkthrough/booking_logged_in.png)

**Please Note:** The assumption is now that the **testuser** has logged in for the rest of this section.

Once logged, the booking page features a form allowing testuser to create a booking. The information collected on the form is:

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

On a successful submission of the form, the site will perform an availability check to ensure that the date and time requested by **testuser** is available to book. If available, the booking will be created, **testuser** notified, and the booking details made available in **testuser's** account:

![booking-created](readme-images/project-walkthrough/booking_created.png)

If there is no availability, **testuser** is notified accordingly:

![no-availability](readme-images/project-walkthrough/no-availability.png)

The options to update and delete the booking are now available to **testuser.**

### Update Booking

To update the booking, the "Update" button is clicked which takes **testuser** to the update booking page. This page pre-populates the form with the current details make the process quick and easy:

![update-booking](readme-images/project-walkthrough/update_booking.png)

**Testuser** now can simply go in and update fields such as the number of people, or special requests, and save the form. If the date and time are to change, this would need to be checked for availability. If there is availability, the booking is updated, and an alert displayed:

![booking-updated](readme-images/project-walkthrough/booking_updated.png)

If there is no availability, like creating a booking, an alert is displayed. 

Should **testuser** want to navigate back to the bookings page, and select another booking, there is a "click here" link available to do this. 

[Back to Contents.](#table-of-contents) 

### Delete Booking

To delete the booking, the "Delete" button is selected which displays an alert asking for confirmation of the delete:

![delete-confirm](readme-images/project-walkthrough/delete-confirm.png)

Once the delete has been confirmed, the selected booking is deleted and no longer visible in **testuser's** account. An alert is also displayed confirming the delete:

![booking-deleted](readme-images/project-walkthrough/booking_deleted.png)

### Booking Management

The **manager** can manage all the bookings that have been created. Once logged in, and authenticated as having access to the admin panel, the **manager** will have total visibility:

![manager-booking-visbility](readme-images/project-walkthrough/manager_booking_visibility.png)

From here, the **manager** can create, update, or delete bookings. Once the necessary action has been performed, the respected user account will show the changes.

In addition to this, to allow the management of bookings to be as efficient as possible, the **manager** has the facility to search by username, email, and phone. Filtering options are also available and include date and time slot which can be seen on the right of the screen.

[Back to Contents.](#table-of-contents)

## About us

The about us page highlights the core values of Sultan's in the clear, easy to ready format that is seen throughout the site:

![aboutus](readme-images/project-walkthrough/about_us.png)

The **manager** can update and style the content on the about us page as needed. This includes, colours, spacing and font size as examples. 

**Please Note:** The assumption is that there will only be one entry active at one time, managed at a local level. The site ensures that only the latest version of this entry is always displayed.

To complete the current logged in session, a logout option is available on the menu bar which prompts confirmation:

![logout](readme-images/project-walkthrough/logout.png)

Once confirmed, the **testuser** is logged out and the site is ready for the next user.

[Back to Contents.](#table-of-contents) 

## Testing

### Fixed Bugs 
* **Issue 1 (ID 2f88738):** Bookings were successfully being created but not attached to the user creating them. This meant that any logged in user was able to see all the bookings created.

  * **Fix (ID 7bebcc1):** This was fixed by adding a filter to the query fetching the current bookings. The filter only returned bookings where the user on the bookings was the same as the user currently logged in. This was tested with two individual test accounts to ensure it worked as it should be.

* **Issue 2 (ID 6ad7f00):**  The booking form `phone` field allowed for non-digit characters to pass through as valid. The same `phone` field was validated correctly within the admin panel using the regex in place.

* **Fix (ID 2c4527c):** This was fixed by adding a custom validation on the form field to raise an error if the entered data did not consist of all digits. The validation error displayed using the Django message network.

This was further refined **(ID 13ea71e)** with the installation of crispy forms. After testing, the validation was being returned correctly and displayed in line with the other form validation. This was tested further over the next few commits and the custom validation removed as it was no longer needed.

* **Issue 3 (ID 13ea71e):** 
**_Note_**: This bug was found after the commit.

If the fields other than the date and time were being updated, the booking was noted as a duplicate and alerting the user as such. For example, if the booking required the addition of people with a special request of "surprise meal"  on the same date and time slot, the booking was not being updated.

* **Fix (ID c2e3c54):** This was fixed by refactoring the update booking function introducing a booking changed check:
1. Check if the form is valid.
2.  store the forms date and time slot.
3. if posted form date and time different from the current booking date and time slot:
    - check the availability as done previously.
    - save if available.
4. If the date and time remains unchanged, save the form with any other changes. 

[Back to Contents.](#table-of-contents) 

### Validation Testing

The code has been tested with the following:

* HTML
   * No errors returned when running the official W3C validator [W3C HTML Validator.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsultans-restaurant-eaffca2215ff.herokuapp.com%2F)

* CSS
   * No errors were found when running the official jigsaw Validator tool (direct input)  [(Jigsaw) Validator.](https://jigsaw.w3.org/css-validator/)

* JavaScript
    * No significant errors were returned when checking the JavaScript code using [(JS Hint.)](https://jshint.com/)

* Python
   * No errors returned when running the code on the [Code Institute Python Linter.](https://pep8ci.herokuapp.com/)
   * Results: All clear, no errors found

### Functionality/performance testing

To ensure the site performed and functioned as expected across browsers, resolutions and devices, the following was tested:

| Criteria               |      Details              | Status |
|:---------------------- |:--------------------------|:------:|
| Desktop browsers:      | Edge                      | Pass   |  
|                        | Chrome                    | Pass   |
|                        | Mozilla Firefox           | Pass   |
|                        | Safari - on Mac OS        | Pass   |
| Mobile browsers:       | Chrome                    | Pass   |
|                        | Safari                    | Pass   |
| Resolutions:           |                           | Pass   |
| desktop                | 1366 x 768 to 1920 x 1080 | Pass   |
| mobile                 | 375 x 667 to 1440 x 3120  | Pass   |
| Devices used:          |                           | Pass   |
|                        | Samsung S24 Ultra         | Pass   |
|                        | Samsung A32 5G            | Pass   |
|                        | iPad 10th gen             | Pass   |
|                        | iPhone 14 Pro             | Pass   |

The testing above found no issues.

The following lighthouse results were returned from the deployed site:

Home:

![home-lighthouse](readme-images/testing/lighthouse_home.png)

Menu:

![menu-lighthouse](readme-images/testing/lighthouse_menu.png)

Booking:

![booking-lighthouse](readme-images/testing/lighthouse_booking.png)

About:

![booking-lighthouse](readme-images/testing/lighthouse_aboutus.png)



### Manual Testing

The following manual testing has been carried out to confirm if the site's performance and functionality matched the expected output. It has tested both JavaScript and Python functionality.

| Test  | Test Step                             |Expected                                                                 |  Result                                       |Status |
| :----:|:----------------------------------------------|:----------------------------------------------------------------|:----------------------------------------|:----:| 
| MT1   |register - successful                          |user can register, login                                         |registered, logged in                    |Pass  | 
| MT2   |register -invalid                              |username/password weak notification                              |advise give to correct                   |Pass  |
| MT3   |login - superuser                              |super user authenticated on log in                               | authenticated, logged in                |Pass  |
| MT4   |login - testuser                               |testuser to be authenticated on log in                           | authenticated, logged in                |Pass  |
| MT5   |login - manager                                |authenticate as manager, access link to admin panel visible.     |logged in, can access admin panel        |Pass  |
| MT6   |login - invalid                                |notification of login failure. No access given.                  |no access given, login fail notification |Pass  |
| MT7   |login - admin                                  |authenticate as admin, access link to admin panel visible.       |logged in, can access admin panel        |Pass  |
| MT8   |view bookings - booking link                   | navigates to booking page                                       | as expected                             |Pass  |
| MT9   |access booking - not logged in                 |no access to bookings, asked to login                            | redirected to login page.               |Pass  |
| MT10  |create booking - email invalid                 |email to be validated for correct format                         | prompt given to correct                 |Pass  |
|MT11   |create booking - phone invalid                 |phone to be validated for correct format                         | prompt given to correct                 |Pass   |
|MT12   |create booking - date invalid                  |notification to be given of previous date                        | notification given to correct           |Pass   |
|MT13   |create booking - time missing                  |prompt to be given to enter time                                 | prompt given to enter                   |Pass   |
|MT14   |create booking - people missing                |prompt to be given to enter no of people                         | prompt given to correct                 |Pass   |
|MT15   |create booking - time/date unavailable         |notification of unavailability to be given                       | notification given on unavailability    |Pass   |
|MT16   |create booking - valid                         |notification that booking is created, available to see in account| Notification given, booking shown      |Pass   | 
|MT17   |update booking - booking selection             |current booking details to pre-fill form                         | form pre-filled                        |Pass   | 
|MT18   |update booking - time/date change (unavailable)|notification of unavailability to be given                       | notification given, booking shown       |Pass   |
|MT19   |update booking - Other information changed     |booking to be updated, notification given                        | notification given, booking updated     |Pass   |
|MT20   |delete booking - confirmation                  |request to confirm delete. Option to delete or cancel            | request given. Options: Delete, cancel  |Pass   |
|MT21   |delete booking - cancel delete                 |action to delete cancel. Booking not affected                    | delete cancelled. Booking remains       |Pass   |
|MT22   |delete booking - post confirmation             | booking deleted, notification of delete shown                   | booking deleted, notification shown     |Pass   |
|MT23   |navigate to home - home link                   | navigates to the home page, show any active promotions          | as expected                             |Pass   |
|MT24*  |add promotion - admin                          | promotion to be shown on home page                              | promotion shown                         |Pass   |
|MT25*  |update promotion - admin                       | updated promotion to be shown on home page                      | updated promotion shown                 |Pass   |
|MT26*  |promotion not live - admin                     | promotion to exist, but not be displayed                        | exists in admin, not shown              |Pass   |
|MT27*  |delete promotion - admin                       | promotion to be deleted after a confirmation                    | promotion deleted                       |Pass   |
|MT28   |view the menu - menu link                      | navigates to and display the menu                               | live menu shown                         |Pass   |
|MT29*  |add menu item - manager                        | menu item to be visible on the menu                             | item visible on menu                    |Pass   |
|MT30*  |update menu item - manager                     |updated menu item to be visible on the menu                      | updated item visible on menu            |Pass   |
|MT31*  |menu item not live - manager                   | menu item should exist, but not displayed on menu               | exists in admin, not shown              |Pass   |
|MT32*  |delete menu item - manager                     | menu item to be deleted after confirmation                      | item visible on menu                    |Pass   |
|MT33   |view about us - about us link                  | navigates to and display the about us content                   | as expected                             |Pass   |
|MT34*  |update about us content - manager              | updated content to be displayed                                 | Displayed                               |Pass   |
|MT35*  |create booking - manager                       | created a booking, booking shown in respected user's account    | booking created, attached to user       |Pass   |
|MT36*  |update booking - manager                       | update a booking, update booking shown                          | booking updated                         |Pass   |
|MT37*  |delete booking - manager                       | delete a booking, booking removed from user's account           | booking deleted, removed                |Pass   |
|MT38*  |search booking - manager                       | search using name, contact or date to find booking              | searchable with expected fields         |Pass   |


*Functionality carried out on the admin panel but has been tested to ensure functionality for this project.

[Back to Contents.](#table-of-contents) 

### Automated Testing - scripts

In addition to the manual testing above, automated testing has been carried out within the project as follows:

| Test  |Test Name                                      |Summary                                                |  Result  |
| :----:|:----------------------------------------------|:------------------------------------------------------|:--------:|
|AT1    | test_about_us_view                            | about us correctly displayed                          | Pass     |
|AT2    | test_menu_view                                | menu correctly displayed                              | Pass     |
|AT3    | test_home_view                                | home page correctly displayed                         | Pass     |             
|AT4    | test_form_is_valid                            | form fields validation                                | Pass     |
|AT5    | test_form_email_invalid                       | email is incorrect                                    | Pass     |
|AT6    | test_form_phone_missing                       | phone is missing                                      | Pass     |
|AT7    | test_form_phone_invalid                       | phone is in invalid format                            | Pass     |
|AT8    | test_form_date_missing                        | date is missing                                       | Pass     |
|AT9    | test_form_time_slot_missing                   | time slot is missing                                  | Pass     |
|AT10   | test_form_no_of_people_missing                | number of people is missing                           | Pass     |
|AT11   | test_view_create_booking_valid                | a valid booking is created                            | Pass     |
|AT12   | test_view_create_booking_date_past_date       | a booking with a past date                            | Pass     |
|AT13   | test_view_create_booking_time_date_unavailable| unavailability on the date and time                   | Pass     |
|AT14   | test_view_update_booking_valid                | a valid booking updated                               | Pass     |
|AT15   | test_view_update_booking_unvailable           | unavailability to update the date and time            | Pass     |
|AT16   | test_view_delete_booking                      | a booking that is deleted                             | Pass     |


A summary of these test results ran within the terminal can be seen below:

![alt text](readme-images/testing/automated_testing_results.png)

### User Story testing

A combination of the manual and automated testing has tested all aspects of the site. To ensure that all the user stories have been successfully implemented, the associated tests above have been tabulated below illustrating the success route:

| User Story  |Test number applicable         |Result          |
| :----------:|:------------------------------------|:---------|
| US1         |MT4, MT8 - MT16, AT4 -AT13           |Successful|
| US2         |MT4, MT8, MT20 - MT22, AT16          |Successful|
| US3         |MT4, MT8,  MT17 - MT19, AT14, AT15   |Successful|
| US4         |MT28, AT2                            |Successful|
| US5         |MT5, MT29 - MT32                     |Successful|
| US6         |MT7, MT24 - MT27, AT3                |Successful|
| US7         |MT5, MT35 - MT38                     |Successful|
| US8         |MT3                                  |Successful|

[Back to Contents.](#table-of-contents) 

## Future Developments

There are three potential future developments for this project.

1. To incorporate the management of the promotions, menu and about us content so the CRUD actions can be carried out on the front-end reducing the need to navigate to the admin panel.

2. Allow tables to have multiple bookings.

3. Email notifications for when a booking is created, updated, or deleted.

## Workload Planning

To manage the project, a live kanban board was used. Using this agile tool has allowed me to efficiently break down and manage the project. It has also facilitated the visualisation of the work involved, allowing the work to progress at a steady pace, and prioritise the completion of tasks before starting new ones.

The live completed board can be viewed [here.](https://github.com/users/NaveedNaseem84/projects/10)
 

## Site Production, Deployment and Contribution  

### Site production

The site was created using Gitpod’s VS Code workspace environment with all the relevant files and folder structures and migrated to the desktop version of VSCode using the instructions provide by Code Institute [here.](https://docs.google.com/document/d/e/2PACX-1vTrL4s5fkIY_SJXjazXiAd6LDKjS7uZMHwY9XW6REJ2T_DyCGRRjjmW-0p4NnkomUwAAru0vLYALohw/pub)

To deploy to GitHub, the following steps were taken:

 **Important**: Ensure the `DEBUG` is set to `False` in the project settings **before** deploying!

 The prerequisites to deployment are:
*  Install `gunicorn~=20.1` and freeze it to the requirements.txt file.
* In the `Procfile`, add a command using gunicorn and sutlans wsgi file to start the webserver in the format:
  * `web: gunicorn sultans.wsgi`
* In the `sultans/settings.py` file, append the `'.herokuapp.com'` hostname to the `ALLOWED_HOSTS` list.

**Please note:** references of sultans would need to replaced by the name of project being deployed.

The commands carried out to in the command line terminal to commit and push the changes to the GitHub repository:

1. `git add .`- (Staging the changes in the current working tree ready to be committed).

2.  `git commit -m 'Meaningful commit message"` - (The working tree is prepared with an upload message).

3.  `git push` - (changes are pushed out up to the GitHub repository).

### Deployment

The site was deployed using Heroku. The steps to deploy are as follows:

1. login to Heroku.
2. Select "create new app" .
3. Create app .
4. Select "Settings" tab at the top.
5. Scroll down to "Config Vars" and add the following keys and corresponding values:
    * `Key: DATABASE_URL`
    * `Key: SECRET_KEY`

**Note:** If you have any additional credentials, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

7. Go to the "Deploy" tab at the top.
8. Select "GitHub" as the Deployment method.
9. Select "Connect to GitHub."
10. Search for your GitHub repository and click connect. Once connected, it will show as follows:

![github-heroku](readme-images/project-walkthrough/github_heroku.png)

11. Scroll down to "Manual deploy" and click "Deploy branch". The app will start to build installing the various packages listed and the dependencies from the `requirements.txt` file. Once complete, click on the "view" button which will take you to the live site.

There is also the option to "Enable Automatic Deploys" which will build the app as soon as it is pushed to the GitHub repository and can be used if preferred.

The live link to the site can be found here: [Sultans.](https://sultans-restaurant-eaffca2215ff.herokuapp.com/)

### Contribution

I welcome any contributions, recommendations or changes to the project. To do this, the GitHub repository would need to be forked from GitHub and downloaded locally so it can be worked on.

GitHub has provided step by step instructions on how to do this [here.](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project#forking-a-repository)

[Back to Contents.](#table-of-contents) 

## Technologies and tools Used
### Languages used

* HTML
* CSS
* JavaScript
* Python
   
### Frameworks, Libraries and Programs Used
* Framework
  * #### [Django framework](https://www.djangoproject.com/)

* #### The following libraries were used:
    * Crispy forms: To allow the control and rendering of the booking form.
    * Summernote: To allow the content on the about us page to be formatted/styled independently.
    * Allauth: To allow registration, login, authentication, and logout of users. 
    * Whitenoise: To allow the project to serve its own static files.    

* #### Google Fonts: [Poppins](https://fonts.google.com/specimen/Poppins) 

  * The Poppins font was imported into the style sheet (style.css) and used throughout the project.

* #### Font Awesome: [Font awesome](https://fontawesome.com/)

  * The social media icons on the footer were placed used font awesome. The classes used are listed in the UX section.

* #### Git/Gitpod:

  * Gitpod’s workspace was used using the VSCode online editor using git to push to GitHub using version control. 

* #### VSCode:

  * Full version of VSCode using git to push to GitHub using version control post migration.

* #### GitHub:

  * GitHub has been used to store the version control repository for the project.

* #### Heroku:
  * Heroku has been used to build and deploy the project.

* #### Figma: [Figma: The Collaborative Interface Design Tool](https://figma.com/)

  * Figma has been used to create the process maps, UX illustrations of the site, and ERD's diagrams for the models.

* #### Balsamiq: [Balsamiq: Wireframe your way to faster, better product decisions ](https://balsamiq.com/)

  * Balsamiq has been used to create the wireframes.

* #### favicon.io: [favicon.io](https://favicon.io/favicon-converter/)
  * Used to create the favicons from an image (Image credited below).

* The code has been formatted using the following extensions within VSCode:
  * Prettier
  * Flake8
  * Ruff

* #### Adobe Photoshop:

  * Adobe has been used to apply the blur effect to the images.

* #### [TinyPNG – Compress WebP, PNG and JPEG images intelligently.](https://tinypng.com/)
  * Tiny PNG was used to optimise the images for web use. 


[Back to Contents.](#table-of-contents)    

## Credits
* The background used on the home and about page was taken from: [Assorted Spices on the Table - Pexels.](https://www.pexels.com/photo/assorted-spices-on-the-table-5740292/)

* The background used on menu page was taken from: [Rich Indian Lamb Curry in Traditional Metal Bowl - Pexels.](https://www.pexels.com/photo/rich-indian-lamb-curry-in-traditional-metal-bowl-28674690/)

* The image used to create the favicon was taken from: [FlatIcon.](https://www.flaticon.com/free-icon/cutlery_1690261?related_id=1689974&origin=search)

* Inspiration for the menu was taken from : [Indian Tiffin Room.](https://indiantiffinroom.com/manchester/)

* The navigation arrow image was taken from : [SVG Repo-Down Arrow SVG Vector.](https://www.svgrepo.com/svg/403209/down-arrow)

### Content

* The general setup and structure for the project was completed following the guidance provided in the [I think Therefore I Blog - CI Project.](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+6/courseware/713441aba05441dfb3a7cf04f3268b3f/824fccecd0fe4e44871eeabcbf69d830/)

* The core Bootstrap navbar in the `base.html` template was implemented using the [Bootstrap documentation on Navbar](https://getbootstrap.com/docs/5.0/components/navbar/)  and customised to my project requirements.

* Within the header -> nav section on the `base.html` template, the implementation of the nav-link if statement to determine if the current page is active or not was taken from [I Think Therefore I Blog > Templates -> Variable and control structures - CI Project.](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+6/courseware/713441aba05441dfb3a7cf04f3268b3f/6b4a4f493cbd46ecb6f6a841c98f0c82/?child=first)
  * The code used: 
    ```<a class="nav-link
        {% if request.path == home_url %}active{%endif%}" aria-current="page" href="{% url 'home' %}">
    ```
  * The code above was refined further for accessibility and the correct classes applied to the Django messages by following the video [I Think Therefore I Blog > Where to put things > Tidying up - CI Project.](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+6/courseware/713441aba05441dfb3a7cf04f3268b3f/0b5c6f09dcfd40fa99a9d68622d62b40/)

* The implementation of the admin link on the nav bar within the `base.html` template was done using [Linking to the Django admin site - Stack Overflow.](https://stackoverflow.com/questions/1022236/linking-to-the-django-admin-site/1026680#1026680)


* Implementation and setup (including adding links to the nav-bar and authentication messages displayed in the `base.html` template) of the Django Allauth authentication was done using [I think before I Blog > Authentication > Introduction to authentication - CI Project.](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+6/courseware/713441aba05441dfb3a7cf04f3268b3f/f614040ed41a49dbb268f0102af9ce05/)
  * The standard register, login, logout allauth templates were customised to match the needs of the project.

* The Django messages in the `base.html` template were displayed by adapting the code from  [I Think Therefore I Blog > Views Part 3>POSTing and writing to the database - CI Project.](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+6/courseware/713441aba05441dfb3a7cf04f3268b3f/21a16093c0084895a6073422447c3f7d/?child=first)

  * The code utilised:
  ```
  ....
  {% for message in messages %}
      <div class="alert {{ message.tags }} alert-dismissible
        fade show" id="msg" role="alert">
        {{ message | safe }}
        <button type="button" class="btn-close"
          data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
      {% endfor %}
  ....
  ```
  * This was further refined in line with the project.

* The core Bootstrap modal was implemented using the [Bootstrap documentation on Modal.](https://getbootstrap.com/docs/5.0/components/modal/)
 
* The structure to update/delete bookings (JavaScript and Python) was taken from [I Think Before I Blog > Views Part 3 > Editing and deleting records - CI Project.](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+6/courseware/713441aba05441dfb3a7cf04f3268b3f/21a16093c0084895a6073422447c3f7d/?child=first)

* The use of pluralize in the `book/book.html` template was implemented using [Template Filter - pluralize - w3schools.](https://www.w3schools.com/django/ref_filters_pluralize.php)

* The core Bootstrap accordion on the `menu/menu.html` was implemented using [Bootstrap document on Accordion - flush.](https://getbootstrap.com/docs/5.0/components/accordion/)
  * This was further customised in line with the project.

* The regex validation on the `book.MakeBooking` `phone` field within `book/models.py` was adapted from [How to use RegEx Validator in Django - Geeks for Geeks.](https://www.geeksforgeeks.org/how-to-use-regex-validator-in-django/)

* Accessing the messages within the unit testing was implemented from [How can I unit test Django messages? - Stack overflow.](https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages )
  * The code utilised:
  ```
  from django.contrib.messages import get_messages
  ....
  messages = [m.message for m in get_messages(response.wsgi_request)]
  self.assertIn('My message', messages)
  ```
  * Accessing the messages ensured the unit testing results were correct.

* The placement of a custom 404 page was done by following [Customizing Django 404 and 500 Error Pages - LearnDjango](https://learndjango.com/tutorials/customizing-django-404-and-500-error-pages)


### General

* The following resources have been used as a general guide for Django, Python:
  * [Django official documentation](https://docs.djangoproject.com/en/5.1/)  
  * [Django Tutorial - W3Schools](https://www.w3schools.com/django/)
  * [Python official Documentation](https://docs.python.org/3/)
  * [Python Tutorial - W3Schools](https://www.w3schools.com/python/)
  * [Python Tutor](https://pythontutor.com/visualize.html#mode=edit)

## Overall Credit

A thank you to Code Institute for the learning curve, and lesson material, which has been incredible and my fellow students on Slack for their continued support!

I also would like to give a special thanks to the Tutor Assistance team at Code Institute for all their help on getting back on track during the migration period.


## Personal Summary

This project by far has brought the steepest learning curve. The whole new world of models, views and templates seemed to bring with it a whole new level of confusion! Taking the time to go over the detailed content material available repeatedly in small iterations has resulted in the project that can be seen here. A massive thank you to my legend of a mentor who not only gave invaluable advice but allowed me to push myself further to refine my work, and as an individual on my coding journey.

The main take away point from this project has been around the value of using agile methodology and tools to manage the project through to completion. I aim to look at refining this further by breaking future projects down into multiple milestones and refining Epics to User Stories to Tasks.

[Back to Contents.](#table-of-contents) 