<?php

    class Coche{
        var $ruedas;
        var $color;
        var $motor;

        function __construct(){
            $this->ruedas=4;
            $this->color="";
            $this->motor="1600";
            
        }
        function arrancar(){
            echo "estoy arrancando <br>";
        }
        function girar(){
            echo "estoy girando <br>";
        }
        function frenar(){
            echo "estoy frenando <br>";
        }
        function establece_color($color_coche, $nombre_coche){
            $this->color= $color_coche;
            echo "el nombre del coche es: " . $nombre_coche . " y el color es:" . $this->color."<br>";
        }
    }


    class Camion extends Coche{

        function __construct(){
            $this->ruedas=8;
            $this->color="";
            $this->motor="3500";
            }

        function establece_color($color_camion, $nombre_camion){
            $this->color= $color_camion;
            echo "el nombre del coche es futon y el color es:" . $this->color."<br>";
        }
        
    }

    
?>
