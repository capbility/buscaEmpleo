document.getElementById('searchForm').addEventListener('submit', async function(e) {
    e.preventDefault(); 
    
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');

    loading.style.display = 'block';
    results.innerHTML = ''; 

    // Obtener datos del formulario
    const formData = {
        palabra_clave: document.getElementById('palabra_clave').value,
        discapacidad: document.getElementById('discapacidad').value,
        cantidad_ofertas: document.getElementById('cantidad_ofertas').value
    };
    
    // Configurar y enviar petición AJAX
    try{

        const response = await fetch('/procesar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        //checkResults();

        const data = await response.json();
        if (data.data.length > 0) {
            //clearInterval(interval);
            loading.style.display = 'none';
            showResults(data.data);
        }


    }catch(error){
        console.error('Error al obtener datos:', error);
        //clearInterval(interval);
        loading.style.display = 'none';
    }
    //.then(response => response.json())
    //.then(data => {
    //    // Mostrar respuesta
    //    document.getElementById('respuesta').innerHTML = `
    //        <div class="alert alert-success">${data.mensaje}</div>
    //    `;
    //    
    //    // Opcional: Limpiar formulario
    //    // document.getElementById('miFormulario').reset();
    //})
    //.catch(error => {
    //    console.error('Error:', error);
    //    document.getElementById('respuesta').innerHTML = `
    //        <div class="alert alert-danger">Hubo un error al procesar la solicitud</div>
    //    `;
    //});

    function checkResults() {
        const interval = setInterval(async () => {
            try {
                const response = await fetch('/get_data');
                const data = await response.json();

                if (data.data.length > 0) {
                    clearInterval(interval);
                    loading.style.display = 'none';
                    showResults(data.data);
                }
            } catch (error) {
                console.error('Error al obtener datos:', error);
                clearInterval(interval);
                loading.style.display = 'none';
            }
        }, 1000);
    }

    function showResults(jobs) {
        let html = `
            <table border="1" cellpadding="5" aria-describedby="jobTableDesc">
                <caption id="jobTableDesc">Lista de ofertas laborales encontradas</caption>
                <thead>
                    <tr>
                        <th scope="col">Puesto</th>
                        <th scope="col">Empresa</th>
                        <th scope="col">Ubicación</th>
                        <th scope="col">Enlace</th>
                    </tr>
                </thead>
                <tbody>
        `;
                
        jobs.forEach(job => {
            html += `
                <tr>
                    <td>${job.title}</td>
                    <td>${job.company}</td>
                    <td>${job.location}</td>
                    <td><a href="${job.link}" target="_blank" rel="noopener">Ver oferta</a></td>
                </tr>
            `;
        });
    
        html += `
                </tbody>
            </table>
        `;
        
        results.innerHTML = html;
    }




});


/**
 * aq
 * qwer
 * 
 * 
 * 
 * 
 * 
 
 {#
    <div id="loading" class="loading-container">
        🧠 Agente buscando ofertas laborales<span class="dot-flashing"></span>
    </div>
    <div id="results"></div>
    <script src="{{ url_for('static', filename='script.js') }}"></script>
   #}
    <script>
        /*
        const form = document.getElementById('searchForm');
        const loading = document.getElementById('loading');
        const results = document.getElementById('results');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            loading.style.display = 'block';
            results.innerHTML = ''; // limpiar resultados anteriores

            const formData = new FormData(form);

            try {
                await fetch('/', {
                    method: 'POST',
                    body: formData
                });

                checkResults();
            } catch (error) {
                console.error('Error:', error);
                loading.style.display = 'none';
            }
        });

        function checkResults() {
            const interval = setInterval(async () => {
                try {
                    const response = await fetch('/get_data');
                    const data = await response.json();

                    if (data.data.length > 0) {
                        clearInterval(interval);
                        loading.style.display = 'none';
                        showResults(data.data);
                    }
                } catch (error) {
                    console.error('Error al obtener datos:', error);
                    clearInterval(interval);
                    loading.style.display = 'none';
                }
            }, 1000);
        }

        function showResults(jobs) {
            let html = `
                <table border="1" cellpadding="5" aria-describedby="jobTableDesc">
                    <caption id="jobTableDesc">Lista de ofertas laborales encontradas</caption>
                    <thead>
                        <tr>
                            <th scope="col">Puesto</th>
                            <th scope="col">Empresa</th>
                            <th scope="col">Ubicación</th>
                            <th scope="col">Enlace</th>
                        </tr>
                    </thead>
                    <tbody>
            `;
                    
            jobs.forEach(job => {
                html += `
                    <tr>
                        <td>${job.title}</td>
                        <td>${job.company}</td>
                        <td>${job.location}</td>
                        <td><a href="${job.link}" target="_blank" rel="noopener">Ver oferta</a></td>
                    </tr>
                `;
            });
        
            html += `
                    </tbody>
                </table>
            `;
            
            results.innerHTML = html;
        }


*/



