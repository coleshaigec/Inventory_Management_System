const { spawn } = require('child_process');
const { ipcRenderer } = require('electron');


let abc = 1;
let page = 0;
const pageSize = 50;
let loading = false;
const container = document.getElementById('table-body');

ipcRenderer.on('sale_table_success', (event, data) => {
	abc ++;
	const our_data = JSON.parse(data.dataset);
	if (loading) {
		const tbody = document.getElementById('table-body');
		our_data.forEach((item) => {
			const tr = document.createElement('tr');
			tr.innerHTML = `
				<td>${item.date}</td>
				<td>${item.SKU}</td>
				<td>${item.product_name}</td>
				<td>${item.cost}</td>
				<td>${item.num || 'N/A'}</td>
				`;
			tbody.appendChild(tr);
		});
		page++;
		loading = false;
	}
});


window.addEventListener('scroll', () => {
	if (window.scrollY + window.innerHeight >= window.documentElement.scrollHeight - 20) { // Adjust as needed
			if (!loading) { // Prevent duplicate calls
				console.log("called more");
				loading = true;
				ipcRenderer.send('create-sale-table', {abc});
  //Ensure this increments correctly for pagination
			}
		
	}
});

if (!loading){
	loading = true;
	ipcRenderer.send('create-sale-table', {abc});
}


