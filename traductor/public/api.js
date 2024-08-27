const express = require('express');

const app = express();


app.get('/mensaje', (req, res) => {

  const mensaje = { mensaje: 'El fracaso es simplemente una nueva oportunidad de empezar de nuevo, esta vez de forma más inteligente' };
  res.json(mensaje);

});


app.listen(3000, () => {

  console.log('API en línea en el puerto 3000');

});