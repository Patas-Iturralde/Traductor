const express = require('express');
const app = express();
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

    res.status(500).json({ message: 'Error al obtener usuarios' });

  }

});

app.post('/mensaje_en', async (req, res) => {

  try {

    const { mensaje } = req.body; // Obtener el mensaje desde el cuerpo de la solicitud

    const query = 'INSERT INTO mensaje_ingles (mensaje_in) VALUES (?)';

    const result = await db.execute(query, [mensaje]);

    res.json({ message: 'Mensaje traducido insertado correctamente' });

  } catch (error) {

    console.error(error);

    res.status(500).json({ message: 'Error al insertar mensaje traducido' });

  }

});


app.listen(3000, () => {

  console.log('API en línea en el puerto 3000');

});