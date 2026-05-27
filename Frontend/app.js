const storage = {
    get(key, fallback) {
        try {
            const item = window.localStorage.getItem(key);
            return item ? JSON.parse(item) : fallback;
        } catch (error) {
            return fallback;
        }
    },
    set(key, value) {
        window.localStorage.setItem(key, JSON.stringify(value));
    }
};

const defaultData = {
    asesorias: [
        { id: 1, nombre: 'Juan', materia: 'POO', profesor: 'Mario', horario: '9AM' },
        { id: 2, nombre: 'Ana', materia: 'BD', profesor: 'Laura', horario: '10AM' },
        { id: 3, nombre: 'Luis', materia: 'Redes', profesor: 'Jose', horario: '11AM' }
    ],
    misAsesorias: [
        { id: 101, nombre: 'Carlos', materia: 'Redes', profesor: 'Jose', horario: '1PM' },
        { id: 102, nombre: 'Sofia', materia: 'Web', profesor: 'Maria', horario: '3PM' }
    ],
    solicitudes: [
        { id: 201, alumno: 'Pedro', materia: 'IA', estado: 'Pendiente', hora: '5PM' },
        { id: 202, alumno: 'Fernanda', materia: 'Web', estado: 'Aprobada', hora: '6PM' }
    ]
};

let toastTimer = null;

function getToastElement() {
    let toast = document.getElementById('pageToast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'pageToast';
        toast.className = 'toast-message';
        document.body.appendChild(toast);
    }
    return toast;
}

function showMessage(target, message, success = true) {
    if (!target || target === document.body || target === document.documentElement) {
        target = getToastElement();
    }

    if (typeof target === 'string') {
        target = getToastElement();
    }

    target.textContent = message;
    target.classList.toggle('success', success);
    target.classList.toggle('error', !success);

    if (toastTimer) {
        clearTimeout(toastTimer);
    }

    toastTimer = setTimeout(() => {
        if (target.id === 'pageToast') {
            target.textContent = '';
            target.classList.remove('success', 'error');
        } else {
            target.textContent = '';
            target.classList.remove('success', 'error');
        }
    }, 4200);
}

function navigateMenu() {
    document.querySelectorAll('.menu a[data-nav]').forEach(link => {
        link.addEventListener('click', event => {
            event.preventDefault();
            const target = link.dataset.nav;
            if (target) {
                window.location.href = target;
            }
        });
    });
}

function initLogin() {
    const form = document.getElementById('loginForm');
    const user = document.getElementById('loginUser');
    const password = document.getElementById('loginPassword');
    const code = document.getElementById('loginCode');
    const message = document.getElementById('loginMessage');
    const users = storage.get('registeredUsers', []);

    if (!form) return;

    // Submit the login form to the backend. Validate client-side then allow default submit.
    form.addEventListener('submit', event => {
        const username = user.value.trim();
        const passwordValue = password.value.trim();
        const codeValue = code.value.trim();

        if (!username || !passwordValue || !codeValue) {
            event.preventDefault();
            showMessage(message, 'Completa todos los campos para ingresar.', false);
            return;
        }

        // Ensure the form posts to the backend root login endpoint
        form.action = 'http://localhost:8000/';
        form.method = 'post';
        // Allow normal submit to let Django render the next page (no fetch here to avoid CSRF complexity)
    });
}

