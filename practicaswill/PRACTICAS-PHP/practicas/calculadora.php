<style>

.resultado{
        color:#f00;
        font-weight:bold;
        font-size: 32px;
        
    }

</style>

<?php
    
    function calcular($calculo){
        if(!strcmp("suma",$calculo)){
            global $numero1;
            global $numero2;
            
            $resultado=$numero1+$numero2;

            echo "<p class='resultado'> El resultado es: $resultado</p>";
        }

        if(!strcmp("resta", $calculo)){
            global $numero1;
            global $numero2;
            
            $resultado =$numero1-$numero2;

            echo "<p class='resultado'> El resultado es: $resultado</p>";
        }

        if(!strcmp("multiplicacion", $calculo)){
            global $numero1;
            global $numero2;
            
            $resultado =$numero1*$numero2;

            echo "<p class='resultado'> El resultado es: $resultado</p>";
        }

        if(!strcmp("division", $calculo)){
            global $numero1;
            global $numero2;
            
            $resultado =$numero1/$numero2;

            echo "<p class='resultado'> El resultado es: $resultado</p>";
        }

        if(!strcmp("modulo", $calculo)){
            global $numero1;
            global $numero2;
            
            $resultado =$numero1%$numero2;

            echo "<p class='resultado'> El resultado es: $resultado</p>";
        }

        if(!strcmp("incremento", $calculo)){
            global $numero1;
            $numero1++;
            
            $resultado =$numero1;

            echo "<p class='resultado'> El resultado es: $resultado</p>";
        }

        if(!strcmp("decremento", $calculo)){
            global $numero1;
            $numero1--;
            
            
            $resultado =$numero1;

            echo "<p class='resultado'> El resultado es: $resultado</p>";
        }
    }
?>