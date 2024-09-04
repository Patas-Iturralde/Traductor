const express = require('express');
const axios = require('axios');
const cors = require('cors');
const app = express();
app.use(cors({
  origin: ['http://localhost:5000', 'http://localhost:3000'], // Permitir solicitudes desde la API de Flask y la aplicación React

  

})); 


const mysql = require('mysql2/promise');
const bodyParser = require('body-parser');
app.use(bodyParser.json());

const db = mysql.createPool({

  host: 'localhost',

  user: 'root',

  password: 'root',

  database: 'traductor'

});

app.get('/mensaje_es', async (req, res) => {

  try {

    const [rows] = await db.execute('SELECT * FROM mensaje_espanol');

    res.json(rows);

  } catch (error) {

    console.error(error);

    res.status(500).json({ message: 'Error al obtener mensaje' });

  }

});

app.post('/mensaje_es', async (req, res) => {

  try {

    const truncate = 'TRUNCATE TABLE mensaje_espanol';

    const ej = await db.execute(truncate);

    const { mensaje } = req.body; // Obtener el mensaje desde el cuerpo de la solicitud

    const query = 'INSERT INTO mensaje_espanol (mensaje) VALUES (?)';

    const result = await db.execute(query, [mensaje]);

    res.json({ message: 'Mensaje traducido insertado correctamente' });

  } catch (error) {

    console.error(error);

    res.status(500).json({ message: 'Error al insertar mensaje traducido' });

  }

});


app.get('/mensaje_en', async (req, res) => {

  try {

    const [rows] = await db.execute('SELECT * FROM mensaje_ingles');

    res.json(rows);

  } catch (error) {

    console.error(error);

    res.status(500).json({ message: 'Error al obtener mensaje' });

  }

});

app.post('/mensaje_en', async (req, res) => {

  try {

    const truncate = 'TRUNCATE TABLE mensaje_ingles';

    const ej = await db.execute(truncate);


    const { mensaje } = req.body; // Obtener el mensaje desde el cuerpo de la solicitud

    const query = 'INSERT INTO mensaje_ingles (mensaje_in) VALUES (?)';

    const result = await db.execute(query, [mensaje]);

    res.json({ message: 'Mensaje traducido insertado correctamente' });

  } catch (error) {

    console.error(error);

    res.status(500).json({ message: 'Error al insertar mensaje traducido' });

  }

});

app.get('/mensaje_fr', async (req, res) => {

  try {

    const [rows] = await db.execute('SELECT * FROM mensaje_fances');

    res.json(rows);

  } catch (error) {

    console.error(error);

    res.status(500).json({ message: 'Error al obtener mensaje' });

  }

});

app.post('/mensaje_fr', async (req, res) => {

  try {

    const truncate = 'TRUNCATE TABLE mensaje_fances';

    const ej = await db.execute(truncate);


    const { mensaje } = req.body; // Obtener el mensaje desde el cuerpo de la solicitud

    const query = 'INSERT INTO mensaje_fances (mensaje_fr) VALUES (?)';

    const result = await db.execute(query, [mensaje]);

    res.json({ message: 'Mensaje traducido insertado correctamente' });

  } catch (error) {

    console.error(error);

    res.status(500).json({ message: 'Error al insertar mensaje traducido' });

  }

});

app.post('/translate', async (req, res) => {
  try {

    const response = await axios.post('http://localhost:5000/translate');

    const translatedMessage = response.data;


    // Devolver la traducción en formato JSON

    res.json({ translatedMessage });
    console.log("como: ",translatedMessage)

  } catch (error) {

    console.error(error);

    res.status(500).json({ message: 'Error al traducir mensaje' });

  }

});

app.post('/translate_fr', async (req, res) => {
  try {

    const response = await axios.post('http://localhost:5000/translate_fr');

    const translatedMessage = response.data;


    // Devolver la traducción en formato JSON

    res.json({ translatedMessage });
    console.log("como: ",translatedMessage)

  } catch (error) {

    console.error(error);

    res.status(500).json({ message: 'Error al traducir mensaje' });

  }

});
  




app.listen(3001, () => {

  console.log('API en línea en el puerto 3001');

});