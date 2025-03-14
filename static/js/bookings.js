//JS to allow the deleting and updating of bookings

//globals for the edit, delete and modal delete confirm button
const deleteButtons = document.getElementsByClassName("btn-delete-booking");
const editButtons = document.getElementsByClassName("btn-update-booking");
const deleteConfirm = document.getElementById("deleteConfirmation");

/**
 * Apply event listener when the DOM loads.
 */
document.addEventListener("DOMContentLoaded", applyUpdateDeleteEventListener);

/**
 * Apply event listener to all the delete and update buttons.
 * Delete buttons: call deleteBooking
 * Update buttons: call EditBooking
 *
 */
function applyUpdateDeleteEventListener() {
  for (let button of deleteButtons) {
    button.addEventListener("click", deleteBooking);
  }

  for (let button of editButtons) {
    button.addEventListener("click", editBooking);
  }
}

/**
 * Delete the selected booking
 * bookingId: ID of booking retrieved from delete button
 * call Book.views.Delete_booking to process passing bookingId
 */
function deleteBooking() {
  let bookingId = this.getAttribute("data-booking-id");
  deleteConfirm.addEventListener("click", () => {
    if (bookingId) {
      window.location.href = `delete_booking/${bookingId}`;
    }
  });
}

/**
 * update the selected booking
 * bookingId: ID of booking retrieved from update button
 * call Book.view.update_booking to process passing bookingId
 */

function editBooking() {
  let bookingId = this.getAttribute("data-booking-id");
  window.location.href = `update_booking/${bookingId}`;
}
