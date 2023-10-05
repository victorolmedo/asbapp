let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6] },
        { orderable: false, targets: [5, 6] },
        { searchable: false, targets: [4, 5, 6] }
    ],
    pageLength: 4,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listCustomers();

    dataTable = $("#datatable-customers").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listCustomers = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/customers/");
        const data = await response.json();

        let content = ``;
        data.forEach((customer, index) => {
            content += `
                <tr>
                    <td>${customer.id}</td>
                    <td>${customer.first_name} ${customer.last_name}</td>
                    <td>${customer.email}</td>
                    <td>${customer.phone}</td>
                    <td>${customer.active == true
                        ? "<i class='fa-solid fa-check' style='color: green;'></i>"
                        : "<i class='fa-solid fa-xmark' style='color: red;'></i>"}
                    </td>
                    <td>
                        <button class='btn btn-sm btn-primary'><i class='fa-solid fa-pencil'  data-bs-toggle='modal' data-bs-target='#myModal'></i></button>
                        <button class='btn btn-sm btn-danger'><i class='fa-solid fa-trash-can' data-bs-toggle='modal' data-bs-target='#myModal'></i></button>
                    </td>
                    <td></td>
                </tr>`;
        });
        tableBody_customers.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});

$('#myModal').on('shown.bs.modal', function () {
// Do something when the modal is shown
});
