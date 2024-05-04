<?php

class Persona{

    public $nombre, $edad;
    public $apellido1, $apellido2;       

    public function setNombre($nombre){

        $this->nombre= strtolower($nombre);
        
    }

    public function getNombre(){

        return ucwords($this->nombre);
        
    }

    public function setApellido($apellido1, $apellido2){
        $this->apellido1= $apellido1;
        $this->apellido2= $apellido2;
    }

    public function getApellidos(){
        return $this->apellido1 ." ". $this->apellido2;
       

    }
}

class Peruano extends Persona{
    public $departamneto, $ciudad;

    public function setApellido($apellido1, $apellido2){

        parent::setApellido($apellido1, $apellido2);

        echo "los apellidos se asignaron con exito";
    }
}

class Chileno extends Persona{
    public $region, $comuna;

    public function setApellido($apellido1, $apellido2){
        $this->apellido1= $apellido2;
        $this->apellido2= $apellido1;

    }
}