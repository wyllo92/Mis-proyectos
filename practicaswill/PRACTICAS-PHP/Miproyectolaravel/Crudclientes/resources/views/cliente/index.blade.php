@extends('home')

@section('content')

<x-nave />

<div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-8">
        <br><br><br>
        <h3>lista de clientes</h3>
        <br>
        <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#create">
            nuevo
        </button>
        <div class="table-responsive">
            <br>
            <table class="table">
                <thead class="bg-dark text-white">
                    <tr>
                        <th scope="col"> id </th>
                        <th scope="col"> nombre </th>
                        <th scope="col">telefono</th>
                        <th scope="col">correo</th>
                        <th scope="col">acciones</th>
                    </tr>
                </thead>
                <tbody>
                    @foreach ($clientes as $cliente)
                    <tr class="">
                        <td scope="row"> {{$cliente->id}} </td>
                        <td> {{$cliente->nombre}} </td>
                        <td> {{$cliente->telefono}} </td>
                        
                        <td> {{$cliente->correo}} </td>
                        <td>
                            <button type="button" class="btn btn-success" data-toggle="modal" data-target="#edit{{$cliente->id}}">
                                actualizar
                            </button>
                            <button type="button" class="btn btn-danger" data-toggle="modal" data-target="#delete{{$cliente->id}}">
                                eliminar
                            </button>
                        </td>
                    </tr>
                    @include('cliente.info')
                    @endforeach
                </tbody>
            </table>
        </div>
        @include('cliente.create')
        

    </div>
    <div class="col-md-2"></div>
</div>
    
@endsection