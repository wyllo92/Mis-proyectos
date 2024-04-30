
        function quitarCerosNoSignificativos(numeroComoCadena) {
            let numeroSinComa = numeroComoCadena.replace(',', '.');
            let numeroSinCeros = parseFloat(numeroSinComa);
            return numeroSinCeros;
        }
        

        
        let prueba1 = "00001843,45000";
        

        console.log(quitarCerosNoSignificativos(prueba1)); 
        
        

