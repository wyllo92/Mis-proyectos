<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php

        /*$datos= array("nombre"=>"william", "apellido"=>"arias", "edad"=>"50");
        $datos["pais"]="españa";
        foreach($datos as $clave=>$valor){
            echo "a $clave le corresponde $valor <br>";
        }*/

        /*$semana[]="lunes";
        $semana[]="martes";
        $semana[]="miercoles";
        $semana[]="jueves"; 

        for($i=0;$i<count($semana);$i++){
            echo $semana[$i] . "<br>";

        }*/

        /*$datos= array("lunes", "martes","miercoles","jueves");
        sort($datos);
            for($i=0; $i<count($datos); $i++){
                echo $datos[$i] . "<br>";

            }*/
        $persona=[
            "nombre"=>"juan",
            "edad"=>"18",
            "ciudad"=>"madrid"
        ];
        ["nombre"=>$elnombre, "edad"=>$laedad, "ciudad"=>$laciudad]=$persona;

        echo "nombre: $elnombre<br>";
        echo "edad: $laedad <br>";
        echo "ciudad: $laciudad <br>";
    ?>
</body>
</html>