<?php
    

    $conexion= new mysqli("localhost", "root", "", "primera_base");
        if($conexion->connect_errno){
            echo"fallo al conectar.";
            exit();

        }
    /*$consulta="SELECT * FROM nueva";
    $resultado=mysqli_query($conexion, $consulta);
    $fila= mysqli_fetch_row($resultado);
    echo $fila[0] . " ";
    echo $fila[1] . " ";
    echo $fila[2] . " ";
    echo $fila[3] . " ";*/
    
?>