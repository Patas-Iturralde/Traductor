import React, { useState, useEffect } from 'react';

import axios from 'axios';


function App() {

    const [users, setUsers] = useState([]);


    useEffect(() => {

        axios.get('http://localhost:3000/mensaje_es')

            .then(response => {

                setUsers(response.data);

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