// ========== AJAX calls ==========

function getAll(callback) {
    $.ajax({
        url: "/trips",
        method: "GET",
        dataType: "JSON",
        success: function (result) {
            callback(result);
        },
        error: function (xhr, status, error) {
            console.log("GET error: " + status + " msg:" + error);
        }
    });
}

function createTrip(trip, callback) {
    $.ajax({
        url: "/trips",
        method: "POST",
        data: JSON.stringify(trip),
        contentType: "application/json; charset=utf-8",
        dataType: "JSON",
        success: function (result) {
            callback(result);
        },
        error: function (xhr, status, error) {
            console.log("POST error: " + status + " msg:" + error);
        }
    });
}

function updateTrip(trip, callback) {
    $.ajax({
        url: "/trips/" + encodeURIComponent(trip.id),
        method: "PUT",
        data: JSON.stringify(trip),
        contentType: "application/json; charset=utf-8",
        dataType: "JSON",
        success: function (result) {
            callback(result);
        },
        error: function (xhr, status, error) {
            console.log("PUT error: " + status + " msg:" + error);
        }
    });
}

function deleteTrip(id, callback) {
    $.ajax({
        url: "/trips/" + id,
        method: "DELETE",
        contentType: "application/json; charset=utf-8",
        dataType: "JSON",
        success: function (result) {
            callback(result);
        },
        error: function (xhr, status, error) {
            console.log("DELETE error: " + status + " msg:" + error);
        }
    });
}

// ========== UI Logic ==========

function showCreate() {
    document.getElementById("createUpdateForm").style.display = "block";

    document.getElementById("button-doCreate").style.display = "inline";
    document.getElementById("button-doUpdate").style.display = "none";
    document.getElementById("createLabel").style.display = "inline";
    document.getElementById("updateLabel").style.display = "none";

    document.getElementById("button-showCreate").style.display = "none";
    document.getElementById("tripTable").style.display = "none";

    clearForm();
}

function showUpdate(buttonElement) {
    document.getElementById("createUpdateForm").style.display = "block";

    document.getElementById("button-doCreate").style.display = "none";
    document.getElementById("button-doUpdate").style.display = "inline";
    document.getElementById("createLabel").style.display = "none";
    document.getElementById("updateLabel").style.display = "inline";

    document.getElementById("button-showCreate").style.display = "none";
    document.getElementById("tripTable").style.display = "none";

    let row = buttonElement.parentNode.parentNode;
    let trip = getTripFromRow(row);
    populateFormWithTrip(trip);
}

function showViewAll() {
    document.getElementById("createUpdateForm").style.display = "none";
    document.getElementById("button-showCreate").style.display = "block";
    document.getElementById("tripTable").style.display = "table";
}

function clearForm() {
    let form = document.getElementById("createUpdateForm");
    form.querySelector('input[name="id"]').disabled = false;
    form.querySelector('input[name="id"]').value = '';
    form.querySelector('input[name="trip_name"]').value = '';
    form.querySelector('input[name="destination"]').value = '';
    form.querySelector('input[name="start_date"]').value = '';
    form.querySelector('input[name="end_date"]').value = '';
}

function getTripFromForm() {
    let form = document.getElementById("createUpdateForm");
    let trip = {};
    trip.id = form.querySelector('input[name="id"]').value;
    trip.trip_name = form.querySelector('input[name="trip_name"]').value;
    trip.destination = form.querySelector('input[name="destination"]').value;
    trip.start_date = form.querySelector('input[name="start_date"]').value;
    trip.end_date = form.querySelector('input[name="end_date"]').value;
    return trip;
}

function populateFormWithTrip(trip) {
    let form = document.getElementById("createUpdateForm");
    form.querySelector('input[name="id"]').disabled = true;
    form.querySelector('input[name="id"]').value = trip.id;
    form.querySelector('input[name="trip_name"]').value = trip.trip_name;
    form.querySelector('input[name="destination"]').value = trip.destination;
    form.querySelector('input[name="start_date"]').value = trip.start_date;
    form.querySelector('input[name="end_date"]').value = trip.end_date;
}

function addTripToTable(trip) {
    let table = document.getElementById("tripTable");
    let row = table.insertRow(-1);
    row.setAttribute("id", trip.id);

    row.insertCell(0).innerText = trip.id;
    row.insertCell(1).innerText = trip.trip_name;
    row.insertCell(2).innerText = trip.destination;
    row.insertCell(3).innerText = trip.start_date;
    row.insertCell(4).innerText = trip.end_date;
    row.insertCell(5).innerHTML = '<button onclick="showUpdate(this)">Update</button>';
    row.insertCell(6).innerHTML = '<button onclick="doDelete(this)">Delete</button>';
}

function getTripFromRow(row) {
    let trip = {};
    trip.id = row.cells[0].innerText;
    trip.trip_name = row.cells[1].innerText;
    trip.destination = row.cells[2].innerText;
    trip.start_date = row.cells[3].innerText;
    trip.end_date = row.cells[4].innerText;
    return trip;
}

function setTripInRow(row, trip) {
    row.cells[1].innerText = trip.trip_name;
    row.cells[2].innerText = trip.destination;
    row.cells[3].innerText = trip.start_date;
    row.cells[4].innerText = trip.end_date;
}

// ========== Actions ==========

function doCreate() {
    let trip = getTripFromForm();
    createTrip(trip, processCreateResponse);
}

function doUpdate() {
    let trip = getTripFromForm();
    updateTrip(trip, processUpdateResponse);
}

function doDelete(buttonElement) {
    let row = buttonElement.parentNode.parentNode;
    let id = row.getAttribute("id");
    deleteTrip(id, processDeleteResponse);
    row.remove();
}

// ========== Response Callbacks ==========

function processGetAllResponse(result) {
    for (let trip of result) {
        addTripToTable(trip);
    }
}

function processCreateResponse(result) {
    addTripToTable(result);
    showViewAll();
    clearForm();
}

function processUpdateResponse(result) {
    let row = document.getElementById(result.id);
    setTripInRow(row, result);
    showViewAll();
    clearForm();
}

function processDeleteResponse(result) {
    console.log("Deleted:", result);
}

function doNothing(result) {
    console.log("Callback result:", result);
}

// ========== Initial Load ==========

getAll(processGetAllResponse);


