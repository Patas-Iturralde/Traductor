import React, { useState, useEffect } from 'react';

import axios from 'axios';


function App() {

    const [mensaje, setMensaje] = useState([]);


    useEffect(() => {

        axios.get('http://localhost:3000/mensaje_en')

            .then(response => {

                setMensaje(response.data);

            })

            .catch(error => {

                console.error(error);

            });

    }, []);


    return (

        <div>

            <h1>Usuarios</h1>

            <ul>

                {users.map(user => (

                    <li key={user.id}>{user.name}</li>

                ))}

            </ul>

        </div>

    );

}


export default App;