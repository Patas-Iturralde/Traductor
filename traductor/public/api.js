const express = require('express');

const app = express();


app.get('/mensaje', (req, res) => {

  const mensaje = { mensaje: 'Hola, como estás' };
  res.json(mensaje);

});


app.listen(3000, () => {

  console.log('API en línea en el puerto 3000');

});