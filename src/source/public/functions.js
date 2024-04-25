const { ipcRenderer } = require('electron');

ipcRenderer.on('login-success', (event, arg) => {
    window.location.href = '../views/map.html';
    remote.app.emit('map-page');
   });

ipcRenderer.on('login-failure', (event, data) => {
    if (data.attemptsLeft > 0) {
        document.getElementById('message').textContent = `Login failed. Attempts left: ${data.attemptsLeft}`;
    } else {
        document.getElementById('message').textContent = 'You have exceeded the number of login attempts.';
    }
});

ipcRenderer.on('login-attempt-exceeded', () => {
    document.getElementById('message').textContent = 'You have exceeded the number of login attempts.';
    window.location.href = '../views/index.html';
    remote.app.emit('main-page');
});

ipcRenderer.on('reset-login', (event,arg) => {
    document.getElementById('message').textContent = '';
    document.getElementById('username').value = '';
    document.getElementById('password').value = '';
    document.getElementById('loginButton').disabled = false;
});

ipcRenderer.on('register_success', (event,data) => {
    window.location.href = '../views/index.html';
    remote.app.emit('main-page');
});

ipcRenderer.on('register-failure', (event, data) => {
    const our_data = data.response;
    document.getElementById('message_register').textContent = our_data;
});

ipcRenderer.on('reset-register', () => {
    document.getElementById('message').textContent = '';
    document.getElementById('username').value = '';
    document.getElementById('password').value = '';
    document.getElementById('status').value = '';
    document.getElementById('loginButton').disabled = false;
});
