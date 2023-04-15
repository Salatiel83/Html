function generarNumeroAleatorio() {
  // Genera un número aleatorio entre 0 y 1
  const numeroAleatorio = Math.random();

  // Multiplica el número aleatorio por 100 y redondea hacia abajo para obtener un número entero entre 0 y 99
  const numeroEntre0y99 = Math.floor(numeroAleatorio * 100);

  // Suma 1 para obtener un número entero entre 1 y 100
  const numeroEntre1y100 = numeroEntre0y99 + 1;

  // Devuelve el número aleatorio generado
  return numeroEntre1y100;
}
const numeroAleatorio = generarNumeroAleatorio();
console.log(numeroAleatorio); // Imprime un número aleatorio entre 1 y 100 en la consola