function initRegister() {
    const form = document.getElementById('registerForm');
    const nameInput = document.getElementById('registerName');
    const emailInput = document.getElementById('registerEmail');
    const userInput = document.getElementById('registerUser');
    const careerInput = document.getElementById('registerCareer');
    const passwordInput = document.getElementById('registerPassword');
    const codeInput = document.getElementById('registerCode');
    const switchToggle = document.getElementById('typeSwitch');
    const codeDigits = Array.from(document.querySelectorAll('.code-digit'));
    const message = document.getElementById('registerMessage');

    if (!form) return;

    switchToggle.addEventListener('click', () => {
        switchToggle.classList.toggle('active');
        const type = switchToggle.classList.contains('active') ? 'Profesor' : 'Estudiante';
        switchToggle.setAttribute('title', `Tipo: ${type}`);
        // Toggle tarifa input visibility and form action
        const tarifaInput = document.getElementById('registerTarifa');
        if (switchToggle.classList.contains('active')) {
            tarifaInput.style.display = '';
            form.action = 'http://localhost:8000/registro/asesor/';
        } else {
            tarifaInput.style.display = 'none';
            form.action = 'http://localhost:8000/registro/asesorado/';
        }
    });

    switchToggle.addEventListener('keydown', event => {
        if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            switchToggle.click();
        }
    });

    codeDigits.forEach((input, index) => {
        input.addEventListener('input', () => {
            input.value = input.value.replace(/[^0-9a-zA-Z]/g, '').slice(0, 1);
            if (input.value && index < codeDigits.length - 1) {
                codeDigits[index + 1].focus();
            }
            codeInput.value = codeDigits.map(d => d.value).join('');
        });
    });

    form.addEventListener('submit', event => {
        // Client-side validation; if valid, let the form submit to the backend.
        if (!nameInput.value.trim() || !emailInput.value.trim() || !userInput.value.trim() || !passwordInput.value.trim() || !codeInput.value.trim()) {
            event.preventDefault();
            showMessage(message, 'Completa todos los campos y el código.', false);
            return;
        }

        // Ensure form action is set according to selected type (the switch handler keeps it in sync)
        if (switchToggle.classList.contains('active')) {
            form.action = 'http://localhost:8000/registro/asesor/';
        } else {
            form.action = 'http://localhost:8000/registro/asesorado/';
        }

        // If user is registering as Asesor, copy tarifa input into a named field (already present in DOM)
        // Allow default submit so backend handles creation and response (avoids CSRF token management here).
    });
}

function renderTableRows(items, tbodyId, createRow) {
    const tbody = document.getElementById(tbodyId);
    if (!tbody) return;
    tbody.innerHTML = items.map(item => createRow(item)).join('');
}

function initAsesorias() {
    // Fetch available advisors and existing asesorias from backend
    let available = [];
    let mine = [];

    const renderLists = () => {
        renderTableRows(available, 'availableTableBody', item => `
            <tr>
                <td>${item.nombre}</td>
                <td>${item.materia}</td>
                <td>${item.profesor}</td>
                <td>${item.horario || ''}</td>
                <td><button class="action-btn" data-action="request" data-id="${item.id}">Solicitar</button></td>
            </tr>
        `);

        renderTableRows(mine, 'myTableBody', item => `
            <tr>
                <td>${item.nombre}</td>
                <td>${item.materia}</td>
                <td>${item.profesor}</td>
                <td>${item.horario || ''}</td>
                <td><button class="action-btn" data-action="cancel" data-id="${item.id}">Cancelar</button></td>
            </tr>
        `);
    };

    // Load advisors
    fetch('http://localhost:8000/api/asesores/')
        .then(r => r.json())
        .then(payload => {
            const items = payload.asesores || [];
            available = items.map(a => ({
                id: a.id,
                nombre: a.nombre,
                materia: a.materia || '',
                profesor: a.profesor || '',
                horario: ''
            }));
            renderLists();
        })
        .catch(err => {
            console.error('Failed to load asesores', err);
            available = storage.get('asesoriasAvailable', defaultData.asesorias);
            renderLists();
        });

    // Load asesorias (reservations/solicitudes)
    fetch('http://localhost:8000/api/asesorias/')
        .then(r => r.json())
        .then(payload => {
            const items = payload.asesorias || [];
            // consider confirmed asesorias as "mine" for now
            mine = items.filter(i => i.confirmada).map(i => ({
                id: i.id,
                nombre: i.asesorado_nombre,
                materia: i.materia || '',
                profesor: i.asesor_nombre || '',
                horario: i.hora || ''
            }));
            renderLists();
        })
        .catch(err => {
            console.error('Failed to load asesorias', err);
            mine = storage.get('asesoriasMine', defaultData.misAsesorias);
            renderLists();
        });

    document.getElementById('availableTableBody').addEventListener('click', event => {
        const button = event.target.closest('button[data-action="request"]');
        if (!button) return;
        const id = Number(button.dataset.id);
        const selected = available.find(item => item.id === id);
        if (!selected) return;

        available.splice(available.indexOf(selected), 1);
        mine.push(selected);
        storage.set('asesoriasAvailable', available);
        storage.set('asesoriasMine', mine);
        renderLists();
        showMessage(null, 'Asesoría solicitada. Revisa Mis Asesorias.');
    });

    document.getElementById('myTableBody').addEventListener('click', event => {
        const button = event.target.closest('button[data-action="cancel"]');
        if (!button) return;
        const id = Number(button.dataset.id);
        const selected = mine.find(item => item.id === id);
        if (!selected) return;

        mine.splice(mine.indexOf(selected), 1);
        available.push(selected);
        storage.set('asesoriasAvailable', available);
        storage.set('asesoriasMine', mine);
        renderLists();
        showMessage(null, 'Asesoría cancelada y disponible de nuevo.');
    });
}

