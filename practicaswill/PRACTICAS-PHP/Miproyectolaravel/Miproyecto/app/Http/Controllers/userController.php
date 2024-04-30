<?php

namespace App\Http\Controllers;

use Illuminate\http\Request;

class UserController extends Controller{

    public function index(){
        $name= "willy";
        $apellido= "wonka";
        $edad=32;

        return view('example', ['name'=>$name, 'apellido'=> $apellido, 'edad'=>$edad]);

    }

    public function home()
    {
        return view('welcome');
    }

    public function showname($name){

        return view('example', ['name'=>$name]);

    }

    
    public function suma($num=0){

        $b=80;

        return $num+$b;

    }
}



