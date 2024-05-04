@extends('layouts/templade')

@section('title', 'alumnos|escuela')

@section('contenido')

<main>
    <div class="conatiner py-4">
        <h2>listado de alumnos</h2>

        <a href="{{url('alumnos/create')}}" class="btn btn-primary btn-sm">nuevo registro</a>

    </div>
</main>