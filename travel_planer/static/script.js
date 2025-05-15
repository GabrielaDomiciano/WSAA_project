// ========== AJAX calls ==========

function getAll(callback) {
    $.ajax({
        url: "/api/trips",
        method: "GET",
        dataType: "JSON",
        success: function (result) {
            callback(result);
        },
        error: function (xhr, status, error) {
            console.log("GET error: " + status + " - " + error);
        }
    });
}

function createTrip(trip, callback) {
    $.ajax({
        url: "/api/trips",
        method: "POST",
        data: JSON.stringify(trip),
        dataType: "JSON",
        contentType: "application/json; charset=utf-8",
        success: function (result) {
            callback(result);
        },
        error: function (xhr, status, error) {
            console.log("POST error: " + status + " - " + error);
        }
    });
}

function updateTrip(trip, callback) {
    $.ajax({
        url: "/api/trips/" + encodeURIComponent(trip.id),
        method: "PUT",
        data: JSON.stringify(trip),
        dataType: "JSON",
        contentType: "application/json; charset=utf-8",
        success: function (result) {
            callback(result);
        },
        error: function (xhr, status, error) {
            console.log("PUT error: " + status + " - " + error);
        }
    });
}

function deleteTrip(id, callback) {
    $.ajax({
        url: "/api/trips/" + id,
        method: "DELETE",
        dataType: "JSON",
        contentType: "application/json; charset=utf-8",
        success: function (result) {
            callback(result);
        },
        error: function (xhr, status, error) {
            console.log("DELETE error: " + status + " - " + error);
        }
    });
}

// ========== View Logic ==========

function showCreate() {
    $("#createUpdateForm").show();
    $("#button-doCreate").show();
    $("#button-doUpdate").hide();
    $("#createLabel").show();
    $("#updateLabel").hide();
    $("#button-showCreate").hide();
    $("#tripTable").hide();
    clearForm();
}

function showUpdate(buttonElement) {
    $("#createUpdateForm").show();
    $("#button-doCreate").hide();
    $("#button-doUpdate").show();
    $("#createLabel").hide();
    $("#updateLabel").show();
    $("#button-showCreate").hide();
    $("#tripTable").hide();

    let row = buttonElement.parentNode.parentNode;
    let trip = getTripFromRow(row);
    populateFormWithTrip(trip);
}

function showViewAll() {
    $("#createUpdateForm").hide();
    $("#button-showCreate").show();
    $("#tripTable").show();
}

function clearForm() {
    let form = $("#createUpdateForm");
    form.find("input[name='id']").prop("disabled", false).val('');
    form.find("input[name='trip_name']").val('');
    form.find("input[name='destination']").val('');
    form.find("input[name='start_date']").val('');
    form.find("input[name='end_date']").val('');
}

function getTripFromForm() {
    let form = $("#createUpdateForm");
    return {
        id: form.find("input[name='id']").val(),
        trip_name: form.find("input[name='trip_name']").val(),
        destination: form.find("input[name='destination']").val(),
        start_date: form.find("input[name='start_date']").val(),
        end_date: form.find("input[name='end_date']").val()
    };
}

function populateFormWithTrip(trip) {
    let form = $("#createUpdateForm");
    form.find("input[name='id']").val(trip.id).prop("disabled", true);
    form.find("input[name='trip_name']").val(trip.trip_name);
    form.find("input[name='destination']").val(trip.destination);
    form.find("input[name='start_date']").val(trip.start_date);
    form.find("input[name='end_date']").val(trip.end_date);
}

function addTripToTable(trip) {
    let table = $("#tripTable");
    let row = $("<tr>").attr("id", trip.id);
    row.append($("<td>").text(trip.id));
    row.append($("<td>").text(trip.trip_name));
    row.append($("<td>").text(trip.destination));
    row.append($("<td>").text(trip.start_date));
    row.append($("<td>").text(trip.end_date));
    row.append($("<td>").html('<button onclick="showUpdate(this)">Update</button>'));
    row.append($("<td>").html('<button onclick="doDelete(this)">Delete</button>'));
    table.append(row);
}

function getTripFromRow(rowElement) {
    let cells = rowElement.cells;
    return {
        id: cells[0].innerText,
        trip_name: cells[1].innerText,
        destination: cells[2].innerText,
        start_date: cells[3].innerText,
        end_date: cells[4].innerText
    };
}

function setTripInRow(rowElement, trip) {
    let cells = rowElement.cells;
    cells[1].innerText = trip.trip_name;
    cells[2].innerText = trip.destination;
    cells[3].innerText = trip.start_date;
    cells[4].innerText = trip.end_date;
}

// ========== Actions ==========

function doCreate() {
    let trip = getTripFromForm();
    createTrip(trip, function (createdTrip) {
        addTripToTable(createdTrip);
        showViewAll();
        clearForm();
    });
}

function doUpdate() {
    let trip = getTripFromForm();
    updateTrip(trip, function () {
        let row = document.getElementById(trip.id);
        setTripInRow(row, trip);
        showViewAll();
        clearForm();
    });
}

function doDelete(buttonElement) {
    let row = buttonElement.parentNode.parentNode;
    let id = row.getAttribute("id");
    deleteTrip(id, function () {
        row.remove();
    });
}

// ========== Initial Load ==========

function processGetAllResponse(result) {
    result.forEach(trip => {
        addTripToTable(trip);
    });
}

getAll(processGetAllResponse);

