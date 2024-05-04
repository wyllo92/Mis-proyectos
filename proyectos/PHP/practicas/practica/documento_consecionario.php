<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php

        include("concesionario.php");

        Compra_vehiculo::descuento_gobierno();
        $compra_antonio= new Compra_vehiculo("compacto");
        $compra_antonio->climatizador();
        $compra_antonio->tapiceria_cuero("blanco");
        echo $compra_antonio-> precio_final()."<br>";

        $compra_ana= new Compra_vehiculo("compacto");
        $compra_ana->climatizador();
        $compra_ana-> tapiceria_cuero("roja");
        echo $compra_ana->precio_final();

    
    ?>
</body>
</html>