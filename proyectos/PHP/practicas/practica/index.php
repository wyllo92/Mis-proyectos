<?php

require_once('clases/Personas.php');

/*$peruano= new Peruano;
$peruano-> setNombre("wIlLiaM aRiAs");

$chileno= new Chileno;


var_dump($peruano);

var_dump($chileno);*/

$chileno= new Peruano;   
$chileno->setApellido("arias", "benavides" );

echo "<br>";
var_dump($chileno);