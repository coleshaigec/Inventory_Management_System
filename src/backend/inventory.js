const { spawn } = require('child_process');
const {ipcRenderer} = require("electron");

// function runPythonScript(scriptPath="../database/Product.py", args) {
//     const python = spawn('python', [scriptPath, args]);


// let dataString = '';
// python.stdout.on('data', (data) => {
//     dataString += data.toString();
//     //console.log(dataString);
// });

// python.stdout.on('end', () => {
//     //const dataconvert = JSON.parse(dataString);
//     // app.get('/data', (req, res) => {
//     //     res.json(dataconvert); // send data to front-end
//     // });
// });

// python.stderr.on('data', (data) => {
//     console.error(`stderr: ${data}`);
// });

// python.on('close', (code) => {
//     console.log(`child process exited with code ${code}`);
// });

// }

//
// console.log(runPythonScript("../database/Product.py", ["printAll"])); // replace "argument1" with the actual argument you want to pass to the script

function addHTMLrow(data) {
var table = document.getElementById('inventory_table');

table.innerHTML += "<li class=\"table-row\">"
 + "<div class=\"col col-1\" data-label=\"SKU\">" + data.SKU + "</div>"
 + "<div class=\"col col-2\" data-label=\"Name\">" + data.product_name + "</div>"
 + "<div class=\"col col-3\" data-label=\"In Stock\">" + data.stock + "</div>"
 + "<div class=\"col col-4\" data-label=\"On Order\">" + data.SKU_Class + "</div>"
 + "<div class=\"col col-5\" data-label=\"Unit Cost\">" + data.cost + "</div>"
 + "<div class=\"col col-6\" data-label=\"Inventory Value\">" + data.inventory_value + "</div>"
 + "<div class=\"col col-7\" data-label=\"Expected Sales\">" + data.expected_sales + "</div> " + "</li>";
}

document.getElementById('load').addEventListener('click', (event) => {
    event.preventDefault();
    const message = "printALL";
  
    ipcRenderer.send('create-table', {message});
  });

ipcRenderer.on('table_success', (event, data) => {
    const our_data = JSON.parse(data.dataset);
    const number_data = our_data.length;
    for(let i = 0; i < number_data; i++){
        addHTMLrow(our_data[i]);
    }
    document.getElementById('load').disabled = false;
});