//JS to allow the deleting and updating of bookings

//globals for the edit and delete buttons
const deleteButtons = document.getElementsByClassName("btn-delete-booking");
const editButtons = document.getElementsByClassName("btn-update-booking");

//apply event listener as soon as the DOM loads
document.addEventListener("DOMContentLoaded", applyEventListener);

//Apply event listen to all delete/update buttons
function applyEventListener() {
  for (let button of deleteButtons) {
    button.addEventListener("click", deleteBooking);
  }

  for (let button of editButtons) {
    button.addEventListener("click", editBooking);
  }
}

//delete the selected booking. Tested using booking ID
// to ensure the delete button pressed corresponds to the 
//booking in question
//
function deleteBooking() {
  let bookingId = this.getAttribute("data-booking-id");
  console.log("Delete id: " + bookingId);
}

//update the selected booking. Tested using booking ID
// to ensure the update button pressed corresponds to the 
//booking in question
//

function editBooking() {
  let bookingId = this.getAttribute("data-booking-id");
  console.log("update id: " + bookingId);
  
}