function initSolicitudes() {
    let solicitudes = [];
    let asesorias = [];

    const renderAsesorias = () => {
        renderTableRows(asesorias, 'asesoriasBody', item => `
            <tr>
                <td>${item.nombre}</td>
                <td>${item.materia}</td>
                <td>${item.profesor}</td>
                <td>${item.horario || ''}</td>
            </tr>
        `);
    };

    const renderSolicitudes = () => {
        renderTableRows(solicitudes, 'solicitudesBody', item => `
            <tr>
                <td>${item.alumno}</td>
                <td>${item.materia}</td>
                <td>${item.estado}</td>
                <td>${item.hora}</td>
                <td>
                    ${item.estado === 'Pendiente'
                        ? `<button class="action-btn" data-action="approve" data-id="${item.id}">Aprobar</button>
                           <button class="action-btn" data-action="reject" data-id="${item.id}">Rechazar</button>`
                        : '<span class="status-tag">Sin acción</span>'}
                </td>
            </tr>
        `);
    };

    // Load asesorias for display
    fetch('http://localhost:8000/api/asesorias/')
        .then(r => r.json())
        .then(payload => {
            const items = payload.asesorias || [];
            asesorias = items.map(i => ({
                id: i.id,
                nombre: i.asesor_nombre,
                materia: i.materia || '',
                profesor: i.asesor_nombre || '',
                horario: i.hora || ''
            }));
            renderAsesorias();
        })
        .catch(err => {
            console.error('Failed to load asesorias', err);
            asesorias = storage.get('asesoriasAvailable', defaultData.asesorias);
            renderAsesorias();
        });

    // Load solicitudes
    fetch('http://localhost:8000/api/solicitudes/')
        .then(r => r.json())
        .then(payload => {
            const items = payload.solicitudes || [];
            solicitudes = items.map(s => ({
                id: s.id,
                alumno: s.alumno,
                materia: s.materia || '',
                estado: s.estado || '',
                hora: s.hora || ''
            }));
            renderSolicitudes();
        })
        .catch(err => {
            console.error('Failed to load solicitudes', err);
            solicitudes = storage.get('solicitudes', defaultData.solicitudes);
            renderSolicitudes();
        });

    document.getElementById('solicitudesBody').addEventListener('click', event => {
        const approve = event.target.closest('button[data-action="approve"]');
        const reject = event.target.closest('button[data-action="reject"]');
        if (!approve && !reject) return;

        const id = Number((approve || reject).dataset.id);
        const solicitud = solicitudes.find(item => item.id === id);
        if (!solicitud) return;

        solicitud.estado = approve ? 'Aprobada' : 'Rechazada';
        renderSolicitudes();
        showMessage(null, `Solicitud ${solicitud.estado.toLowerCase()}.`, true);
    });
}

function initApp() {
    navigateMenu();

    const page = document.body.dataset.page;
    switch (page) {
        case 'login':
            initLogin();
            break;
        case 'registro':
            initRegister();
            break;
        case 'asesorias':
            initAsesorias();
            break;
        case 'solicitudes':
            initSolicitudes();
            break;
        default:
            break;
    }
}

window.addEventListener('DOMContentLoaded', initApp);
