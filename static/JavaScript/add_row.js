function addRow() {
const table = document.getElementById('tbody');
const row = table.insertRow();

const cell1 = row.insertCell(0);
const cell2 = row.insertCell(1);

cell1.innerHTML = '<input type="text" name="terms" value="">';
cell2.innerHTML = '<input type="text" name="defs" value="">';
}

function removeRow(button) {
const row = button.closest('tr');
row.remove();
}